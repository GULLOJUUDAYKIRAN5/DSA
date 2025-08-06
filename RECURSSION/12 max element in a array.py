def mai(i,s,maxi):
    if i==len(s):
        return maxi
    maxi=max(maxi,s[i])
    return mai(i+1,s,maxi)
maxi=0
print(mai(0,[1,2,3,4],maxi))
