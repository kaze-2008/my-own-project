a=int(input())
if a<=1:
    Tien=a*12000
elif a<=30:
    Tien=1*12000 + (a-1)*10000
else:
    Tien=1*12000 + 29*10000 + (a-30)*9000
print(Tien)