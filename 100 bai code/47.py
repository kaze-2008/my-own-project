a=int(input())
lst=list(map(int,input().split()))
plus=0
Plus=[]
minus=0
Minus=[]
for k in lst:
    if k >0:
        plus+=1
        Plus.append(k)
    else:
        minus+=1
        Minus.append(k)
print(f"{plus} {minus}")
for k in Plus:
    print(k,end=" ")
print(" ")
for k in Minus:
    print(k,end=" ")