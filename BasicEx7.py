#Write a program to find how many times substring "Emma" appears in the given string.
#Given: Emma is a good developer. Emma is also a writer.  ---> Emma appeared 2 times

given=input("Please provide some senteces: ")
nr = given.count(input("Please provide target: "))
print(f"Your target appeared {nr} time/s")