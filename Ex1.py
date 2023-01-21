#Given 2 integer number return their product only if the product is equal to or lower than 1000,
#else return their sum.

a = int(input("First number = "))
b = int(input("Second number = "))
if(a * b <= 1000):
    print(f"The product result is: {a *b}")
else:
    print(f"The sum result is: {a + b}")
