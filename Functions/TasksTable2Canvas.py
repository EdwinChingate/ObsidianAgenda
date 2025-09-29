from SquareCardsCanvas import *
from AllCardsFromTables import *
from TasksExtraction import *
import datetime
from pathlib import Path
import json
import numpy as np
def TasksTable2Canvas(TasksFolder,
                      card_width=500,
                      card_height=120,
                      padding=140,
                      color='#4169E1'):
    CleanTextList=TasksExtraction(TasksFolder=TasksFolder)
    N_tasks=len(CleanTextList)
    SquereSide=int(np.sqrt(N_tasks))
    task_count=0
    nodes_json=[] 
    for task in CleanTextList:        
        nodes_json,task_count=AllCardsFromTables(task_count=task_count,
                                                 task=task,
                                                 SquereSide=SquereSide,
                                                 nodes_json=nodes_json,
                                                 card_width=card_width,
                                                 card_height=card_height,
                                                 padding=padding,
                                                 color=color)
    data = {"nodes": nodes_json, "edges": []}
    Time=datetime.datetime.now()
    Date=str(Time.date())
    routeTasksCanvas=TasksFolder+'/'+Date+'.canvas'    
    Path(routeTasksCanvas).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")        
