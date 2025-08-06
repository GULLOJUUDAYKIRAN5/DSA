n=int(input("enter cost of 2 packs"))
m=int(input("enter cost of 4 packs"))
k=int(input("to noof cans to brought"))
def subb(tot,ans,k,maxi):
    if ans>=tot:
        # print(k)
        f=0
        for i in k:
            if i==2:
                f+=n
            else:
                f+=m
        if maxi>f:
            maxi=f

        return maxi
    x,y=9999,9999
    # if ans+2<=tot:
    x=subb(tot,ans+2,k+[2],maxi)
    # if ans+4<=tot:
    y=subb(tot,ans+4,k+[4],maxi)
    return min(x,y)
print(subb(k,0,[],9999))