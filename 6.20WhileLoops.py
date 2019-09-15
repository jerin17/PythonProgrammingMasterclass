for i in range(10):
    print(i, end=' ')
print()

i = 0
while i < 10:
    print(i, end=' ')
    i += 1
print('\n')
# Infiite loop
# while True:
#     print(i)

available_exits = ["east", "north east", "south"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction : ")
    if chosen_exit == "quit" or chosen_exit == 'exit':
        print("\nGame Over.")
        break
else:
    print("\nAren't you glad, you made it through !!!!")