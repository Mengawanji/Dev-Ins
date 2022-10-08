items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
wallet= "$300"
amount=int(wallet.replace("$",""))
newL=[]
for i in items_purchase.keys():
    if int(items_purchase[i].replace('$','').replace(',',''))<= amount:
      newL.append(i)
print(sorted(newL))
