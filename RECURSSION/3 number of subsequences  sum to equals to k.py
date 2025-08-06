def count(arr,i,k,s):
    if i==len(arr):
        if s==k:
            return 1
        else:
            return 0
    l=count(arr,i+1,k,s+arr[i])
    r=count(arr,i+1,k,s)
    return l+r
    








arr=[1,1,2]
k=2
print(count(arr,0,k,0))