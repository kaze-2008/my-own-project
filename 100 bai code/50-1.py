a=int(input())
lst=list(map(int,input().split()))
lst.sort()
for k in lst:
    print(k,end=" ")