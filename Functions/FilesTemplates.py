import os
import pandas as pd
import numpy as np
from DatesStr import *
from Day_of_the_week import *
from RewriteSameInFoldersInside import *
from RewriteFile import *
def FilesTemplates(Year,Month,FilesFolder='Files',FileName='Events',FinalDest=''):
    home=os.getcwd()
    Months=pd.read_csv('Months.csv',index_col=0)
    MaxDay=Months['D'][Month]    
    monthString=Months['Name'][Month]
    command0="cp ./"+FilesFolder+'/'+FileName+".md ./"
    if not os.path.exists(monthString):
        os.mkdir(monthString)
    if FinalDest!='':
        ListFileLoc=monthString+'/'+FileName+'.md'
        ListFile=open(ListFileLoc,'w')
        ListFile.write('## '+monthString+'\n')
        ListFile.close()
    FolderLoc=monthString+'/'+FileName
    os.mkdir(FolderLoc)
    for Day in np.arange(1,MaxDay+1):
        DateString=DatesStr(Year,Month,Day)        
        DateString_=DateString+'-'
        FullFileName=DateString_+FileName+'.md'
        FileLoc=FolderLoc+'/'+FullFileName
        WritenName='- [['+FinalDest+'/'+str(Year)+'/'+monthString+'/'+FullFileName+'|'+FullFileName+']]\n'
        command=command0+FileLoc    
        day=Day_of_the_week(Year,Month,Day)
        TemplatesFolder=FolderLoc
        activity1=DateString
        original1='~~~~'
        activity2='day: '+day
        original2='day:'
        os.system(command)
        RewriteFile(Folder=FolderLoc,original=original1,new=DateString,file=FullFileName)
        RewriteFile(Folder=FolderLoc,original=original2,new=activity2,file=FullFileName)
        if FinalDest!='':
            ListFile=open(ListFileLoc,'a')
            ListFile.write(WritenName)
            ListFile.close()
