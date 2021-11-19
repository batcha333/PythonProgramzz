f=open("demo1.txt","r+")
user=input("user:")
word=input("pass:")
a=user+" "+word
for i in f:
    if a in i:
        print("User already found")
        break
else:
    b=user+" "+word
    f.write("\n")
    f.write(b)
    print("new account created")
f.close()