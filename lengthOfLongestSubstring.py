#TC:O(N)
#SC:O(N)

#Create hasmap with char:index of occurence(not a list, only latest index)
# if the char exists already, update i pointer. 
# else add to hasmap with its respective index
#keep calculating length as j-i+1 and keep a track of max length found.
#return max length


#TC:O(n)
#SC:O((m)),m-#unique character in string
#Normal sliding window:Using two pointers.use a slding window to check unique strinngs by storing the character in a hasset, if the char repeats remove them form set, and increment i. 
#TC:O(2n)
#SC:O(n)


#Sliding window optmised
#TC:O(n)
#SC:O((m)),m-#unique character in string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         if not s:
                return 0
         i=0
         maxlen=float("-inf")
         hashMap=defaultdict(int)
         for j in range(len(s)):
            if s[j] in hashMap:
                i=max(hashMap[s[j]],i)
            maxlen=max(maxlen,j-i+1)
            hashMap[s[j]]=j+1
         print(hashMap)
         return maxlen
        
    
            
            
            
           
