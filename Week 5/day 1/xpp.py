from dataclasses import dataclass
from unicodedata import name


class Dog:
    def __init__(self, name, height):
        self.name=name
        self.height=height

    def bark(self):
        print (f"{self.name} goes WOOF!")
    def jump(self):
        print (f"{self.name} jumps {self.height*2} cm high!")


davids_dog= Dog("Rex",50)
print(f"davids_dog is called{davids_dog.name} and is {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog= Dog("TeaCup",20)
print(f"davids_dog is called{sarahs_dog.name} and is {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog > sarahs_dog:
    print("davids_dog")
else:
    print("sarahs_dog")
    

