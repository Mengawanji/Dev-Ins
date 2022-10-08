#ex 1
forr = 'Helloworld'
fore ='I love python'
x=0
while x <4:
    print(forr)
    x = x + 1
x=0
while x<4:
    print(fore)
    x = x + 1

#ex 2

user=int(input("Enter month number "))
if user >2 and user <6:
    print('Spring')
elif user >5 and user < 9:
    print('Summer')
elif user >8 and user < 12:
    print('Autum')
elif user <=2 or user == 12:
    print('Winter') 