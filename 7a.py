import math
class shape:
    def __init__(self):
        self.area=0
        self.name=""
    def showarea(self):
        print("The area of ",self.name," is ",self.area)

class triangle(shape):
    def __init__(self,base,height):
        self.area=0
        self.base=base
        self.height=height
        self.name="triangle"
    
    def calcarea(self):
        self.area=0.5*self.base*self.height

class circle(shape):
    def __init__(self,radius):
        self.area=0
        self.radius=radius
        self.name="Circle"
    
    def calcarea(self):
        self.area=math.pi*self.radius*self.radius

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.area=0
        self.name="rectamgle"

    def calcarea(self):
        self.area=self.length*self.breadth

c1=circle(5)
c1.calcarea()
c1.showarea()

t1=triangle(3,4)
t1.calcarea()
t1.showarea()

r1=rectangle(5,4)
r1.calcarea()
r1.showarea()