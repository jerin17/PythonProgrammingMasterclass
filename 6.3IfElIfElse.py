# name = input("Enter your name : ")
# age = int(input("How old are you, {}? ".format(name)))
#
# if age > 18:
#     print("\nHey, {}. You're old enough to vote.".format(name))
#     print("Please put in your vote in the box.")
# else:
#     print("\nWhoops. Not 18 yet !!!")
#     print("Please come back after {} years please.".format(18-age))

guess = int(input("Enter a number betweeen 1 and 10 : "))

if guess != 5:
    if guess < 5:
        print("Please enter a higher number : ")
    else:
        print("Please enter a lower number : ")
    guess = int(input())
    if guess == 5:
        print("\nWell done.")
    else:
        print("\nrehne de bhai, nahi hogaaaaaa")

else:
    print("\n\nWaah mere sher, chak de fatte !!!!")