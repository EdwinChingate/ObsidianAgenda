import os
import numpy as np
from date_formatting import *
from DatesVecGen import *
from Write_DF_as_markdownTable import *
def Slice_DF_by_date_and_write(MessagesDF,
                               MessagedFolderDestination='',
                               startYear=2019,
                               endYear=2030,
                               join='|',
                               endLine='\n'):
    if len(MessagedFolderDestination)==0:
        MessagedFolderDestination=os.getcwd()
    Record_datesVec=np.array(list(map(date_formatting,MessagesDF['Date'])))
    DatesVec=DatesVecGen(startYear=startYear,
                         endYear=endYear)  
    Ndate=len(DatesVec)
    start_date=DatesVec[0]
    for date_id in np.arange(1,Ndate):
        #This whole block can become a function
        end_date=DatesVec[date_id]
        DatesLoc=(Record_datesVec>start_date)&(Record_datesVec<end_date)    
        Month_MessagesDF=MessagesDF[DatesLoc]
        Nmessages=len(Month_MessagesDF)
        if Nmessages>0:
            SavedMessage=MessagedFolderDestination+'/'+str(start_date)[:7]+'-'+str(Nmessages)+'.md'
            Write_DF_as_markdownTable(MessagesDF=Month_MessagesDF,
                                      SavedMessage=SavedMessage,
                                      join=join,
                                      endLine=endLine)
        start_date=end_date
