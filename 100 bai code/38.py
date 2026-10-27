a=int(input())
k=1
lst=[]
while True:
    check=0
    for i in range(1,k+1):
        if k%i==0:
            check+=1
    if check==2:
        lst.append(k)
        print(k,end=" ")
    k+=1
    if len(lst)==a:
        break