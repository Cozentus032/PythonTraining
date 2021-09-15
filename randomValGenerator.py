# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:52:56 2021

@author: debashish
"""
import pandas as pd
import numpy as np
import requests
import json
import random

salutation,firstName,lastName,gender,dOb,Age,street_No,street_Name,city_Name,state_Name,country_Name,postCode,time_Zone,area,email,username,password = [[]for j in range(17)]
#column_names=["salutation","firstName","lastName","gender","dOb","Age","street_No","street_Name","city_Name","state_Name","country_Name","postCode","time_Zone","area","email","username","password"]


for i in range(5000):
    response = requests.get('https://randomuser.me/api/')
    data=json.loads(response.content)
    #json_format = '{"results":[{"gender":"male","name":{"title":"Mr","first":"Liam","last":"Ree"},"location":{"street":{"number":2935,"name":"Skjellveien"},"city":"Risør","state":"Telemark","country":"Norway","postcode":"7657","coordinates":{"latitude":"54.1097","longitude":"-68.9046"},"timezone":{"offset":"+9:00","description":"Tokyo, Seoul, Osaka, Sapporo, Yakutsk"}},"email":"liam.ree@example.com","login":{"uuid":"8ad4cac1-a632-47d6-a9f6-950889d15d17","username":"yellowkoala660","password":"moose","salt":"PxoiD1Aj","md5":"076609cab1e0e41b38ae29ef4dec81d7","sha1":"22edaa2cae5081b24ebe4a1334e15c93ccb5ff61","sha256":"e21037cd2b448dd29d0a2c6fc4c3152c1ed4a513af7380e59ae71b394cce9523"},"dob":{"date":"1961-08-03T23:00:34.450Z","age":60},"registered":{"date":"2002-09-06T08:20:29.087Z","age":19},"phone":"65813804","cell":"97173847","id":{"name":"FN","value":"03086112182"},"picture":{"large":"https://randomuser.me/api/portraits/men/55.jpg","medium":"https://randomuser.me/api/portraits/med/men/55.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/55.jpg"},"nat":"NO"}],"info":{"seed":"ce01d1d818009f5d","results":1,"page":1,"version":"1.3"}}'
    # data = json.loads(json_format)
    data_list = data['results'][0]
    salutation.append(data_list['name']['title'])
    firstName.append(data_list['name']['first'])
    lastName.append(data_list['name']['last'])
    gender.append(data_list['gender'])
    street_No.append(data_list['location']['street']['number'])
    street_Name.append(data_list['location']['street']['name'])
    city_Name.append(data_list['location']['city'])
    state_Name.append(data_list['location']['state'])
    country_Name.append(data_list['location']['country'])
    postCode.append(data_list['location']['postcode'])
    time_Zone.append(data_list['location']['timezone']['offset'])
    dOb.append(data_list['dob']['date'])
    Age.append(data_list['dob']['age'])
    area.append(data_list['location']['country'])
    email.append(data_list['email'])
    username.append(data_list['login']['username'])
    password.append(data_list['login']['password'])
    
dfdata = pd.DataFrame({"salutation":salutation,"firstName":firstName,"lastName":lastName,"gender":gender,"dOb":dOb,"Age":Age,"street_No":street_No,"street_Name":street_Name,"city_Name":city_Name,"state_Name":state_Name,"country_Name":country_Name,"postCode":postCode,"time_Zone":time_Zone,"area":area,"email":email,"username":username,"password":password})
print(dfdata)

Weight = []
p=[]
sal=[]
sum=0
Profession = ['Software Engineer', 'Teacher', 'Driver', 'Actor', 'Investment Banker', 'Entrepreneur', 'Doctor', 'Writer',
'Chef', 'Student', 'Scientist', 'Palaeontologist']
for i in range(5000):
    n = random.randint(30,90)
    Weight.append(n)
    p.append(random.choice(Profession))
    s= random.randint(30000,90000)
    sum=s+sum
    sal.append(s)
    
#adding new column weight
dfdata['Weight'] = Weight

#adding new column profession
dfdata['Profession']= p

#adding new column salary
dfdata['Salary'] = sal

#adding new column Average salary
avg=sum/5000
dfdata['Average Salary']= avg
    
#dfData = pd.DataFrame(final)
print(dfdata)

dfdata.to_excel(r"Compiled5kdata.xlsx")
