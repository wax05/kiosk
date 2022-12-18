import random
import json

def Init(Path:str)->list:
    with open(Path) as f:
        setting = json.load(f)
    res = []
    res.append(setting["Item1"])
    res.append(setting["Item2"])
    res.append(setting["Item3"])
    res.append(setting["Item4"])
    res.append(setting["Item5"])
    res.append(setting["Item6"])
    res.append(setting["Item7"])
    res.append(setting["Item8"])
    res.append(setting["Item9"])
    res.append(setting["Item10"])
    return res
