import re
#to return digits present in string
a="Rajeev has 12 billion biabedn"
x=re.findall("\d",a)
print(x)
#find internal words
y=re.findall("bi....n",a)
#to find word when we dont know how many letters are in between (.*)
c=re.findall("R.*v",a)
print(c)
print(y)
#^=startswith(for whole string)
z=re.findall("^R",a)
print(z)
#$ if string ends with n
b=re.findall("n$",a)
print(b)
#find words match with dots 
d=re.findall("R....?v",a)
print(d)
e=re.findall("bi.{4}n",a)
print(e)
f="hello world"
#find whether the given word is inside string
g=re.findall("hello|max",f)
print(g)
#if string starts with given word (\A_)
h=re.findall("\Ah",f)
print(h)
#if string ends with given word
i=re.findall("\Bl",f)
print(i)