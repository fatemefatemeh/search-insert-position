class Solution:
    def searchInsert(self,nums,target):
       nums.append(target)
       return sorted(nums).index(target)
    
       
s=Solution()
print(s.searchInsert(nums=[1,3,5,6],target=7))