
# coding: utf-8

# ## Analysis with Display

# In[1]:

import pandas as pd
import numpy as np
import requests
from keras.models import load_model
from keras.preprocessing import image
import pymysql as sql
from selenium import webdriver
from PIL import Image
import os
import re


# In[2]:

df=pd.read_csv('hist_data.csv', encoding="cp1252")
model = load_model('nsfw.h5')
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
os.system('cls')


# In[3]:

def rateurl(i):
            BASE = 'https://render-tron.appspot.com/screenshot/'
            path = 'target.jpg'
            response = requests.get(BASE + i, stream=True)
            
            return response.status_code 

        
def selfie(url):
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    valid=re.match(regex,url) is not None
    driver.get(url)
    screenshot = driver.save_screenshot('target.png')
    driver.quit()
    im = Image.open("target.png")
    rgb_im = im.convert('RGB')
    rgb_im.save('colors.jpg')


# In[4]:

def statuscheck(url):
    c=sql.connect(host="localhost",user="root",password="",db="urls")
    connection=c.cursor()
    command="SELECT status FROM urls.url_status where name='"+ url +"';"
    connection.execute(command)
    retrived=connection.fetchall()
    return retrived

def urlinsert(url):
    c=sql.connect(host="localhost",user="root",password="",db="urls")
    connection=c.cursor()
    status=rateurl(url)
    if len(url) > 255:
        print(url)
    command="insert into urls.url_status values('" +url+ "','" +status+ "');"
    connection.execute(command)
    return status


# In[5]:

def sync(url):
    status=statuscheck(url)
    if len(status)!=0:
        return status
    else:
        return urlinsert(url)


# In[6]:

def result(url):
    status=str(url)
    status=status.split()
    status=status[0]
    status=sync(status)
    if type(status)==str:
        return status
    if type(status)==tuple:
        return status[0][0]


# In[7]:

for i in range(100):
    print(i,result(df.iloc[[i],[0]].values[0][0]))




# In[ ]:

dataframe=pd.DataFrame(urlscan)
dataframe

