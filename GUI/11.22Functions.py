def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" "*left_margin, text)
# python_food()
# print(python_food())


# def center_text(text):
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     print(" "*left_margin, text)
#
#
# center_text("spam and eggs")
# center_text("spam, spam and eggs")
# center_text(12)
# center_text("spam, spam, spam and spam")
# print("first", "second", 3, 4, "spam")

# def center_text(*args, sep=' ', end='\n', file=None, flush=False):
#     text = ""
#     for i in args:
#         text += str(i) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" "*left_margin, text, end=end, file=file, flush=flush)
#
#
# with open("centerText", mode='w') as cT:
#     center_text("spam and eggs", file=cT)
#     center_text("spam, spam and eggs", file=cT)
#     center_text(12, file=cT)
#     center_text("spam, spam, spam and spam", file=cT)
#     print("first", "second", 3, 4, "spam", file=cT)
#     center_text("Jerin", "Thomas", 1, 2, 3, sep=':', file=cT)


def center_text(*args, sep=' '):
    text = ""
    for i in args:
        text += str(i) + sep
    left_margin = (80 - len(text)) // 2
    return " "*left_margin + text


print(center_text("spam and eggs"))
print(center_text("spam, spam and eggs"))
print(center_text(12))
print(center_text("spam, spam, spam and spam"))
print("first", "second", 3, 4, "spam")
print(center_text("Jerin", "Thomas", 1, 2, 3, sep=':'))
print("=" + str(12 * 3))
print(sorted(["b", "d", "c", "a"]))
