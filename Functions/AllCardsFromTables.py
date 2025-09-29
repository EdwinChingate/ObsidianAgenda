from SquareCardsCanvas import *
def AllCardsFromTables(task_count,task,SquereSide,nodes_json,
                       card_width=500,
                       card_height=120,
                       padding=70,
                       color='#4169E1'):
    if len(task)==0:
        return nodes_json,task_count
    x,y,row,task_count=SquareCardsCanvas(task_count=task_count,
                                         SquereSide=SquereSide,
                                         card_width=card_width, 
                                         card_height=card_height,
                                         padding=padding)
    nodes_json.append({"type": "text",
                       "id": str(task_count),
                       "text":str(task_count)+'-'+task,
                       "x": int(x),
                       "y": int(y),
                       "width": card_width,
                       "height": card_height,
                       "color": color})       
    return nodes_json,task_count
