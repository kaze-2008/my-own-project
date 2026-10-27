a=list(map(int,input().split()))
check=0
for k in a:
    if k == max(a):
        check+=1
if check ==3:
    print("=")
else:
    print(max(a))