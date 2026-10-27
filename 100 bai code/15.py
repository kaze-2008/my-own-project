import math
a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    print("Day la 3 canh cua mot tam giac")
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"{a+b+c:.2f} {s:.1f}")
else:
    print("Day khong phai la 3 canh cua mot tam giac")