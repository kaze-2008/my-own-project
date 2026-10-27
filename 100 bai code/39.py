import math
a=int(input())
b=math.sqrt(a)
int_check=True
if int(b)**2!=a:
    int_check=False
if int_check==True:
    print("Yes")
else:
    print("No")