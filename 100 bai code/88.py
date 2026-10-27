a,b=map(int,input().split())
def UCLN(a,b):
    A=[]
    for k in range(1,a+1):
        if a%k==0:
            A.append(k)
    A.reverse()
    for k in A:
        if b%k==0:
            return k
print(f"{a/UCLN(a,b):.0f}/{b/UCLN(a,b):.0f}")