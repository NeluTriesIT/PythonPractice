#Print the following pattern 
#1
#1 2
#1 2 3
#1 2 3 4...etc
n = int(input("Number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()