#TC:O(NlogN)-sort+freq count
#SC:O(N)-hashMap
#Sorting Solution:
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #inti hashmap{word:count/freq}
        #iterate thru the list, count the freq add it ot hashmap
        #return the k words with high freq
        hashMap=defaultdict()
        res=[]
        for word in words:
            if word not in hashMap:
                hashMap[word]=1
            else:
                hashMap[word]+=1
      
        sorted_arr=sorted(hashMap.keys(),key=lambda x:(-hashMap[x],x))
        print(sorted_arr)
        return sorted_arr[:k]
        
