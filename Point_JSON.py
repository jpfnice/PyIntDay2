class Point:
    __counter=0 # A class attribute
    def __init__(self, vx, vy):
        self.__x=vx   # attribute x is defined here
        self.__y=vy   # attribute y is defined here
        Point.__counter += 1
    def __del__(self):
        Point.__counter -= 1
    def __str__(self):
        return f"<{self.__x},{self.__y}>"
    def __repr__(self):
        return f"<{self.__x},{self.__y}>"
    def __add__(self, other):
        return Point(self.__x+other.__x, self.__y+other.__y)
    
    @classmethod
    def getCounter(self): # A class method
        return self.__counter
    
    def distance(self, other):
        import math
        return math.sqrt((other.__x-self.__x)**2 + (other.__y-self.__y)**2)
    
    def clear(self):
        self.__x=self.__y=0
        
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid attribute value {value}")
        self.__x=value
   
    @property
    def y(self):
        return self.__y
    # y=property(y)
    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid attribute value {value}")
        self.__y=value
    #y=y.setter(y)
    
    @staticmethod
    def json_encoder(obj):
        return {"Point":True, "x":obj.x, "y":obj.y}
    
    @staticmethod
    def json_decoder(obj):
        if "Point" in obj:
            return Point(obj["x"], obj["y"])
        else:
            raise Exception("This JSON String does not a represent a Point")
            
            
p1=Point(3,4)
p2=Point(7,8)

l1=[p1,p2]

import json

# with open("point.json", "w") as fic:
#     json.dump(l1, fic, default=Point.json_encoder)
    
with open("point.json") as fic:
    p=json.load(fic, object_hook=Point.json_decoder)  
    print(p)

