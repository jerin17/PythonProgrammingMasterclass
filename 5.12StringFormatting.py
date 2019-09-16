age = 23
# print("My age is " + age + " years.")

print("My age is " + str(age) + " years.")
print("My age is {} years.".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May", "July",
                                                                          "August", "October", "Deceber"))
print()

print("""Jan : {2}
Feb : {0}
Mar : {2}
Apr : {1}
May : {2}
Jun : {1}
Jul : {2}
Aug : {2}
Sep : {1}
Oct : {2}
Nov : {1}
Dec : {2}
""".format(28, 30, 31))

print("My age is %d years." % age)
print("My age is %d %s, %d %s." % (age, "years", 8, "months"))

for i in range(1, 11):
    print("Square of %2d : %4d and cube of %2d : %4d" % (i, i**2, i, i**3))

for i in range(1, 11):
    print("Square of %2d : %3d %6s cub1e of %2d : %4d" % (i, i**2, " ", i, i**3))

#   %2d %3d %6s %2d %4d -  used for alligning be of %2d : %4d" % (i, i**2, " ", i, i**3))
#
# #   %2d %3d %6s %2d %4d -  used the numbers"

print("Pi is approximately %12f" % (22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 11):
    print("Square of {0:2} : {1:4} {3:10} cube of {0:2} : {2:4}".format(i, i**2, i**3, ' '))

# same allignment purpose. 0th string will get 2. 3rd sting will get 10

for i in range(1, 11):
    print("Squared of {0:2} : {1:<4} and cubed of {0:2} : {2:<4}".format(i, i ** 2, i ** 3))
# Squared of  1 : 1    and cubed of  1 : 1
# Squared of  2 : 4    and cubed of  2 : 8
# Squared of  3 : 9    and cubed of  3 : 27
# Squared of  4 : 16   and cubed of  4 : 64
# Squared of  5 : 25   and cubed of  5 : 125
# Squared of  6 : 36   and cubed of  6 : 216
# Squared of  7 : 49   and cubed of  7 : 343
# Squared of  8 : 64   and cubed of  8 : 512
# Squared of  9 : 81   and cubed of  9 : 729
# Squared of 10 : 100  and cubed of 10 : 1000

for i in range(1, 11):
    print("Squared of {0:2} : {1:>4} and cubed of {0:2} : {2:>4}".format(i, i ** 2, i ** 3))
# Squared of  1 :    1 and cubed of  1 :    1
# Squared of  2 :    4 and cubed of  2 :    8
# Squared of  3 :    9 and cubed of  3 :   27
# Squared of  4 :   16 and cubed of  4 :   64
# Squared of  5 :   25 and cubed of  5 :  125
# Squared of  6 :   36 and cubed of  6 :  216
# Squared of  7 :   49 and cubed of  7 :  343
# Squared of  8 :   64 and cubed of  8 :  512
# Squared of  9 :   81 and cubed of  9 :  729
# Squared of 10 :  100 and cubed of 10 : 1000


print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

for i in range(1, 12):
    print("Square of {:2} : {:4} and cube of {} {:4}".format(i, i ** 2, i, i ** 3))
