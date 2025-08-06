s="abc"
result=[]
def subb(st,path):
    result.append(path)
    for i in range(st,len(s)):
        subb(i+1,path+s[i])
subb(0,"")
print(result)
