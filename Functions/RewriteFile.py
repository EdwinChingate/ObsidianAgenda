import os
def RewriteFile(Folder,original,new,file='Events.md'):
    File=Folder+'/'+file
    commandStart="sed -i 's/"
    commandMiddle="/"   
    commandEnd="/g' "
    command=commandStart+original+commandMiddle+new+commandEnd+File
    os.system(command)    
