import numpy as np
import pandas as pd
from load_canvas import *
from split_date_in_MessagesDF import *
def extract_messages_as_DF(FileName):
    FileDict=load_canvas(path_or_dict=FileName)
    MessagesList=[]
    FileList=FileDict["messages"]
    for n in FileList:
        nid = n.get("id")
        CellType=str(n.get("type"))
        if CellType=="message":
            text=str(n.get("text")).replace('\n',' ')
            MessagesList.append({"id": nid,
                                 "Full date":n.get("date"), 
                                 "Text":text,
                                 "Use":'',
                                 "Unixtime":n.get("date_unixtime")})
    MessagesDF=pd.DataFrame(MessagesList)
    MessagesDF.set_index("id", inplace=True)    
    MessagesDF=split_date_in_MessagesDF(MessagesDF=MessagesDF)
    return MessagesDF

