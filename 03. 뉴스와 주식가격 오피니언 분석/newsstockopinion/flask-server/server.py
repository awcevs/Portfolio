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
from flask_cors import CORS
    
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r'*': {'origins': '*'}})

today = datetime.today().strftime("%Y%m%d") # 오늘 날짜

# 메인화면 종합 주가지수 ======================================================================
# kospi, kosdaq, kospi200 정보 dict로 리턴
@app.route('/stockindex', methods=['GET','POST'])
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
    #return kospi, kosdaq, kospi200
    return { "kospi" : kospi, "kosdaq" : kosdaq, "kospi200" : kospi200 }

if __name__ == "__main__":
    app.run(port="5000", debug=True, threaded=True)