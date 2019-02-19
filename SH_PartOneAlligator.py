# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:13:16 2018

@author: XPS15
"""

import tushare as ts
import datetime
import numpy as np

def today():
    today=datetime.date.today()
    return today
    
#读取对应数据，重新组合
def his_data(code,start='19960101',end='today()'):
    pro = ts.pro_api()
    df= pro.daily(ts_code=code, start_date=start, end_date=end)
    df=df.iloc[:,1:6].sort_index(ascending=False).reset_index(drop=True)
    df['Var1']=(df['high']+df['low'])/2
    return df

#SMA数组的获取，作为鳄鱼线的基础
def SMA(close,n,m=1):
    result = np.array([np.nan]*len(close))
    result[n-2]=close[:n-1].mean()
    for i in range(n-1,len(close)):
        result[i]=(m*close[i]+(n-m)*result[i-1])/n
    return result

#对数据组的基础处理：   
def Alligator(df,n=1):
    average=[5,8,13] #fibonacci squence:5,8,13 
    moves=[3,5,8]
    names=['jaw','teeth','lips']
    #生成3条对应的均线
    for i in range(3):
        df[names[i]]=SMA(df['Var1'],average[i])
        df[names[i]]=df[names[i]].shift(periods=moves[i])
    
    df['5&8']=df['jaw']-df['teeth']
    df['8&13']=df['teeth']-df['lips']
    df['5&8']=abs(df['5&8'])
    df['8&13']=abs(df['8&13'])
    #均线粘合的差值由close来决定
    df['compare']=((df['close']/10).astype(int)+n)*0.01
    df['daily_pct']=abs(df['open']-df['close'])/df['close']
    df=df.dropna().reset_index(drop=True)
    return df

def main(code):
    df=his_data(code,start='19960101',end='today()')
    df=Alligator(df)
    m='D:\\Python Codes Lib\\Data Base'
    n=code
    
    df.to_csv(m+'\\'+n+'.csv')
    return df

if __name__ == '__main__':
    for i in range(600000,604000,1):
        try:
            m=str(i)
            main(m+'.SH')
        except:
            IndexError

