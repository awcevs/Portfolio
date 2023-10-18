from flask import Flask, render_template, jsonify, request, redirect
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import pandas as pd
import json
import time
import threading
import re
from datetime import datetime, timedelta
from transformers import pipeline, AutoModel, AutoTokenizer
from sqlalchemy import create_engine, select
import sqlalchemy
import pymysql
from pykrx import stock as stk
import FinanceDataReader as fdr
from apscheduler.schedulers.background import BackgroundScheduler
import threading

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

today = datetime.today().strftime("%Y%m%d") # 오늘 날짜

# 메인화면 종합 주가지수 ======================================================================
# kospi, kosdaq, kospi200 정보 dict로 리턴
def GetStockIndex():
    pd.options.display.float_format = '{:.2f}'.format
    try:
        df_kospi = stk.get_index_price_change(today, today,'KOSPI')
        df_kosdaq = stk.get_index_price_change(today, today,'KOSDAQ')
    # 월요일 오전에 오류뜰 때
    except:
        df_kospi = stk.get_index_price_change(str(int(today)-3), today, 'KOSPI')
        df_kosdaq = stk.get_index_price_change(str(int(today)-3), today, 'KOSDAQ')
    df_market = pd.concat([df_kospi,df_kosdaq])
    df_market['전일비'] = df_market['종가'] - df_market['시가']
    df_market = df_market.loc[['코스피','코스닥','코스피 200'],['종가','전일비','등락률']]
    kospi = df_market.to_dict('records')[0]
    kosdaq = df_market.to_dict('records')[1]
    kospi200 = df_market.to_dict('records')[2]
    return kospi, kosdaq, kospi200

# 현재 주식 가격정보 데이터프레임 ===========================================================
# 모든 종목의 가격정보 데이터프레임으로 리턴
def GetData():
    pd.options.display.float_format = '{:.2f}'.format
    try:
        df_kospi = stk.get_market_price_change(today, today, market='KOSPI')
        df_kospi['시장구분'] = '코스피'
        df_kosdaq = stk.get_market_price_change(today, today, market='KOSDAQ')
        df_kosdaq['시장구분'] = '코스닥'
        df_konex = stk.get_market_price_change(today, today, market='KONEX')
        df_konex['시장구분'] = '코넥스'
    # 월요일 오전에 오류뜰 때
    except:
        df_kospi = stk.get_market_price_change(str(int(today)-3), today, market='KOSPI')
        df_kospi['시장구분'] = '코스피'
        df_kosdaq = stk.get_market_price_change(str(int(today)-3), today, market='KOSDAQ')
        df_kosdaq['시장구분'] = '코스닥'
        df_konex = stk.get_market_price_change(str(int(today)-3), today, market='KONEX')
        df_konex['시장구분'] = '코넥스'
    df_krx = pd.concat([df_kospi, df_kosdaq, df_konex])
    df_krx.rename(columns = {'시가' : '전일가','종가' : '현재가','변동폭' : '전일비'}, inplace = True)
    df_krx.index.name = '종목코드'
    df_marCap = stk.get_market_cap(today)
    df_marCap = df_marCap['시가총액']
    df_marCap.index.name = '종목코드'
    df = pd.merge(df_krx, df_marCap, on='종목코드')
    df['관심종목'] = 0
    df['고가'] = 0
    df['저가'] = 0
    df = df.reset_index()
    return df

# 업데이트용 데이터프레임 (종목명, 시장구분 안들어가있음)
def UpdateData():
    pd.options.display.float_format = '{:.2f}'.format

    df_today = stk.get_market_ohlcv(today)
    df_today['전일비'] = df_today['종가'] - df_today['시가']
    df_today.rename(columns = {'시가' : '전일가', '종가' : '현재가'}, inplace = True)
    df_today.index.name = '종목코드'

    df_marCap = stk.get_market_cap(today)
    df_marCap = df_marCap['시가총액']
    df_marCap.index.name = '종목코드'

    df = pd.merge(df_today, df_marCap, on='종목코드')
    df = df.reset_index()
    return df


