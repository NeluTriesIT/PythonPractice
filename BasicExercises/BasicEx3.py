#Input a string from the user and display characters that are present at an even index number.
a = input("Please provide a string: ")

for i in range(0,len(a), 2):
    print(a[i])
