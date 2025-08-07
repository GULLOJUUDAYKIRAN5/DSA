
# better solution
dic={}
nums=[1,2,3,4,5]
k=5
curr=leni=0
for i in range(len(nums)):
    curr+=nums[i]
    if curr==k:
        leni=max(leni,i+1)
    if curr-k in dic:
        leni=max(leni,i-dic[curr-k])
    if curr not in dic:
        dic[curr]=i
print(leni)