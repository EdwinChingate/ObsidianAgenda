import pandas as pd
def Day_of_the_week(year,month,day):
    Months=pd.read_csv('Months.csv',index_col=0)
    WeekDays=pd.read_csv('WeekDays.csv',index_col=0)
    MonthCode=Months['Key'][month]
    CenturyCode=6
    YearCode=(year+year/4)%7
    DAY=int((YearCode+MonthCode+CenturyCode+day-1)%7)
    DayString=WeekDays['Day'][DAY]
    return DayString
