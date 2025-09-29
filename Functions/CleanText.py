def CleanText(text,clean='',join=' '):
    if len(clean)==0:
        clean_textList=text.split()
    else: 
        clean_textList=text.split(clean)
    clean_text=join.join(clean_textList)
    return clean_text
