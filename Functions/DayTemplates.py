import os
import pandas as pd
import numpy as np
from DatesStr import *
from Day_of_the_week import *
def DayTemplates(Year,Month,TemplatesFolder='DayTemplates'):
    home=os.getcwd()
    Months=pd.read_csv('Months.csv',index_col=0)
    MaxDay=Months['D'][Month]    
    monthString=Months['Name'][Month]
    FullSource=home+'/'+TemplatesFolder    
    source_dir = "/path/to/source/folder"
    destination_dir = "/path/to/destination/folder"
    prefix = "prepend-"  # Define the prefix you want to add
    # Use os.system to run the shell command    
    command1="cp ./Files/Events.md ./"
    command2="cp ./Files/Finances.md ./"
    command3="cp ./Files/Thoughts_and_Observations.md ./"
    os.mkdir(monthString)
    for Day in np.arange(MaxDay+1):
        DateString=DatesStr(Year,Month,Day)
        FolderLoc=monthString+'/'+DateString
        DateString_=DateString+'-'
        FileLoc=FolderLoc+'/Events.md'
        FileLoc2=FolderLoc+'/Finances.md'
        FileLoc3=FolderLoc+'/Thoughts_and_Observations.md'
       # command=command0+FolderLoc
        command1_=command1+FileLoc
        command2_=command2+FileLoc2
        command3_=command3+FileLoc3
        #print(command)
        day=Day_of_the_week(Year,Month,Day)
        #print(day)
        #os.system(command) 
        FullDestination=home+'/'+monthString+'/'+DateString
        os.mkdir(FullDestination)
        os.system(f'''cd "{FullSource}" && find . -type f -exec sh -c 'mkdir -p "{FullDestination}/$(dirname "$0")" && cp "$0" "{FullDestination}/$(dirname "$0")/{DateString_}$(basename "$0")"' {{}} \;''')
        TemplatesFolder=FolderLoc
        activity1=DateString
        original1='~~~~'
        activity2='day: '+day
        original2='day:'
        RewriteSameInFoldersInside(TemplatesFolder,activity1,original1,activity2,original2)
        os.system(command1_)
        os.system(command2_)
        os.system(command3_)
        RewriteFile(Folder=FolderLoc,original=original1,new=DateString,file='Events.md')
        RewriteFile(Folder=FolderLoc,original=original2,new=activity2,file='Events.md')
        RewriteFile(Folder=FolderLoc,original=original1,new=DateString,file='Finances.md')
        RewriteFile(Folder=FolderLoc,original=original2,new=activity2,file='Finances.md')
        RewriteFile(Folder=FolderLoc,original=original1,new=DateString,file='Thoughts_and_Observations.md')
        RewriteFile(Folder=FolderLoc,original=original2,new=activity2,file='Thoughts_and_Observations.md')        
