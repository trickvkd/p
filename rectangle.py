class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area of rectangle:",self.length*self.breadth)
    def perimeter(self):
        print("Perimeter:",2*(self.length+self.breadth))
a=int(input("Enter length:"))
b=int(input("enter breadth:"))        
rec1=rectangle(a,b)
rec1.area()
rec1.perimeter()
