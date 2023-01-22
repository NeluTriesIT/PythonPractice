#Print the following Pattern:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

x = int(input("Tell me the dimension: "))
for i in range(1,x+1):
    print((str(i) + " ") * i)    #concatenation of the string with " "