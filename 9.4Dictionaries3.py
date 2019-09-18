# fruit = {"orange": "a sweet, orange, citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour, yellow citrus fruit",
#          "grape": "a small, sweet fruit growing in bunches",
#          "lime": "a sour, green citrus fruit"}
# print(fruit)
#
# fruit_keys = fruit.keys()
# # print(fruit_keys)
# # fruit["tomato"] = "not nice with ice cream"
# # print(fruit_keys)
# print()
#
# # to get dictionary as a tuple - fruit.item
# print(fruit.items())
# t = tuple(fruit.items())
# print(t)
# print()
# for i in t:
#     item, description = i
#     print("{:7} : {}".format(item, description))
#
# print()
# x = dict(t)
# print(x)

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

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

location = 1
while True:
    availableExits = ", ".join(exits[location].keys())

    print()
    print(locations[location])
    print("Available Directions : " + availableExits)
    direction = input("Where do you wanna go ? : ").upper()

    if direction == 'Q':
        print("\n"+locations[0])
        break

    if direction in exits[location]:
        location = exits[location][direction]
    else:
        print("You cannot go in that direction !")