def BlockWord(InputID:str)->bool:
    if InputID.find("-") != -1:
        return False
    elif InputID.find("#") != -1:
        return False
    elif InputID.find("*") != -1:
        return False
    elif InputID.find("/") != -1:
        return False
    else:
        return True