#permute and combine with itertools
from itertools import permutations as pt
from itertools import combinations as cb
l=[1,2,3,4,5]
x=list(pt(l))
print(x)
y=list(cb(l,2))
print(y)