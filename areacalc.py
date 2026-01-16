###------Area Calculator------###
import math 

while True:
  print("---------📐AREA CALCULATOR📐-----------")
  print("1.Square")
  print("2.Rectangle")
  print("3.Triangle")
  print("4.Circle")
  print("5.Exit!")
  

  choice= int(input("Choose a shape (1-5):"))

  if choice == 1:
    side=float(input("side:"))
    Area = side*side
    print("Area of sqaure",Area)

  elif choice == 2:
    length=float(input("length:"))
    width=float(input("width:"))
    Area= length*width
    print("Area of Rectangle",Area)

  elif choice == 3:
    height=float(input("height:"))
    base=float(input("base:"))
    Area=(height*base)/2
    print("Area of Triangle",Area)

  elif choice == 4:
    radius=float(input("radius:"))
    Area=math.pi* radius **2
    print("Area of Cicle",Area)

  elif choice == 5:
    print("You have exited the calculator!")
    break

  else:
    print("Wrong input!")



  