a=input()
b=sum(int(k) for k in a)%10
if b==9:
    print("may man")
else:
    print("chua may man")