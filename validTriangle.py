#TC:O(NlogN)
#SC:O(1)
# sort first
# In order to create a triangle, we could first select the longest edge.
# nums[i] as the longest edge
# Then we use two pointer(l,r) to determine if there has any solution
# if there is a pair of l, r is ok (nums[l]+ nums[r] > nums[i]), we increment the count r-l, cuz any new l which is bigger than old l and smaller than r is a solution.from itertools import permutations 
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            #2,2,3,4
            #l     r i
            l=0
            r=i-1
            while l<r:
                if nums[i]<nums[r]+nums[l]:
                    count+=r-l
                    r-=1
                    
                else:
                    
                    l+=1
        return count
                    
    
    
  

            
        
