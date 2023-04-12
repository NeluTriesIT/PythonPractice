#Accept a list of n floats as an input from the user
n = int(input("How many floats would you like to add? "))
string_float = []
for i in range(1, n+1):
    string_float.append(float(input(f"Introduce number {i} = ")))
print(f"Final string list is_{string_float}")