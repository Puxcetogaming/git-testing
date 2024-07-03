import time

i = 0

while True:
    if i != 5:
        print("Can't Harvest")
        i = i + 1
        time.sleep(1)
    else:
        print("Can Harvest")
        i = 1
        time.sleep(1)
    

