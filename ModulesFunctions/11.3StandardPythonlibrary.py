print(dir())
print(dir(__builtins__))

import shelve
print(dir())
print()
print(dir(shelve))

for i in dir(shelve.Shelf):
    if i[0] != '_':
        print(i)

# help
help(shelve)