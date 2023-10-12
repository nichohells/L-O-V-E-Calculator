
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1.lower() + name2.lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")


love = l + o + v + e

absolute_love = int(str(true) + str(love))

# Score

if (absolute_love < 10) and (absolute_love > 90):
    print(f"Your score is {absolute_love}, you go together like coke and mentos.")
elif (absolute_love >= 40) and (absolute_love <= 50):
    print(f"Your score is {absolute_love}, you are alright together.")
else:
    print(f"Your score is {absolute_love}.")


