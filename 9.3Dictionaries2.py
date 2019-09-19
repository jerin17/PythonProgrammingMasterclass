fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# for j in range(10):
#     for i in fruit:
#         print(i + " " + fruit[i])
#     print()

# ordered_keys = sorted(list(fruit.keys()))
# for i in ordered_keys:
#     print("{:<7}".format(i) + ": "+fruit[i])

for i in sorted(list(fruit.keys())):
    print("{:<7}".format(i) + ": "+fruit[i])
print()

for i in fruit.values():
    print(i)
print()

for i in fruit:
    print(fruit[i])

print(fruit.keys())
print(fruit.values())