import random

lotto = str(random.randint(100,999))
lotto1 = lotto[0]
lotto2 = lotto[1]
lotto3 = lotto[2]

print("Lotto number is: ", lotto)

user_guess = str(input("Please enter a three digit number: "))
digit1 = user_guess[0]
digit2 = user_guess[1]
digit3 = user_guess[2]

if user_guess == lotto:
    print("Exact Match")
elif digit1 in lotto and digit2 in lotto and digit3 in lotto:
    print("Exact Numbers, but mismatch")
elif digit1 in lotto or digit2 in lotto or digit3 in lotto:
    print("one match")
else:
    print("no match")
    
