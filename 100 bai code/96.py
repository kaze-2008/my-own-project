a=int(input())
b=list(map(int,input().split()))
def sum_even(x):
    sm=0
    for k in x:
        if k%2==0:
            sm+=k
    return sm
def count_even(x):
    sm=0
    for k in x:
        if k%2==0:
            sm+=1
    return sm
print(f"{sum_even(b)/count_even(b):.2f}")