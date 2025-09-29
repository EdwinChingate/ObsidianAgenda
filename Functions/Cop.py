import os
import shutil
def Cop(old,new): #Coppy files from an old rute to a newone
    #old: full name of the file with the current directory
    #new: new name for the file with the directory wanted
    origen=old
    destino=new
    if os.path.exists(origen):
        with open(origen, 'rb') as forigen:
            with open(destino, 'wb') as fdestino:
                shutil.copyfileobj(forigen, fdestino)
