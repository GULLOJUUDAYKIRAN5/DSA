# SOLUTION TIME(O(N**2)) SPACE(O(N))
n=[1,4,7,3,2]
ans=[-1]*(len(n))
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]<n[j]:
#             ans[i]=n[j]
# print(ans)
# OPTIMAL
print(ans)
maxi=0
st=[]
for i in range(len(n)-1,-1,-1):
    if not st:
        st.append(n[i])
        
    else:
        while st and n[i]>st[-1]:
            st.pop()
        if st:
            ans[i]=st[-1]
            
st.append(n[i])
print(ans)
# st=[]
# ans=[-1]*len(nums1)
# if nums1:
#     st.append(nums1[-1])
# for i in range(len(nums1)-2,-1,-1):
#     while st and nums1[i]>st[-1]:
#         st.pop()
#     if st:
#         ans[i]=st[-1]
#     st.append(nums1[i])
# return ans
           

       





    

    
   
    
