user= input("enter a word: ")
dict=()
timm=[]
for(i,letter) in enumerate(user):
    timm.append(i)
    dict[letter] = []
    dict[letter].append(timm)
print(dict)



