#Display an n number of strings as only one
#Name, is, James ==> Name**is**James
n = int(input("Number of strings you want to combine: "))
b = ""
for i in range(n):
    b += input(f"String {i+1} :")
    if(i < n-1):
        b+= "**"
print(b)

