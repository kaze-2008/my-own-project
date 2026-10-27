a=list(map(int,input().split()))
def count_element(x):
    element=0
    for k in x:
        lst=0
        for i in range(1,k+1):
            if k%i==0:
                lst+=1
        if lst==2:
            element+=1
    return element
print(count_element(a))