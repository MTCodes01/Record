#Write a program in python to generate rondom number between 1-6 (like a dice)

import random
ans=str(input("play(y):"))
play=ans
while play=="y":
    while True:
        n=random.randint(1,6)
        print(n,"\n")
        ans=str(input("playmore?(y):"))
        if ans.lower()!="y":
            play="n"
            print("Exited!")
            break
else:
    print("Exited!")
