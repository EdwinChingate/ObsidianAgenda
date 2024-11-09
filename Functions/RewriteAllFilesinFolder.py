from SearchActivity import *
import os
def RewriteAllFilesinFolder(folder,activity='',original="activityID"):
    if activity=='':
        ReplaceActivity=True
    else:
        ReplaceActivity=False
    for file in os.listdir(folder):
        File=folder+'/'+file
        if file[-2:]=='md':
            if ReplaceActivity:
                activity=SearchActivity(File)
            commandStart="sed -i 's/"
            commandMiddle="/"   
            commandEnd="/g' "
            command=commandStart+original+commandMiddle+activity+commandEnd+File
            os.system(command)
        else:
            insideFolder=folder+'/'+file
            RewriteAllFilesinFolder(insideFolder,original=original,activity=activity)           
