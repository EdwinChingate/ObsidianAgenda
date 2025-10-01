from datetime import datetime
def date_formatting(date_str):
    format_string="%Y-%m-%d"
    dt_obj=datetime.strptime(date_str,format_string)
    return dt_obj
