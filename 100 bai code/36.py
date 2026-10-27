a,b=map(int,input().split())
A=[]
for k in range(1,a+1):
    if a%k==0:
        A.append(k)
A.reverse()
for k in A:
    if b%k==0:
        print(k)
        break
