"""
Serialization/Deserialization:
    pickle => bytes (binary format)
    json => str (text format): str, int, float, bool, tuple, list, dict, NoneType
"""
import json

data=[12, 3.4, True, "Abc"]

with open("data.json", "w") as aFile:
    json.dump(data, aFile)
    
# or 
# aFile=open("data.pick", "wb") 
# ....
# aFile.close()
