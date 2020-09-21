#TC:O(N)
#SC:O(N)
#1.Create a hashmap with {nums[i]:i}
#2.Search in the hashmap fo rthe complement (target-nums[i]) and ensure it is no tthe same num and return the answer.

#One pass solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        hashMap=defaultdict(int)
        for i in range(len(nums)):
            hashMap[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in hashMap and hashMap[target-nums[i]]!=i:
                return (i,hashMap[target-nums[i]])
                
       
            
