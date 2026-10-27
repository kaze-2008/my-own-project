a=int(input())
lst=list(map(int,input().split()))
st=[]
for k in lst:
    if len(st)==0:
        st.append(k)
    else:
        for i in range(len(st)):
            if k<=st[i]:
                st.insert(i,k)
                break
            elif i==len(st)-1:
                st.append(k)
for k in st:
    print(k, end=" ")