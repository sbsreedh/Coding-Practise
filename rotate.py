#Brute Force: To take last element and keep appending them to the first index of the array
#TC: O(nxk)
#SC:O(1)
#Using extra array and placing each element in its place a[(i%k)%len(arr)]=nums[i]
#TC:O(N),SC:O(N)
#Using reverse by n-k elements:
#TC:O(N),SC:O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r,nums):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
                l+=1
            print(nums)
            return nums
        n=len(nums)
        k%=len(nums)
        reverse(0,len(nums)-1,nums)
        reverse(0,k-1,nums)
        
        reverse(k,n-1,nums)
        
