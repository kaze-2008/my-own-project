a=input()
b=input()
try:
    location=a.index(b)
except Exception:
    location="-1"
print(location)
