#Write a program in python to generate rondom number between 1-6 (like a dice)

import random
import time
print("press CTRL+C to stop the dice")
ans=str(input("play(y):"))
play=ans
while play=="y":
    try:
        while True:
            for i in range(10):
                print()
            n=random.randint(1,6)
            print(n,end=' ')
            time.sleep(0.00001)
    except KeyboardInterrupt:
        print("your number is",n)
        ans=str(input("playmore?(y):"))
        if ans.lower()!="y":
            play="n"
            print("Exited!")
            break
else:
    print("Exited!")

    