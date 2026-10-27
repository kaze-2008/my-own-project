a,b,c=map(int,input().split())
def min(x,y):
    if x<y:
        return x
    else:
        return y
print(min(min(a,b),c))