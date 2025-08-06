def find(arr,t,res,i):
    if i==len(arr):
        if t==0:
            print(res)
        return
    if arr[i]<=t:
        find(arr,t-arr[i],res+[arr[i]],i)
    find(arr,t,res,i+1)






arr=[2,3,6,7]
tar=7
find(arr,tar,[],0)