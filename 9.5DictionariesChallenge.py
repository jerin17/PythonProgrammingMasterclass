
#                                                 NORTH
#     |------> 5. Forest                        ^
#     |             ^                           |
#     |             |                           |
#     V             v                           |
# 2. Hill <--- 1. Road <----> 3. Building
#     ^             ^
#     |             |
#     |             v
 #     |------  4. Valley

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in a forest"
             }

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

words = {"QUIT": "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W"
         }

# SPLIT
# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

location = 1
while True:
    availableExits = ", ".join(exits[location].keys())

    print()
    print(locations[location])
    print("Available Directions : " + availableExits)
    direction = input("Where do you wanna go ? : ").upper()

    if len(direction) > 1:
        for i in words:
            if i in direction:
                direction = words[i]

    if direction == 'Q':
        print("\n"+locations[0])
        break

    if direction in exits[location]:
        location = exits[location][direction]
    else:
        print("You cannot go in that direction !")
