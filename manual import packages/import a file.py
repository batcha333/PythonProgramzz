import math_sum
import math_diff
import math_product
import math_division
user=int(input("choice:"))
if user==1:
    print(math_sum.sum())
elif user==2:
    print(math_diff.diff())
elif user==3:
    print(math_product.product())
elif user==4:
    print(math_division.division())