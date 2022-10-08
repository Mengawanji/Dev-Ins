class Animals():
    name = "Pink"
    leg = 4

    def walk(self):
        print("Hey,I'm Walking")

class Dog(Animals):
        pass

one = Animals()
print(one.name)

two= Dog()
print(two.walk())


class Door:
    is_opened = "is_opened "

    def open(self):
        print("The door is open")

    def clossed(self):
        print("The door is closed")

class BlockedDoor(Door):

    def open(self):
        print("The door cannot be opened and closed")

    def closed(self):
        print("The door cannot be opened and closed")
done = BlockedDoor()
print(done.closed())