# 주식 데이터 가져와서 DB에 Insert (관심종목 초기화 됨 - 맨처음 DB 만들때만 사용할것) ==========
def InsertDB():
    pd.options.display.float_format = '{:.2f}'.format
    df = GetData()
    db_connection_str = 'mysql+pymysql://stock:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    dtype = {'종목코드':sqlalchemy.types.VARCHAR(6), 
             '종목명':sqlalchemy.types.VARCHAR(30),
             '등락률':sqlalchemy.types.Float,
             '시장구분':sqlalchemy.types.VARCHAR(6),
             '관심종목':sqlalchemy.types.VARCHAR(1),
             '고가':sqlalchemy.types.INTEGER,
             '저가':sqlalchemy.types.INTEGER}
    df.to_sql(name='stock', con=db_connection, if_exists='replace',index=False, dtype=dtype)
    conn.execute('ALTER TABLE stock ADD PRIMARY KEY (종목코드);')
    conn.close()

# 주식 데이터 가져와서 DB에 Update (관심종목 초기화 X) ========================================
def UpdateDB():
    pd.options.display.float_format = '{:.2f}'.format
    df = GetData()
    db_connection_str = 'mysql+pymysql://stock:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    for i in df.index:
        sql  = ''
        sql += 'UPDATE stock SET '
        sql += "전일가 = '" + str(df.loc[i]['전일가']) + "', "
        sql += "고가 = '" + str(df.loc[i]['고가']) + "', "
        sql += "저가 = '" + str(df.loc[i]['저가']) + "', "
        sql += "현재가 = '" + str(df.loc[i]['현재가']) + "', "
        sql += "거래량 = '" + str(df.loc[i]['거래량']) + "', "
        sql += "거래대금 = '" + str(df.loc[i]['거래대금']) + "', "
        sql += "전일비 = '" + str(df.loc[i]['전일비']) + "', "
        sql += "등락률 = '" + str(df.loc[i]['등락률']) + "', "
        sql += "시가총액 = '" + str(df.loc[i]['시가총액']) + "' "
        sql += "WHERE 종목코드 = '" + str(df.loc[i]['종목코드']) + "'"
        conn.execute(sql)
    conn.close()

# DB에서 데이터 가져오는 함수 (기본 num=100, 메인 페이지에서는 num=5 넣어서 사용) ==========
# 상위종목 데이터를 데이터프레임으로 리턴
def GetStockTop(num=100, sort='거래량'):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql = 'SELECT * FROM stock '
    if sort == '거래량':
        sql += "order by 거래량 desc limit 0,100"
    if sort == '상승':
        sql += "order by 등락률 desc limit 0,100"
    if sort == '하락':
        sql += "order by 등락률 limit 0,100"
    if sort == '시가총액':
        sql += "order by 시가총액 desc limit 0,100"
    df = pd.read_sql(sql, conn)
    conn.close()
    return df.head(num)

# 이름으로 DB에서 종목코드 가져오는 함수 ==================================================
def GetCode(stock_name):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql = "SELECT 종목코드 from stock where 종목명 = '" + stock_name + "'"
    result = conn.execute(sql)
    conn.close()
    return result.fetchall()[0][0]

# 검색 함수 ======================================================================
def Search(string):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql = "SELECT 종목명, 종목코드 FROM stock WHERE (종목명 LIKE '%%" + string + "%%' or 종목코드 LIKE '%%" + string + "%%');"
    result = conn.execute(sql)
    conn.close()
    stock_name, stock_code = result.fetchall()[0]
    return stock_name, stock_code

# 종목명 -> 종목코드 ============================================================
def NameToCode(stock_name):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql = "SELECT 종목코드 from stock where 종목명 = '" + stock_name + "'"
    result = conn.execute(sql)
    conn.close()
    return result.fetchall()[0][0]

# 종목코드 -> 종목명 ============================================================
def CodeToName(stock_code):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql = "SELECT 종목명 from stock where 종목코드 = '" + stock_code + "'"
    result = conn.execute(sql)
    conn.close()
    return result.fetchall()[0][0]
    
# 특정 종목 정보 ======================================================================
# 종목코드 받아서 해당 종목의 가격정보 데이터프레임으로 리턴
def GetStock(stock_code):
    pd.options.display.float_format = '{:.2f}'.format
    df_item = stk.get_market_ohlcv(str(int(today) - 3), today, stock_code) # 월요일에 전주 금요일 데이터까지 가져옴
    df_item['전일가'] = df_item['종가'].shift(1) # 전일의 종가를 전일가로 컬럼 추가
    df_item = df_item.fillna(0)
    df_item.rename(columns={'종가':'현재가'}, inplace = True)
    df_item = df_item.astype({'전일가':'int'})
    df_item['전일비'] = df_item['현재가'] - df_item['전일가']
    df_item['종목명'] = stk.get_market_ticker_name(stock_code)
    df_item['종목코드'] = stock_code
    df_item = df_item.iloc[[-1]]
    return df_item

