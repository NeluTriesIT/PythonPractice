import os
if os.stat("test.txt").st_size == 0:
    print("FIle is empty!")
else:
    print("File is not empty")