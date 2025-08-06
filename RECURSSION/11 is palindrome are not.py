def pal(i,s):
    if i==0:
        return s[i]
    x=s[i]+pal(i-1,s)
    return x
s="xyy"
print(s==pal(len(s)-1,s))

