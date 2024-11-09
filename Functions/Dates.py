import numpy as np
import pandas as pd
def Dates(year,month,day,loc=0,Months='',Days=''):
    if loc==0:
        Days=np.zeros((7,3))
        day=day-3
        Months=pd.read_csv('Months.csv',index_col=0)
    MaxDay=Months['D'][month]
    if day>MaxDay:
        day=day-MaxDay
        month+=1
    if month==13:
        month=1 
        year+=1
    if day<1:
        MaxDay=Months['D'][month-1]
        day=MaxDay+day
        month-=1
        Days[loc,0]=year
        Days[loc,1]=month
        Days[loc,2]=day
        loc+=1    
        day+=1
        Days=Dates(year,month,day,loc,Months,Days)
    elif loc<7:
        Days[loc,0]=year
        Days[loc,1]=month
        Days[loc,2]=day
        loc+=1    
        day+=1
        Days=Dates(year,month,day,loc,Months,Days)
    return Days
