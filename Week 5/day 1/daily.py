class Farm():
    def __init__(self):
        self.name = "McDonald"
        self.animal = {}

    def get_info(self):
        print(f"{self.name} 's farm")
        for animals in self.animal:
            print(f"{animals} : {self.animal[animals]}")

    def add_animal(self, animals, number=1):
       if animals in self.animal:
           self.animal[animals] += number
       else:
           self.animal[animals] = number

    def get_animal_types(self):
        print(sorted(list(self.animal)))



macdonald = Farm()
macdonald.get_info()
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_animal_types()
print(macdonald.get_info())
print(f"{'-'.join(list('EIEI0')).center(22)}") ,"!"
