fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "round and crunchy"}

# print(fruit)
# print()
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# print()
# fruit["lime"] = "great with tequila"
# print(fruit)
# print()
# # del fruit - to delete the variable itself
# # fruit.clear() - to remove everything from dictionary itself
# # del fruit["lemon"]
# # print(fruit)
# # fruit.clear()
# # print(fruit)
# print(fruit["tomato"])

while True:
    key = input("Please enter a fruit : ")
    if key == "quit":
        break
    if key in fruit:
        description = fruit.get(key)
        print(description)
    else:
        print("we don't have ", key)



# bike = {"make": "Honda", "model": "250 dream", "color": "red", "engine_size": 250}
# print(bike)
# print(bike["color"])
# print(bike["engine_size"])
