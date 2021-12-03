a="sri"
b=iter(a)
print(b)
while True:
    try:
        c=next(b)
        print(c)
    except StopIteration:
        print("error")
        break
