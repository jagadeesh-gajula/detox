
# coding: utf-8

# ## This code will generate CSV file containing history data

# In[156]:

#Good code is its own documentation
#importing all the librarires needed 
import browserhistory as bh
import pandas as pd
import numpy as np


# In[160]:

# This method maps url into clean home urls 
def mapinto(link):
    link=str(link)
    linklen=len(link)
    begin=link.find('h',0,linklen)
    end=link.find('/',begin+10,linklen)
    homeurl=link[begin:end]
    return homeurl

# this cleanses date and time for dataset
timer=[]
def datecleaner(value):
    value=str(value)
    value=value.split()
    timer.append(value)
    return 

#this is the root function of all calling this function will genarate the dataset
def developdata(df):
    links=df.iloc[:,[0]].apply(mapinto,axis=1)
    df=pd.concat([links,df],axis=1)
    x=df.iloc[:,[3]].apply(datecleaner,axis=1)
    del(x,links)
    datentime=pd.DataFrame(timer)
    datentime=datentime.iloc[:,[1,2]]
    datentime.shape
    df=pd.concat([df,datentime],axis=1)
    df=df.fillna(value=np.nan)
    df=df.drop(['url specific','datentime'],axis=1)
    df.columns=['home_urls','desc','date','time']
    return df

# this is main function intiatiates process and exports data
def initdetox(history):
    keys=history.keys()
    browsercount=0
    for key in keys:
        df=pd.DataFrame(history[key],columns={'url specific','description','datentime'})
        if browsercount==0:
            dataset=developdata(df)
        else:
            data=developdata(df)
            dataset=pd.concat([dataset,data],axis=0)
        browsercount+=1
    dataset=dataset[dataset.home_urls.notnull()]   
    return dataset

history=bh.get_browserhistory()
gen=initdetox(history)


# In[163]:

#throws back dataset
gen.to_csv('hist_data.csv')

