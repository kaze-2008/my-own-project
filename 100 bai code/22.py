a=int(input())
if a<=50:
    Tien=a*600
elif a<=100:
    Tien=50*600 + (a-50)*800
elif a<=200:
    Tien=50*600 + 50*800 + (a-100)*1100
else:
    Tien=50*600 + 50*800 + 100*1100 + (a-200)*1500
print(Tien)