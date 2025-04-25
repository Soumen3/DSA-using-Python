class Rectangle:
    def __init__(self, length=None, breadth=None):
        self.length=length
        self.breadth=breadth
    
    def setDimensions(self,length=None, breadth=None):
        self.length=length
        self.breadth=breadth

    def showDimension(self):
        print(f"The length is: {self.length}")
        print(f"The breadth is: {self.breadth}")

    def getArea(self):
        print(f"The area of the rectangle is: {self.length * self.breadth}")


r1=Rectangle(10,8)
r1.showDimension()
r1.getArea()

r1.setDimensions(5,4)
r1.showDimension()
r1.getArea()