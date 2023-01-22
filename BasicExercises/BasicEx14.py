#Print downward Half Pyramid Pattern with Star(asterisk)
x = int(input("Please introduce the pyramid dimension: "))

for i in range(x, 0, -1):
    print("* " * x)
    x -= 1
