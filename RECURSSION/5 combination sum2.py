def combi(arr,i,s,t,ans):
    if i==len(arr):
        if t==0:
            ans.add(tuple(s))
        return 
    if t>=arr[i]:
        combi(arr,i+1,s+[arr[i]],t-arr[i],ans)
    combi(arr,i+1,s,t,ans)
arr=[1,1,1,2,2]
t=4
s=[]
ans=set()
combi(arr,0,s,t,ans)
print(ans)

    
    