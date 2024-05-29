"""
Serialization/Deserialization:
    pickle => bytes (binary format)
    json => str (text format): str, int, float, bool, tuple, list, dict, NoneType
"""
import pickle

data=[12, 3.4, True, "Abc"]

with open("data.json", "wb") as aFile:
    pickle.dump(data, aFile)
    
# or 
# aFile=open("data.pick", "wb") 
# ....
# aFile.close()
