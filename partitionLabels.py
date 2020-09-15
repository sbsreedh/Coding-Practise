#TC:O(N)
#SC:O(1),only 26 letters can occur

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #write hashmap with last index of each letter.
        #set start and end 
        hashMap={}
        result=[]
        for idx,x in enumerate(S):
            hashMap[x]=idx
        end=0
        start=0
        for i in range(len(S)):
            end=max(end,hashMap[S[i]])
            if end==i:
                result.append(end-start+1)
                start=end+1
        return result
