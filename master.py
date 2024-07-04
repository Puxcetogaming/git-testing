import random
import os

x = 0
y = 0
z = 0
blocksBroken = 0
blockSpawn = (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))


while True:

    move = input("Enter a move: ")
    if move == "north":
        amount = int(input("How many: "))
    elif move == "south":
        amount = int(input("How many: "))
    elif move == "east":
        amount = int(input("How many: "))
    elif move == "west":
        amount = int(input("How many: "))
    elif move == "up":
        amount = int(input("How many: "))
    elif move == "down":
        amount = int(input("How many: "))
    else:
        amount = 0

    match move:
        case "north":
            y = y + amount
        case "south":
            y = y - amount
        case "east":
            x = x + amount
        case "west":
            x = x - amount
        case "up":
            z = z + amount
        case "down":    
            z = z - amount
        case "position":
            print(f"({x}, {y}, {z})")
        case "break block":
            if (x, y, z) == blockSpawn:
                print("Block broken")
                blockSpawn = (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))
                blocksBroken = blocksBroken + 1
            else:
                print("No block to break")
        case "spawn block":
            blockSpawn = (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))
            print(f"Block spawned at {blockSpawn}")
        case "blocks broken":
            print(f"Blocks broken: {blocksBroken}")
        case "locate block":
            print(f"Block located at {blockSpawn}")
        case "help":
            print("Valid moves are: north, south, east, west, up, down, position, break block, spawn block, blocks broken, locate block, help, exit")
        case "exit":
            break
        case _:
            print("Invalid move")


folder_path = '/home/iliyan/Coding folder/git testing/Score' 

if not os.path.exists(folder_path): 
    os.makedirs(folder_path) 

file_name = 'Last Score.txt'
file_path = os.path.join(folder_path, file_name) 
 
with open(file_path, 'w') as f: 
    f.write(f"Last score: {blocksBroken}") 


# Game where you move and break blocks