# 관심종목 설정하는 함수 ============================================================
# 종목코드 받아서 DB에 관심종목으로 update
def SetFav(stock_code):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql  = ''
    sql += 'UPDATE stock SET '
    sql += "관심종목 = '1' "
    sql += "where 종목코드 = '" + stock_code + "' "
    conn.execute(sql)
    conn.close()

# 관심종목 리스트 불러오는 함수 ============================================================
# 관심종목의 종목코드 리스트로 리턴
# for stock_code in GetFav():
#     NewsCrawl(stock_code)
# 로 사용
def GetFav():
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql = 'SELECT 종목코드 FROM stock WHERE 관심종목 = 1 '
    df_code = pd.read_sql(sql, conn)
    conn.close()
    return list(df_code['종목코드'])

# 60 페이지 크롤링해서 10일전까지의 뉴스 DB에 넣는 함수 ========================================
def NewsCrawl(stock_code):
    db_connection_str = 'mysql+pymysql://news:ezen@127.0.0.1:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    
    for i in range(1,51):
        page_n = i
        url = f"https://finance.naver.com/item/news_news.nhn?code={stock_code}&page={page_n}&sm=title_entity_id.basic&clusterId="
        soup = requests.get(url).text
        html = bs(soup, "lxml")

        #링크 가지고 오기
        links = html.select('.title')
        link_result = []
        for link in links:
            href = link.find('a')['href']
            office_id = href.split('office_id=')[1][0:3]
            article_id = href.split('article_id=')[1][0:10]
            add = 'https://n.news.naver.com/mnews/article/' + office_id + '/' + article_id
            link_result.append(add)
            #print(add)
        # 뉴스 날짜 가지고 오기
        dates = html.select('.date')
        date_result = [date.get_text()for date in dates]
        date_result

        # 링크, 날짜로만 데이터프레임 (중복제거, 날짜 제한해서 데이터 줄인 후 제목 추출할 것)
        result = {"종목코드": stock_code, "기사링크": link_result, "날짜": date_result}
        if i == 1:
            df_news = pd.DataFrame(result) # 1페이지에서 데이터프레임 생성
        elif i != 1:
            df_temp = pd.DataFrame(result) # 1페이지 이후에 데이터프레임 concat
            df_news = pd.concat([df_news,df_temp])
    
    # 데이터프레임 내에서 중복되는 링크 제거
    df_news.drop_duplicates(subset='기사링크', keep='last', inplace=True)
    
    # DB와 중복되는 링크 제거
    sql = "SELECT 기사링크 FROM news where 종목코드 ='" + stock_code + "'"
    df_dup = pd.read_sql(sql, conn) # 중복 링크용 데이터프레임
    links = list(df_dup['기사링크']) # 중복 링크 리스트
    for link in links:
        df_news.drop(df_news[df_news['기사링크'] == link].index, axis=0, inplace=True)

    # 10일전까지의 뉴스만 분리
    df_news['날짜'] = pd.to_datetime(df_news['날짜']) # 날짜 컬럼 datetime 으로
    fromdate = datetime.today() - timedelta(10)
    fromdate = fromdate.strftime('%Y.%m.%d')
    df_news = df_news[df_news['날짜'] >= fromdate] # 10일 전부터 오늘까지
    df_news.reset_index(drop=True, inplace=True) # 중복 인덱스 제거
    
    # 링크 들어가서 제목 가져옴
    title_result = []

    for link in df_news['기사링크']:
        print(link)
        soup = requests.get(link).text
        html = bs(soup, "lxml")
        try:
            title = html.select('#title_area')[0].get_text()
        # 제목 태그가 달라서 오류나는 경우( 스포츠 뉴스 )
        except:
            title = html.select('.title')[0].get_text()
        title = re.sub('\n', '', title)
        title_result.append(title)

    dtype = {'종목코드':sqlalchemy.types.VARCHAR(6),
             '날짜':sqlalchemy.types.DateTime}

    df_news['기사제목'] = title_result

    df_news.to_sql(name='news', con=db_connection, if_exists='append',index=False, dtype=dtype)
    conn.close()

