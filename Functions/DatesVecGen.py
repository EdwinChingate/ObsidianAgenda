import pandas as pd
import numpy as np
from int_2_str import *
from date_formatting import *
def DatesVecGen(startYear=2019,
                endYear=2030):
    N_years=endYear-startYear
    yearsList=[]
    monthsList=[]
    List_of_Months=list(map(int_2_str,np.arange(1,13)))
    monthsList=N_years*List_of_Months
    daysArray=12*N_years*['1']
    for year in np.arange(startYear,endYear):
        yearsList+=12*[str(year)]
    DatesDF=pd.DataFrame([yearsList,monthsList,daysArray]).T
    DatesDF['Date string']=DatesDF[0]+'-'+DatesDF[1]+'-'+DatesDF[2]
    DatesVec=list(map(date_formatting,DatesDF['Date string']))
    return DatesVec
