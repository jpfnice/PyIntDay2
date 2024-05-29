"""
Serialization/Deserialization:
    pickle => bytes (binary format)
    json => str (text format): str, int, float, bool, tuple, list, dict, NoneType
"""
import json
#import datetime

with open("data.json", "r") as aFile:
    aList=json.load(aFile)

print(aList, type(aList))
aList.append(56)
print(aList, type(aList))