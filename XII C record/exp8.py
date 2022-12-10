#Write a program to count and display the frequency of words from a text file "test.txt"
def frequencyofwords(filename):
    f=open(filename,'r')
    Wordslist=[]
    Content=f.readlines()
    for line in Content:
        Words=line.split()
    for i in Words:
        Wordslist.append(i)
    uniquewords=list(set(Wordslist))
    for words in uniquewords:
        print(words,":",Wordslist.count(words))
#_main()_
fileName=input("Enter File Name:")
frequencyofwords(fileName)