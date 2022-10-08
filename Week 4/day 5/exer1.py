add=['a','b','c','b','d','m','n','n','e','g','f','r','e']
dup=[]
for item in add:
    if add.count(item) > 1:
        dup.append(item)
print(dup)

