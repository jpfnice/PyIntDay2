"""
Serialization/Deserialization:
    pickle => bytes (binary format)
    json => str (text format): str, int, float, bool, tuple, list, dict, NoneType
"""
import pickle
import datetime

with open("data.pick", "rb") as aFile:
    aList=pickle.load(aFile)

print(aList, type(aList))
aList.append(56)
print(aList, type(aList))