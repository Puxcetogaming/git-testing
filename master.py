import time

i = 0

while True:
    print("Moved north")
    if i != 5:
        print("Can't Harvest")
        i = i + 1
        time.sleep(1)
    else:
        print("Can Harvest")
        print("Planted bush")
        i = 1
        time.sleep(1)
    

