# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:33:20 2018

@author: XPS15
"""
import datetime
import pandas as pd
import numpy as np
def UpFractal(df):
#2.1 上分型 
    df1=np.array(df)
    li=df1.tolist()
    
    list1=[]
    #high:3
    for i in range(2, len(li)-2):
        if li[i-2][3]<li[i][3]:
            if li[i-1][3]<li[i][3]:
                if li[i+1][3]<li[i][3]:
                    if li[i+2][3]<li[i][3]:
                        list1.append(i)

    dict={}
    for i in list1:
        dict[i]=li[i][3]
    return dict
    

def DownFractal(df):
##2.2 下分型                    
    list2=[]
    df1=np.array(df)
    li=df1.tolist()
    
    #low:4
    for i in range(2, len(li)-2):
        if li[i-2][4]>li[i][4]:
            if li[i-1][4]>li[i][4]:
                if li[i+1][4]>li[i][4]:
                    if li[i+2][4]>li[i][4]:
                        list2.append(i)
    dict={}
    for i in list2:
        dict[i]=li[i][4]
    return dict

def main(code):
    start = datetime.datetime.now()
    m=str(code)
    df=pd.read_csv('D:/Python Codes Lib/SH_Data Base/'+m+'.SH.csv')
    UpFractal(df)
    DownFractal(df)
    end = datetime.datetime.now()
    print(end-start)
    

