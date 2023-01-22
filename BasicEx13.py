#Print multiplication table from 1 to 10
x = int(input("Please input the dimension of the multiplication table. n = "))
for i in range(1,x+1):
    for j in range(1,x+1):
        print(i * j, end=" ")
    print()