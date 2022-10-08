user = input("enter ten charecters: ")
if len(user)<10:
    print("String not long enough")
if len(user)>10:
    print("String too long")
else:
    print(user[0] + user[-1])


