def square():
    a,b=map(int,input().split())
    print("*"*a)
    c=b-2
    for k in range(c):
        print(f"{"*"}{" "*(a-2)}{"*"}")
    print("*"*a)
square()