A=float(input("Enter Your First Number\n"))
B=float(input("Enter Your Second Number\n"))
C=float(input("Enter Your Third Number\n"))
if A>=B and A>=C:
    print("The Largest Number",A)
elif B>=A and B>=C:
    print("The Largest Number",B)
elif C>=A and C>=B:
    print("The Largest Number",C)
else:
    print("All are Equal Number")