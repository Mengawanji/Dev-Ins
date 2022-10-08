  
import random


class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0
        return self

class Chromosome:
    def __init__(self, rand_mutate):
        self.Chromo = [Gene() for i in range(10)]
        self.rand_mutate = rand_mutate

    def mutate(self):
        self.Chromo = [gene.mutate() if random.random() < self.rand_mutate else gene for gene in self.Chromo]
        return self


class DNA:
    def __init__(self, rand_mutate=.5):
        self.D = [Chromosome(rand_mutate) for i in range(10)]
        self.rand_mutate = rand_mutate

    def mutate(self):
        self.D = [chromosome.mutate() if random.random() < self.rand_mutate else chromosome for chromosome in self.D]


class Organism:
    def __init__(self, DNA, para):
        self.DNA = DNA
        self.DNA.rand_mutate = para


temp = DNA()
for chrom in temp.D:
    for gene in chrom.Chromo:
        print(gene.value, end=" ")
    print()
print()
org = Organism(temp, .25)
total = 0
while True: # this finds only 1 line since finding 10 lines of 10 1's will take forever
    count = 0
    for chrom in org.DNA.D:
        for gene in chrom.Chromo:
            count += gene.value
        if count == 10:
            break
        else:
            total += 1
            count = 0
    if count == 10:
        break
    org.DNA.mutate()
print(total)