# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:42:12 2019

@author: XPS15
"""

import pandas as pd
import numpy as np
import datetime

def CalculateDay(m):
    m=str(m)
    df=pd.read_csv('D:/Python Codes Lib/'+m+'.csv')

    df=df[~df['result'].str.contains('stop loss')]

    df1=np.array(df)
    li3=df1.tolist()

    k=0
    for i in range(len(li3)):
        m=str(li3[i][-1])
        year1=int(m[0:4])
        month1=int(m[4:6])
        day1=int(m[6:8])
    
        d1 = datetime.datetime(year1,month1,day1)
    
        n=li3[i][-3]
        year2=int(n[0:4])
        month2=int(n[4:6])
        day2=int(n[6:8])
    
        d2 = datetime.datetime(year2,month2,day2)
    
        m=d2-d1
    
        k=k+m.days

    k=k/len(li3)
    return k


    


