a,b,c=map(int,input().split())
def plus(x,y):
    return x+y
def devide(x,y):
    return x/y
print(f"{plus(a,b)+c} {devide(a,b)+c:.2f} {a/plus(b,c):.3f}")