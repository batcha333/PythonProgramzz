import re
#to return digits present in string
a="Rajeev has 12 billion biabedn"
x=re.findall("\d",a)
print(x)
#find internal words
y=re.findall("bi....n",a)
print(y)
#^=startswith
z=re.findall("^h",a)
print(z)