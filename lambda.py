s=int(input("Enter the side of square:"))
area1=lambda s:(s*s)
print("area of square:",area1(s))
b=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of triangle:"))
area2=lambda b,h:(b*h)/2
print("area of triangle:",area2(b,h))
l=int(input("Enter the length of rectangle:"))
br=int(input("Enter the breadth of rectangle:"))
area3=lambda l,br:(l*br)
print("Area of rectangle:",area3(l,br))
