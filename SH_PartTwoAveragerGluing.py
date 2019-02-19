# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:34:26 2018

@author: XPS15
"""

from interval import Interval
import pandas as pd
import datetime
import numpy as np
# example: 5&8均线粘合
#para: dataframe,target:5&8,8&13,daily_pct:实体大小,

#when change target, 实体镶嵌也要修改
def AveragerGluing(df,target=10,daily_pct=0.015):
    #将dataframe拆开，拆成list操作
    df1=np.array(df)

    li=df1.tolist()
    
    #target represent 5&8, 8&13
    #5&8:10，8&13:11,compare:12
    list1=[]
    for i in range(0,len(li)-2):
        if li[i][target]<=li[i][12]:
            if li[i+1][target]<=li[i+1][12]:
                if li[i+2][target]<=li[i+2][12]:
                    list1.append(i)
                        
    #open:2，close:5,jaw:7,teeth:8
    #5&8 对应的实体镶嵌则是镶嵌在jaw：7 & teeth：8 上
    #8&13 对应的实体镶嵌则是在 teeth：8 & lips：9 上
    list2=[]
    for i in list1:
        s=0
        k=[li[i+s][2],li[i+s][5]]
        m=Interval(min(k),max(k))
        if li[i+s][7] in m:
            list2.append(i)

        if li[i+s][8] in m:
            list2.append(i)
    
    #daily_pct:13
    list3=[]
    for i in list2:
        if li[i][13]<=daily_pct:
            list3.append(i)

    list3=list(set(list3))
    list3.sort()
    return list3

def main(code):
    start = datetime.datetime.now()
    m=str(code)
    df=pd.read_csv('D:/Python Codes Lib/SH_Data Base/'+m+'.SH.csv')
    list=AveragerGluing(df)
    print(list)
    end = datetime.datetime.now()
    print(end-start)
    return list

if __name__ == '__main__':
    main(600116)


