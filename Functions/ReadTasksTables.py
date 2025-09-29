import pandas as pd
from ConcatenateTasksDFs import *
def ReadTasksTables(task_file,TasksFolder,FirstFile,Tasks_DF):
    if task_file[-2:]!='md':
        return FirstFile,Tasks_DF
    TaskFile=TasksFolder+'/'+task_file
    DF=pd.read_csv(TaskFile,
                   sep='|',
                   usecols=[1,2,3],
                   names=["Time","Comment","Keywords"])  
    FirstFile,Tasks_DF=ConcatenateTasksDFs(FirstFile=FirstFile,
                                           Tasks_DF=Tasks_DF,
                                           DF=DF)
    return FirstFile,Tasks_DF
