def squareperi(x):
  perimeter=4*x
  print("perimeter of square is",perimeter)

def rectangleperi(l,b):
  perimeter = 2*(l+b)
  return perimeter

def circumference(r):
  c=2*3.14*r
  print("circumference of circle is",c)

r=int(input("enter radius of circle:"))
circumference(r)

x=int(input("Enter side of square->"))
squareperi(x)

l = int(input("Enter length of rectangle->"))
b = int(input("Enter breadth of rectangle->"))
print(rectangleperi(l,b))