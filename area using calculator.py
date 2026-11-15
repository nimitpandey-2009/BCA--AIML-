print("-----AREA CALCULATOR-----")
print("(1) for Area of Rectangle")
print("(2) for Area of Square")
print("(3) for Area of Circle")
print("(4) for Area of Triangle")

choice=int(input("Enter your choice (1-4)\n"))

if choice==1:
    l=float(input("Enter length\n"))
    b=float(input("Enter breadth\n"))
    a=l*b
    print("Area  of Rectangle=",a)

elif choice==2:
    s=float(input("Enter side\n"))
    a=s**2
    print("Area of Square=",a)

elif choice==3:
    r=float(input("Enter Radious\n"))
    a=r*3.14
    print("Area of Circle=",a)

elif choice==4:
    b=float(input("Enter Base\n"))
    h=float(input("Enter Height\n"))
    a=1/2*b*h
    print("Area of Triangle=",a)