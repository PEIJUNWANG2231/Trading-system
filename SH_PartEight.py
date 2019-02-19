# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:54:59 2019

@author: XPS15
"""
import sys
sys.path.append(r'D:\Python Codes Lib\SH_Alligator trading system')
from SH_PartTwoAveragerGluing import AveragerGluing
from SH_PartSevenResult import IterAveragerGluing
from SH_PartFourMatchUpFractals import MatchUpFractals
from SH_PartFiveMatchDownFractals import MatchDownFractals
from SH_PartSixEnterAndLossPoint import EnterPoint,StopLossPoint
import pandas as pd
import datetime

#遍历所有的股票，输出到一张excel中
def DataFrame(code):
    m=str(code)
    df=pd.read_csv('D:/Python Codes Lib/SH_Data Base/'+m+'.SH.csv')
    
    list1=AveragerGluing(df)
    
    m=['Unnamed: 0', 'trade_date', 'open', 'high', 'low', 'close', 'Var1',
       'jaw', 'teeth', 'lips', '5&8', '8&13', 'compare', 'daily_pct']
    
    df1=pd.DataFrame(columns = m)
    
    list2=IterAveragerGluing(df)
    
    li1=MatchUpFractals(df,list1)
    
    li2=MatchDownFractals(df,list1)
    
    dict1=EnterPoint(df)
    
    dict2=StopLossPoint(df)
    
    for i in range(len(list1)):
        df2=df.iloc[list1[i]:list1[i]+1,:]
        df2['result']=list2[i]
        df2['code']=code
        df2['StopLoss']=dict2[li2[i]]
        df2['Enter']=dict1[li1[i]]
        df2['StopLossPct']=(dict1[li1[i]]-dict2[li2[i]])/dict1[li1[i]]
        frames=[df1,df2]
        df1=pd.concat(frames)

    return df1

def set():
    list=[]
    for i in range(600000,604000):
        try:
            df=DataFrame(i)
            list.append(df)
        except:
            FileNotFoundError
    df1=pd.concat(list)
    df1.to_csv('D:/Python Codes Lib/1.csv')
    return df1

def main():
    start = datetime.datetime.now()
    set()
    df1=pd.read_csv('D:/Python Codes Lib/1.csv')
    
    df1=df1[~df1['result'].str.contains('no enter')]
    df1=df1[~df1['result'].str.contains('no result')]
    
     
    df2=df1[~df1['result'].str.contains('stop loss')]
    
    SR=len(df2)/len(df1)
    
    print('sussecc rate is %2f' %SR)
    df1.to_csv('D:/Python Codes Lib/1.csv')
    end = datetime.datetime.now()
    print(end-start)
    return SR

if __name__ == '__main__':
    main()




