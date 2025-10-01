import pandas as pd
def AgendaGen(startYear=2019,
              endYear=2030):
    DatesVec=DatesVecGen(startYear=startYear,
                         endYear=endYear)
    AgendaDF=pd.DataFrame()
    AgendaDF['start']=DatesVec[:-1]
    AgendaDF['end']=DatesVec[1:]    
    return AgendaDF
