import pandas as pd
def ConcatenateTasksDFs(FirstFile,Tasks_DF,DF):
    if FirstFile:
        Tasks_DF=DF[2:]
        FirstFile=False
    else:
        Tasks_DF=pd.concat([Tasks_DF,DF[2:]],
                           ignore_index=True)    
    return FirstFile,Tasks_DF
