#Write A Program to display all stings that are in UPPERCASE from a file and also find the total size of the file.
import os
fr=input("Enter filename:")
with open(fr,'r') as fh:
    c=fh.readlines()
    print("Uppercase words are:")
    for line in c:
        w=line.split()
        for word in w:
            if word.isupper()==True:
                print(word)
with open(fr,'a') as fh:
    fh.seek(0,os.SEEK_END)
    print("\nSize of the file is",fh.tell(),"bytes.")