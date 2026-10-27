a,b=map(int,input().split())
lst=list(map(int,input().split()))
if b in lst:
    print("Yes")
    print(lst.index(b))
else:
    print("No")