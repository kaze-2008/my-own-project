a,b=map(float,input().split())
TBCN=(a+b*2)/3
if TBCN>=8:
    print(f"""{TBCN:.1f}
Gioi""")
elif TBCN >=6.5:
    print(f"""{TBCN:.1f}
Kha""")
elif TBCN >=5:
    print(f"""{TBCN:.1f}
TrungBinh""")
elif TBCN >=3.5:
    print(f"""{TBCN:.1f}
Yeu""")
else:
    print(f"""{TBCN:.1f}
kem""")