a=input()
b=input()
c=False
for k in range(len(a)-1,-1,-1):
    if a[k]==b:
        print(k)
        c=True
        break
if c==False:
    print("-1")
