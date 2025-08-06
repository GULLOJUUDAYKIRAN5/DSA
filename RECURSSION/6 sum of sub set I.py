def subset(arr,i,s):
    if i>=len(arr):
        print(s)
        return
    subset(arr,i+1,s+arr[i])
    subset(arr,i+1,s)
arr=[3,1,4]
subset(arr,0,0)