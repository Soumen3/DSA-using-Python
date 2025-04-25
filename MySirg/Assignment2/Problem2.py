from math import pi

class Circle:
    def __init__(self,redius=None):
        self.redius=redius
    
    def setRadius(self, redius):
        self.redius=redius
    
    def getRedius(self):
        print(f'The redius is: {self.redius}')
    
    def getArea(self):
        print(f"The area of the circle is {pi * self.redius**2}")
    
    def getCircumference(self):
        print(f'The circumference of the circle is: {2 * pi * self.redius}')
    

c1=Circle(10)
c1.getRedius()
c1.getArea()
c1.getCircumference()

c1.setRadius(5)
c1.getRedius()
c1.getArea()
c1.getCircumference()