# DB에서 뉴스 가져오는 함수 ============================================================
def GetNews(stock_code):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    select_time = (datetime.today() - timedelta(10)).strftime("%Y-%m-%d")
    sql  = "SELECT "
    sql += "*, "
    sql += "(SELECT 분석 FROM opinion WHERE opinion.뉴스번호 = news.뉴스번호 and 문장여부 = '0') as 분석, "
    sql += "(SELECT 점수 FROM opinion WHERE opinion.뉴스번호 = news.뉴스번호 and 문장여부 = '0') as 점수 "
    sql += "FROM news "
    sql += "WHERE 종목코드 = '" + stock_code + "' "
    sql += "and 날짜 >= '" + select_time + "' "
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

# 오피니언 분석 함수 ======================================================================
def opinion(text):

    pipe_fin = pipeline("text-classification", model="snunlp/KR-FinBert-SC", tokenizer="snunlp/KR-FinBert-SC")

    #print("KR-FinBert-SC :\n\t", pipe_fin(text, max_length=512, truncation=True))
    #print(text)
    #print(pipe_fin(text, max_length=512, truncation=True)[0],'\n')

    label = pipe_fin(text, max_length=512, truncation=True)[0]['label']
    score = pipe_fin(text, max_length=512, truncation=True)[0]['score']
    return label, score

# 분석해서 DB에 넣는 함수 ============================================================
def NewsOpinion():
    pd.options.display.float_format = '{:.6f}'.format
    newsNo_result = []
    code_result = []
    link_result = []
    text_result = []
    label_result = []
    score_result = []
    issentence_result = []
    db_connection_str = 'mysql+pymysql://opinion:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    # 분석 안된 링크(opinion 테이블에 없는 링크)만 select
    sql  = "SELECT 뉴스번호, 종목코드, 기사링크 FROM news "
    sql += "WHERE 뉴스번호 NOT IN (SELECT 뉴스번호 FROM opinion) "
    df_link = pd.read_sql(sql, conn)
    # 기사링크 들어가서 내용 크롤링
    for i in df_link.index:
        newsNo = df_link.loc[i]['뉴스번호']
        code = df_link.loc[i]['종목코드']
        link = df_link.loc[i]['기사링크']
        
        newsDup = "SELECT 뉴스번호 FROM opinion WHERE 뉴스번호 ='" + str(newsNo) + "'"
        if len(conn.execute(newsDup).fetchall()) != 0:
            print('* 중복 [ ' + str(newsNo) + " ] " + link)
            continue
        print("\n[ 분석 ] (" , i + 1 , "/" , df_link.index.stop , ") " + link + " 시작 : " + time.strftime("%H:%M:%S"))
        
        soup = requests.get(link).text
        html = bs(soup, "lxml")
        try:
            article = str(html.select('#dic_area')[0]).replace('\n','<br/>').replace('data-src','src') # DB에 들어갈 html 태그 포함 내용
            article_text = html.select_one('#dic_area').get_text()
            article_text = re.sub('\n', '', article_text) # 분석용 태그 제거 텍스트
        # 스포츠 뉴스일 경우 태그가 다름
        except:
            article = str(html.select('#newsEndContents')[0]).replace('\n','<br/>').replace('data-src','src')
            newsad1 = str(html.select('.reporter_area')[0])
            newsad2 = str(html.select('.copyright')[0])
            newsad3 = str(html.select('.categorize')[0])
            newsad4 = str(html.select('.promotion')[0])
            newsad5 = str(html.select('.source')[0])
            newsad6 = str(html.select('.byline')[0])    
            article = article.replace(newsad1,'').replace(newsad2,'').replace(newsad3,'').replace(newsad4,'').replace(newsad5,'').replace(newsad6,'')
            article_text = bs(article, 'lxml').select_one('#newsEndContents').get_text()
            article_text = re.sub('\n', '', article_text) # 분석용 태그 제거 텍스트
        article_label, article_score = opinion(article_text)
        newsNo_result.append(newsNo)
        code_result.append(code)
        link_result.append(link)
        text_result.append(article)
        label_result.append(article_label)
        score_result.append(article_score)
        issentence_result.append('0')
        sentences = article.split('.')
        for sentence in sentences:
            sentence_label, sentence_score = opinion(sentence)
            newsNo_result.append(newsNo)
            code_result.append(code)
            link_result.append(link)
            text_result.append(sentence.replace("'","''"))
            label_result.append(sentence_label)
            score_result.append(sentence_score)
            issentence_result.append('1')
        result = {"뉴스번호": newsNo_result, "종목코드" : code_result, "기사링크": link_result,"내용": text_result, 
                  "분석": label_result, "점수": score_result, "문장여부":issentence_result}
        df_opinion = pd.DataFrame(result)
        df_opinion.to_sql(name='opinion', con=db_connection, if_exists='append',index=False)
        print("[ 분석 ] (" , i + 1 , "/" , df_link.index.stop , ") " + link + " 종료 : " + time.strftime("%H:%M:%S"))
        newsNo_result = []
        code_result = []
        link_result = []
        text_result = []
        label_result = []
        score_result = []
        issentence_result = []
    conn.close()

