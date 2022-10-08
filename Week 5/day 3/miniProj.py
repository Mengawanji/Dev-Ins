class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        self.life -=1


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life=20, attack=10)
        self.attack = attack
        print("I am Druid")


    def meditate(self):
        self.life +=10
        self.attack -=2
        return f'Number of life of {self.name}: {self.life} \nand number of attack'
    def animal_help(self):
        self.attack +=5
    def fight(self ,other):
       other.life -= (0.75 * self.life + 0.75 * self.attack)
       return f'Number of life of {other.name}: {other.life} '

class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life=20, attack=10)
        self.attack = attack
        print("I am Warrior")
        if self.life < 1 or self.attack < 1:
            return f'{self.name} you lose '

    def brawl(self, other):
        self.life += 0.5 * self.attack
        other.life -= 2 * self.attack
        if other.life < 1:
            return f'{other.name} you lose'
        else:
            return f'Number of life of {self.name} : {self.life}'

    def train(self):
        self.life *= 2
        self.attack *= 2
        return f'Number of life of {self.name}: {self.life}'

    def roar(self, other):
        other.attack -= 3
        if other.attack < 1:
            return f'{other.name} you lose'
        else:
            return f'Number of attack of {other.name}: {other.attack}'

class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life=20, attack=10)
        self.attack = attack
        print("I am a Mage")

    def curse(self, other):
        other.attack -= 2
        if other.attack < 1:
            return f'Number of attack of {other.name}: {other.attack}'

    def summon(self):
        self.attack += 3
        return f'Number of attack of {self.name}: {self.attack}'

    def cast_spell(self,other):
        if self.life < 1:
            return f'{self.name} you lose'
        else:
            num = int(self.attack / self.life)
            other.life -= num
            if other.attack < 1:
                return f'{other.name} you lose'
            else:
                return f'Number of life of {other.name} : {other.life}'

druid1 = Druid("Panoramix")
warior = Warrior("Asterix")
mage = Mage("Merlin")

print(druid1.meditate())
print(druid1.animal_help())
print(druid1.fight(warior))

print(warior.brawl(mage))
print(warior.train())
print(warior.roar(druid1))

print(mage.curse(druid1))
print(mage.summon())
print(mage.cast_spell(warior))