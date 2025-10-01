def Write_DF_as_markdownTable(MessagesDF,SavedMessage,
                              join='|',
                              endLine='\n'):    
    ColumnsNamesList=list(MessagesDF.columns)
    N_columns=len(ColumnsNamesList)
    Text=join+join.join(ColumnsNamesList)+join+endLine
    Text=Text+join+join.join(N_columns*['--------'])+join+endLine
    for index in MessagesDF.index:
        message=join+join.join(list(MessagesDF.loc[index]))+join+endLine
        Text+=message
    with open(SavedMessage, 'w') as file:
        file.write(Text)    
