import importtest
print(__name__)

importtest.fun1()
importtest._fun2()

personal_details = ("Tim", 24, "Australia")
name, _, country = personal_details

print(name)
print(_)
