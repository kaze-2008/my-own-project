a=int(input())
lst=list(map(int,input().split()))
print(f"{max(lst)} {lst.index(max(lst))}")