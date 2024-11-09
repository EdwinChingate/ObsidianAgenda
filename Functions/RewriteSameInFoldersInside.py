import os
from RewriteAllFilesinFolder import *
def RewriteSameInFoldersInside(TemplatesFolder,activity1='',original1="activityID",activity2='',original2="activityID"):
    for folderName in os.listdir(TemplatesFolder):
        folder=TemplatesFolder+'/'+folderName
        RewriteAllFilesinFolder(folder,original=original1,activity=activity1)
        RewriteAllFilesinFolder(folder,original=original2,activity=activity2)
