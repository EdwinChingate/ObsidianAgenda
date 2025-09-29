import os
from ReadTasksTables import *
from CleanText import *
def TasksExtraction(TasksFolder):
    TasksList=os.listdir(TasksFolder)
    TasksList.sort()
    FirstFile=True
    Tasks_DF=[]
    for task_file in TasksList:    
        FirstFile,Tasks_DF=ReadTasksTables(task_file=task_file,
                                           TasksFolder=TasksFolder,
                                           FirstFile=FirstFile,
                                           Tasks_DF=Tasks_DF)
    CommentsList=(list(Tasks_DF['Comment']))
    CleanTextList=list(map(CleanText,CommentsList))
    return CleanTextList