# 해당 링크의 오피니언 분석 가져오는 함수 ==================================================
# 뉴스링크 받아서 뉴스정보, 문장들 분석정보 리턴
def GetOpinion(link):
    db_connection_str = 'mysql+pymysql://ezen:ezen@192.168.0.215:3306/stock'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
    sql  = "SELECT *, "
    sql += "(select 기사제목 from news where 기사링크 = '" + link + "') as 기사제목 "
    sql += "FROM opinion WHERE 기사링크 = '" + link + "'"
    df = pd.read_sql(sql, conn)
    conn.close()
    newsNo = str(df.loc[0]['뉴스번호'])
    stock_code = df.loc[0]['종목코드']
    title = df.loc[0]['기사제목']
    article = df.loc[0]['내용']
    article_label = df.loc[0]['분석']
    article_score = df.loc[0]['점수']
    df_sentence = df[['내용', '분석', '점수']][1:]
    # 긍정, 부정 점수순으로 정렬한 딕셔너리, positive[0]['내용'] 형식으로 받아쓰면 됨
    positive = df_sentence.loc[df_sentence['분석']=='positive'].sort_values('점수', ascending=False).reset_index().to_dict('records')
    negative = df_sentence.loc[df_sentence['분석']=='negative'].sort_values('점수', ascending=False).reset_index().to_dict('records')
    return newsNo, stock_code, title, article, article_label, article_score, positive, negative

# 스케줄러 ================================================================================

# 오피니언분석 함수 쓰레드용 함수
def OpinionTimer():
    while int(time.strftime("%H")) >= 9 and int(time.strftime("%H")) < 17:
        print('[ opinion ]')
        NewsOpinion()
        time.sleep(5)

job_defaults = {'max_instances': 10}

sched = BackgroundScheduler(job_defaults=job_defaults, daemon=True, timezone='Asia/Seoul')

def stock():
    print('[ stock ]')
    if int(time.strftime("%H")) < 9 or int(time.strftime("%H")) >= 17:
        sched.remove_job('stock')
    else:
        print("\n[ 주식 ] 데이터 갱신 시작 : " + time.strftime("%H:%M:%S"))
        UpdateDB()
        print("[ 주식 ] 데이터 갱신 종료 : " + time.strftime("%H:%M:%S"))
        time.sleep(5)
        
def news():
    print('[ news ]')
    if int(time.strftime("%H")) < 9 or int(time.strftime("%H")) >= 7:
        sched.remove_job('news')
    else:
        print("\n[ 뉴스 ] 크롤링 시작 : " + time.strftime("%H:%M:%S"))
        for stock_code in GetFav():
            NewsCrawl(stock_code)
        print("[ 뉴스 ] 크롤링 종료 : " + time.strftime("%H:%M:%S"))
        time.sleep(5)
    
sched.add_job(stock, 'cron', day_of_week='0-4', hour='9-17', minute='*', misfire_grace_time=60, id='stock')
sched.add_job(news, 'cron', day_of_week='0-4', hour='9-17', minute='*/5', misfire_grace_time=60, id='news')

sched.start()

OpinionThread = threading.Thread(target=OpinionTimer)
OpinionThread.daemon = True # 백그라운드로 작동하게 함
OpinionThread.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True, threaded=True)