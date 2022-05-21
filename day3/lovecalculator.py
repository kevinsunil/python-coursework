# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nameone = name1.lower()
nametwo = name2.lower()
count_t = (nameone.count("t") + nametwo.count("t"))
count_r = (nameone.count("r") + nametwo.count("r"))
count_u = (nameone.count("u") + nametwo.count("u"))
count_e = (nameone.count("e") + nametwo.count("e"))
count_l = (nameone.count("l") + nametwo.count("l"))
count_o = (nameone.count("o") + nametwo.count("o"))
count_v = (nameone.count("v") + nametwo.count("v"))
final_true = count_t + count_r + count_u + count_e
final_love = count_l + count_o + count_v + count_e
truelove = (final_true*10) + final_love
if truelove <  10 or truelove > 90:
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove > 40 and truelove < 50 :
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")
