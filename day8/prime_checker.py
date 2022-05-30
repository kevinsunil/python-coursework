#Write your code below this line 👇
import math
def prime_checker(number):
    if number == 0:
        print("It's not a prime number.")
    elif number == 1 or number == 2:
        print("It's a prime number.")
    else:
        check = 0
        for i in range(2,math.ceil(number/2)+1):
            if number % i == 0:
                check += 1
        if check > 0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
