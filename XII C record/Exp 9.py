#Write a program to count and display the frequency of words from a text file "test.txt"
with open("test.txt",'r') as F:
    l=[]
    w=str(F.readlines()).split()
    for i in w:l.append(i)
    for W in set(l):print(W,":",l.count(W))