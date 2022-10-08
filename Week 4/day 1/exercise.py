#Ask the user for a number between 1 and 100

#If the number is a multiple of three, print "Fizz"

#If the number is a multiple of five, print "Buzz".

#If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

user =  int(input("Enter number betwen 1 and 100"))
if user >=1 and user < 101:
    print("good")
    if user %3==0 and user %5==0:
        print("FizBuzz") 
    if user %3==0:
        print("Fizz")
    if user %5==0:
        print("Buzz")
else:
     print("Please enter a valid num")


