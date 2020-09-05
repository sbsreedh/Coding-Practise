#TC:O(n)
#SC:O(n)
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap=defaultdict()
        for i in range(len(s)):
            if s[i] not in  hashMap:
                 hashMap[s[i]]=i
            else:
                hashMap[s[i]]=-1#make it -1 if it repeats 
        print(hashMap)
        min_=float("inf")
        for char in hashMap:
            if hashMap[char]>-1 and hashMap[char]<min_:#process only if it is not -1 and update min evertime you encounter min
                min_=hashMap[char]
          
        if min_==float("inf"):
            return -1
        else:
            return min_
        
#         index=-1
#         if not s:
#             return index
#         hashMap=defaultdict()
#         for i in range(len(s)):
#             if s[i] in hashMap:
#                 hashMap[s[i]]+=1
#             else:
#                 hashMap[s[i]]=1
        
#         for i in range(len(s)):
#             if hashMap[s[i]]==1:
#                 index=i
#                 break
#         return index
                
