r1 = range(0, 100)
r2 = r1[3: 40: 3]
print("r1 : {} \nr2 : {}".format(r1, r2))

print(r2 == range(3, 40, 3))
# True

print(range(0, 5, 2) == range(0, 6, 2))

print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))
# True - sequence is same : [0, 2, 4]

r3 = range(0, 100)
print(r3)

for i in r3[::-2]:
    print(i, end=' ')
print()

print(range(0, 100)[::-2])
print()

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])
# range in reverse

r4 = range(0, 10)
for i in r4[::-1]:
    print(i, end=' ')


o = range(0, 100, 5)
print(o)
p = o[::5]
for i in p:
    print(i)
# 0
# 25
# 50
# 75