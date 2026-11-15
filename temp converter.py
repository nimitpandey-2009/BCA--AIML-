
a = input("If you want to convert Fahrenheit to Celsius press (C), or Celsius to Fahrenheit press (F):\n").upper()

if a == "C":
    f = float(input("Temperature in Fahrenheit:\n"))
    c = (f - 32) * 5 / 9
    print("Temperature in Celsius:", c)

elif a == "F":
    c = float(input("Temperature in Celsius:\n"))
    f = (c * 9 / 5) + 32
    print("Temperature in Fahrenheit:", f)

else:
    print("Invalid Choice")
