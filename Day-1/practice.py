"""x=1101
y=x
op=""
while y!=0:
    op=op+str(y%10)
    y=y//10
if int(op)==x:
    print("is a palindrome")
else:
    print("not a palindrome")
    """

#3 - Guessing
import random
random_num=random.randint(1,10)
def guessmethod(random_num):
    guess=int(input("Guess the number:")) 
    if random_num==guess:
        print("well guessed")
        return
    else:
        guessmethod(random_num)
guessmethod(random_num)

