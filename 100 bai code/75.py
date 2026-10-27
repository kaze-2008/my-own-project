a=input()
lst=a.split()
result=[]
for k in lst:
    b=list(k)
    b.reverse()
    b="".join(b)
    result.append(b)
print(" ".join(result))