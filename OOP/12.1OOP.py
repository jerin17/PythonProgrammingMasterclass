class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
# kenwood.switch_on()
print(kenwood.make, kenwood.price, kenwood.on)
kenwood.__init__("k", 888)
print(kenwood.make, kenwood.price, kenwood.on)
print()

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power) error, since no parameter for kettle named power

Kettle.power_source = 'Solar'

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print()

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
