def SquareCardsCanvas(task_count,SquereSide,
                      card_width=500, 
                      card_height=120,
                      padding=70):
    col=task_count%SquereSide  
    row=task_count/SquereSide
    y=int(row)*(card_height+padding)
    x=int(col)*(card_width+padding)
    task_count+=1  
    return x,y,row,task_count
