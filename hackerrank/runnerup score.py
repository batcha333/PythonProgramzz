if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print(sorted(list(set(arr)))[-2])  




'''n = int(input(""))
l=[]
for i in range(n):
    a=int(input(""))
    l.append(a)
    l.sort()    
if(l[-1]==l[-2]):
    print(l[-3])
else:
    print(l[-2])'''