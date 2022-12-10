#Write a program to check whether a number is pallindrome or not
'''
n=int(input("Enter a number:"))
num=n
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if n==rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
'''
def palindrome(st):
    l=len(st)
    if (l/2)%2!=0:
        l+=1
        if st[0:(l/2)-1:1]==st[(l/2)+2:-1:-1]:
            return True
        else:
            return False
    elif st[0:l]==st[l-1:-1:-1]:
        return True
    else:
        return False
palindrome('aba')