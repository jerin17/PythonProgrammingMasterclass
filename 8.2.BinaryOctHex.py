# print("Decimal |  Binary  | Hex")
# print("-" * 25)
#
#
# for i in range(18):
#     print("{0:>7} | {0:>08b} | {0:02x}".format(i))
#
# x = 0x20
# y = 0x0a
# print("x :", x)
# print("y :", y)
# print("x * y :", x * y)
# print(0b0010100)
# print(0b10100)

powers = []
for i in range(15, -1, -1):
    powers.append(2 ** i)
    # powers.append(8 ** i) - for hexa
    
print(powers)
flag = False

x = int(input("Please enter a number : "))
for i in powers:
    bit = x // i
    if bit != 0:
        flag = True
    if flag == True:
        print(bit, end='')
    x %= i
