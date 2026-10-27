a=int(input())
b=list(map(int,input().split()))
def max(x):
    m=x[0]
    M=[]
    for k in range(len(x)):
        if m<x[k]:
            m=x[k]
            M.clear()
            M.append(k)
        elif m==x[k]:
            M.append(k)
    M.insert(0,m)
    return M

def min(x):
    m=x[0]
    M=[]
    for k in range(len(x)):
        if m>x[k]:
            m=x[k]
            M.clear()
            M.append(k)
        elif m==x[k]:
            M.append(k)
    M.insert(0,m)
    return M
for k in max(b):
    print(k,end=" ")
print("")
for k in min(b):
    print(k,end=" ")