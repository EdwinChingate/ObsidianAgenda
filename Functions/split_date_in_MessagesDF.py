import pandas as pd
import numpy as np
from SplitDate_Hour import *
from SplitYear_Month_Day import *
from SplitHour_Minute_Second import *
def split_date_in_MessagesDF(MessagesDF):
    DatesList=list(MessagesDF['Full date'])
    indexCol=list(MessagesDF.index).copy()
    Date_HourList=list(map(SplitDate_Hour,DatesList))
    Date_HourArray=np.array(Date_HourList)
    Year_Month_Day_List=list(map(SplitYear_Month_Day,Date_HourArray[:,0]))
    Hour_Minute_Second_List=list(map(SplitHour_Minute_Second,Date_HourArray[:,1]))
    Year_Month_Day_DF=pd.DataFrame(Year_Month_Day_List,columns=["Year","Month","Day"],index=indexCol)
    Date_DF=pd.DataFrame(Date_HourArray[:,0],columns=["Date"],index=indexCol)
    Hour_Minute_Second_DF=pd.DataFrame(Hour_Minute_Second_List,columns=["Hour","Minute","Second"],index=indexCol)
    MessagesDF=pd.concat([MessagesDF,Date_DF,Year_Month_Day_DF,Hour_Minute_Second_DF], axis=1)
    N_columns=len(MessagesDF.columns)
    BorderTable=pd.DataFrame(np.array(N_columns*['--------']).reshape(1,-1),columns=MessagesDF.columns,index=['---'])
    MessagesDF=pd.concat([BorderTable,MessagesDF], ignore_index=False)
    return MessagesDF
