H=float(input("Hindi Marks\n"))
E=float(input("English Marks\n"))
M=float(input("Mathematics Marks\n"))
P=float(input("Physics Marks\n"))
C=float(input("Chemistry Marks\n"))
tm=(H+E+M+P+C)
print("Total Marks =",tm)
p=tm*100/500
print("Percentage = ",p)

if p>=80:
    print("Grade A")
elif p>=70:
    print("Grade B")
elif p>=60:
    print("Grade C")
elif p>=40:
    print("Grade D")
else:
    print("Fail")