memo={}
def rob(i,nums):
    if i>=len(nums):
        return 0
    if i in memo:
        return memo[i]
    memo[i]= max(rob(i+1,nums),nums[i]+rob(i+2,nums))
    return memo[i]
return rob(0,nums)
nums[1,2,3,4]
return rob(0,nums)


        