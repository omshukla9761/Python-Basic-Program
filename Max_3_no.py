a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Minimum =", a)
elif b <= a and b <= c:
    print("Minimum =", b)
else:
    print("Minimum =", c)
