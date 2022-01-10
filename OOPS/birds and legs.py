#method-1
head_count=48
leg_count=140
for a in range(0,head_count):
    for b in range(0,head_count):    
        if ((a+b)==head_count) and ((a*4)+(b*2)==leg_count):
            print(a,b)
#method-2
head_count=100
leg_count=300
a=(leg_count-(head_count*2))//2
b=head_count-a
print(a,b)