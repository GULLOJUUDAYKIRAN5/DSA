def sumi(arr,k,res,i):
    if i==len(arr):
        if sum(res)==k:
            print(res)
        return
    
    sumi(arr,k,res+[arr[i]],i+1)
    sumi(arr,k,res,i+1)







k=2
arr=[1,2,1]
sumi(arr,k,[],0)