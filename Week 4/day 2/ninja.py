fore = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
fore_list= fore.split(" ")
print(fore_list)
for i in fore_list:
    if fore_list.count(i)>1:
        print(i, ':', fore_list.count(i))
    else:
        if fore_list.count(i) == 1:
            print(i, ':', fore_list.count(i))