import time
import random
print("Go get your moms credit card")
time.sleep(1)
haveCard = 0.0
ree  = 0.0
while haveCard == 0.0: 
    print("Do you have it? (y/n)")
    i = input()
    if i.lower() == "y":
        break
    else:
        print("you need your moms card so go get it")
print("enter the number on the back")
cardNumber = input()
while 0 == 0:
    cardNumber = input()
    if(len(cardNumber) >= 13 and len(cardNumber) <= 19):
        break
    else:
        print("ur number is wrong, try again")
print("enter the expiration date")
expDate = input()
while 0 == 0:
    expDate = input()
    if(len(expDate) >= 4 and len(expDate) <= 5 ):
        if(expDate.isdigit()):
            break
print("enter the cvc")
cvc = input() 
while 0 == 0:
    cvc = input()
    if(len(cvc) == 3):
        break
    else:
        print("ur cvc is wrong, try again")
print("here is the data you've entered,\nthe card number is " + cardNumber + "\nthe Expiration date is " + expDate + "\nthe cvc is " + cvc)
while haveCard == 0.0: 
    print("is all the data correct? (y/n)")
    j = input()
    if j.lower() == "y":
        ree = 1.0
        break
    else:
        print("please rerun the program and enter your data correctly")
        break
if ree == 1.0:
    print("thanks, your data and money will be used well >:)")
sadness = random.randint(1, 1000000)
if sadness == 69420:
    print("        _______________________________________         _______________________________________\n       |                                       |       |                                       |\n       |                                       |       |                                       |\n       |                                       |       |                                       |\n       |                                       |       |                                       |\n       |       __                       __     |       |       __                       __     |\n       |      |  |                     |  |    |       |      |  |                     |  |    |\n       |      |__|                     |__|    |       |      |__|                     |__|    |\n       |                                       |       |                                       |\n       |          _____________________        |       |         |_____________________|       |\n       |         |                     |       |       |                                       |\n       |                                       |       |                                       |\n       |_______________________________________|       |_______________________________________|")
    print("wow thats rare :)")
    print("the value that made this happen was " + sadness)