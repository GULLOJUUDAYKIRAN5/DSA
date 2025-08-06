def maze(arr,i,j,res):
  
    if i>len(arr)-1 or j>len(arr[0])-1:
        return
    res+=[[i,j]]
    if i==len(arr)-1 and j==len(arr[0])-1:
        print(res)
        return
     
    if arr[i][j]!=0:
        maze(arr,i+1,j,res)
        maze(arr,i,j+1,res)
    
arr=[
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1]
]
res=[]
maze(arr,0,0,res)