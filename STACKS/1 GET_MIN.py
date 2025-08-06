# OPTIMAL TIME(O(1)) SPACE (O(2*N))
n=[1,2,-1,4,5]
st=[]
def get_min(x,y):
    if x<y:
        return x
    else:
        return y

for i in n:
    if not st:
        st.append((i,i))
    else:
        st.append((i,get_min(i,st[-1][1])))

print(st[-1][1])
# BETTER