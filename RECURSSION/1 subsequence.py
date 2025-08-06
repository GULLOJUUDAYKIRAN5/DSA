def subseq(arr,i,res):
    if i>=len(arr):
        print(res)
        return
    subseq(arr,i+1,res+[arr[i]])
    subseq(arr,i+1,res)
# hi
    
    




arr=[1,2,3]

subseq(arr,0,[])