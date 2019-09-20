# jabber = open("C:\PythonPrograms\Pythonfiles\SampleText.txt",'r')
# for i in jabber:
#     print(i)
# jabber.close()


# jabber = open("Pythonfiles\SampleText.txt",'r')
# for i in jabber:
#     if "jabberwock" in i.lower():
#         print(i)
# jabber.close()

#   we can skip closing step
with open("SampleText.txt", 'r') as jabber:
    for i in jabber:
        if "JAB" in i.upper():
            print(i, end='')

#   readline
with open("SampleText.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

#   readlines
with open("SampleText.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
for i in lines:
    print(i, end='')


with open("SampleText.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
for i in lines[::-1]:
    print(i, end='')


with open("SampleText.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)
for i in lines[::-1]:
    print(i, end='')