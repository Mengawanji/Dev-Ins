class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def instance(self):
        print("I am ", self.name ," i have " ,self.age ,"years old")


cat1 = Cat("kodak", "3")
cat2 = Cat("Diesel", "9")
cat3 = Cat("rambo", "4")

#create a function that finds the oldest cat and return the funtion

def oldest():
        if cat1.age > cat2.age and cat1.age > cat3.age:
            print(f"The oldest cat is: {cat1.name} and he has {cat1.age} years old")
        elif cat2.age > cat1.age and cat2.age > cat3.age:
            print(f"The oldest cat is: {cat2.name} and he has {cat2.age} years old")
        elif cat3.age > cat1.age and cat3.age > cat2.age:
            print(f"The oldest cat is: {cat3.name} and he has {cat3.age} years old")
oldest()

