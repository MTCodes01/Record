lst=[]
for i in range(5):
    st=input(" ")
    s=st.split()
    lst.append((s[0],",",str(s[1]),s[2],s[3],str(s[4]),s[5]))
print("INSERT INTO orders\nVALUES(",lst[0],"),\n")
for i in range(1,len(lst)):
    print("(",lst[i],"),\n")
#(int,"",int,int,date,discount)