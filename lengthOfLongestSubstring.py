#TC:O(N)
#SC:O(N)

#Create hasmap with char:index of occurence(not a list, only latest index)
# if the char exists already, update i pointer. 
# else add to hasmap with its respective index
#keep calculating length as j-i+1 and keep a track of max length found.
#return max length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        myset=defaultdict()
        maxlen=0
        i=0
        for j in range(0,len(s)):
                if  s[j] in myset:
                    i=max(myset[s[j]],i)
                maxlen=max(maxlen,j-i+1) 
                myset[s[j]]=j+1
        print(myset)
        return maxlen
                    
          
