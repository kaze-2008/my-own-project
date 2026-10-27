a,b=map(int,input().split())
if a==2:
    if b%4==0:
        print("29")
    else:
        print("28")
elif a in [1,3,5,7,8,10,12]:
    print("31")
else:
    print("30")