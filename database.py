import json
__fileName = "./items.json"
def LoadingJsonFile():
    with open(__fileName,"r") as file:
        data = json.load(file)
    return data

def WritingJsonFile(newItem,data):
    data.append(newItem)
    with open(__fileName,"w") as file:
        json.dump(data,file,indent=4)
def start(newData):
    ExsitingData = LoadingJsonFile()
    WritingJsonFile(newData,ExsitingData)
    
def EditJsonFile():
    pass 
    #TODO need to implement add(),delete() and edit()
    