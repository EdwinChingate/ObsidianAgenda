import yaml
def SearchActivity(File):
    doc=[]
    try:
        with open(File, 'r') as file:
            YamlFile=yaml.safe_load_all(file)
            for page in YamlFile:
                doc.append(page)
    except:
        print('')
    activity=doc[0]['activity']
    return activity
