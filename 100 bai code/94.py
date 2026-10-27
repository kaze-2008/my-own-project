a,b=map(int,input().split())
c,d=map(int,input().split())
def UCLN(x,y):
    A=[]
    for k in range(1,x+1):
        if x%k==0:
            A.append(k)
    A.reverse()
    for k in A:
        if y%k==0:
            return k
def plus(x,y,z,w):
    tu=x*w+y*z
    mau=y*w
    if tu>mau:
        he_so=tu//mau
        tu=tu-he_so*mau
        print(f"{he_so},{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")
    else:
        print(f"{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")

def minus(x,y,z,w):
    tu=x*w-y*z
    mau=y*w
    if tu>mau:
        he_so=tu//mau
        tu=tu-he_so*mau
        print(f"{he_so},{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")
    else:
        print(f"{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")

def time(x,y,z,w):
    tu=x*z
    mau=y*w
    if tu>mau:
        he_so=tu//mau
        tu=tu-he_so*mau
        print(f"{he_so},{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")
    else:
        print(f"{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")

def devide(x,y,z,w):
    tu=x*w
    mau=y*z
    if tu>mau:
        he_so=tu//mau
        tu=tu-he_so*mau
        print(f"{he_so},{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")
    else:
        print(f"{tu/UCLN(tu,mau):.0f}/{mau/UCLN(tu,mau):.0f}")
plus(a,b,c,d)
minus(a,b,c,d)
time(a,b,c,d)
devide(a,b,c,d)