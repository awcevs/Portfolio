# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:15:14 2023

@author: 407-16
"""

from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
from pprint import pprint
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pymysql
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# DB 음식정보 select =========================
def GetFood(result, foodnum = None, limit = None, orderby = None):
    
    db = 1    
    
    if db == 0 :
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='ezen',
                             database='food',
                             cursorclass=pymysql.cursors.DictCursor)
    elif db == 1 :
        db = pymysql.connect(host='192.168.0.112',
                             user='ezen',
                             password='ezen',
                             database='food',
                             cursorclass=pymysql.cursors.DictCursor)
    run = db.cursor()
    
    # SQL query 작성
    sql  = "select * from food "
    sql += "where weather_menu = '" + result + "' "
    
    # 해당 음식 데이터만 select
    if foodnum != None :
        sql += "and foodnum = '" + foodnum + "' "
    
    # select 데이터 갯수 제한
    if limit != None :
        sql += "limit 0, " + limit
        
    # 데이터 정렬
    if orderby != None :
        sql += "order by " + orderby + " "
    
    # SQL query 실행
    run.execute(sql)
    
    # SQL query 실행 결과를 가져옴
    food = run.fetchall()
    db.close()
    return food

# 네이버 날씨 정보 크롤링 =========================
def GetWeather():
    html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8')
    #html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
    #pprint(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class': 'inner'})
    find_address = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.top_wrap > div.title_area._area_panel > h2.title')
    print('현재 위치: ' + find_address.get_text())
    find_currenttemp = data1.find('div',{'class': 'temperature_text'}).text
    print('현재 온도: ' + find_currenttemp)
    data2 = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div.report_card_wrap > ul > li:nth-child(1) > a > span')
    find_dust = data2.text
    weather = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > p > span.weather.before_slash')
    weather = weather.text
    #find_ultra_dust = data2[1].find('span', {'class':'num'}).text
    #find_ozone = data2[2].find('span', {'class':'num'}).text
    print('현재 미세먼지: ' + find_dust)
    print('현재 날씨: ' + weather)
    #print('현재 초미세먼지: '+find_ultra_dust)
    #print('현재 오존지수: '+find_ozone)
    weather_info = [find_currenttemp.replace("현재 온도", ""), weather]
    
    # 기온, 날씨
    degree  = weather_info[0]
    weather = weather_info[1]
    
    # 날씨 판단
    result = "normal"
    temp = float(weather_info[0].replace("°",""))
    
    if temp > 25 :
        result = "hot"
    elif temp < 10 :
        result = "cold"
    
    if  "눈" in weather_info[1] and "비" in weather_info[1] :
        result = "rainsnow"
    elif "비" in weather_info[1] :
        result = "rain"
    elif weather_info[1] == "소나기" :
        result = "rain"
    elif "눈" in weather_info[1] :
        result = "snow"
    
    return degree, weather, result

# 선택한 음식 기반으로 추천
def Recommend(weather, foodnum):
    
    foodSelect = GetFood(weather, foodnum)
    
    rc_food = GetFood(weather)
    rc_food = pd.DataFrame(rc_food)
    
    # 카운터 벡터라이즈 훈련
    cv = CountVectorizer(ngram_range=(1,3)) 
    cv_category = cv.fit_transform(rc_food['food_category'])
    similarity_category = cosine_similarity(cv_category, cv_category).argsort()[:,::-1]
    
    def recommend_menu(df, menu_name):
        target_menu_idx = df[df['foodname'] == menu_name].index.values
    
        sim_idx = similarity_category[target_menu_idx].reshape(-1)
        sim_idx = sim_idx[sim_idx != target_menu_idx]
    
        result = df.iloc[sim_idx]
        return result
    
    recommend = recommend_menu(rc_food, foodSelect[0]['foodname']).head(10)
    recommend = recommend.to_json(orient='records')
    return recommend

@app.route('/', methods=['GET','POST'])
def GetData():
    
    # 날씨 정보(기온, 날씨, 판단)
    degree, weather, result = GetWeather()
    # 음식 정보(DB에서 result 날씨로 select)
    food = GetFood(result)
    
    # rows = html의 tr 갯수 (tr 당 음식 5개)
    count = len(food)
    rows = (count // 5) + 1
    if (count % 5) == 0 :
        rows = rows - 1
        
    return render_template('index.html', 
                           degree = degree,
                           weather = weather,
                           result = result,
                           food = food,
                           rows = rows
                           )

@app.route('/ajax', methods=['GET','POST'])
def ajax():
    # select에서 선택한 날씨로 갱신 ====================
    
    jsonData = request.get_json("data")
    todo = jsonData['todo']
    weatherSelect = jsonData['weatherSelect']

    data = GetFood(weatherSelect)
    if todo == "orderby" :
        orderby = jsonData['orderby']
        data = GetFood(weatherSelect, orderby = orderby)
    
    return jsonify(data)

@app.route('/result/<weather>/<foodnum>', methods=['GET','POST'])
def result(weather, foodnum):
    
    foodSelect = GetFood(weather, foodnum)
    foodSelect = foodSelect[0]
    #foodSelect = jsonify(foodSelect)
    #foodSelect = json.dumps(foodSelect)
    #foodSelect = app.response_class(response=json.dumps(foodSelect),mimetype='application/json')
    # 추천 함수 
    foodRec = Recommend(weather, foodnum)
    
    foodWeather = GetFood(weather, limit='5')
    
    return render_template('result.html', 
                           foodnum = foodnum, 
                           weather = weather,
                           foodSelect = foodSelect,
                           foodRec = foodRec,
                           foodWeather = foodWeather)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)