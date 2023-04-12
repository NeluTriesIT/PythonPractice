#Write a program to count the total number of digits in a number using a while loop.
n = int(input("Insert number = "))
ct = 0
while n > 0:
    ct += 1
    n = int(n/10)

print(f"The number has {ct} digits.")