def DatesStr(Year,Month,Day):
    year=str(Year)
    month=str(Month)
    day=str(Day)
    if len(day)==1:
        day='0'+day
    if len(month)==1:
        month='0'+month
    date=year+'-'+month+'-'+day
    return date
