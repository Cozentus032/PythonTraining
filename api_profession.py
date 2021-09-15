import json
import pandas as pd
import random
import requests
salutation,firstName,lastName,gender,dOb,Age,street_No,street_Name,city_Name,state_Name,country_Name,postCode,time_Zone,area,email,username,password = [[]for j in range(17)]
column_names = ["salutation","firstName","lastName","gender","Age","street_No","Street_Name","Country_Name","City_Name","stateName","postCode","time_Zone","dOb","Area","E-mail","Username","password"]
for i in range(5000):
    fetch = requests.get("https://randomuser.me/api/")
    data = json.loads(fetch.content)
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
df = (pd.DataFrame([salutation, firstName,lastName,gender,street_No,street_Name,city_Name,state_Name,country_Name,postCode,time_Zone,dOb,Age,area,email,username,password],column_names)).T
print(df)
weight = []
proff1=[]
salary=[]
proff = ['Software Engineer','Teacher','Driver','Actor','Investment_Banker','Doctor','Writer','Chef','Student','Scientist','Palaeontologist']
for j in range(5000):
    weight.append(random.randint(27,110))
    proff1.append(random.choice(proff))
for k in range(5000):
    if(proff1[k] != "Student"):
        salary.append(random.randint(200000,1200000))
    else:
        salary.append(0)
df['Weight'] = weight
df['Profession'] = proff1
df['Salary'] = salary
df["avg_salary"] = df.groupby("Profession")["Salary"].transform("mean")
print(df)
df.to_excel('Records5000.xlsx',index = None)