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
    
#heap Solution:
#TC:O(Nlogk), N-elements, k elements in heap
#SC:O(N)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #initialize a max heap
        #create counter dict to store freq of words
        #iterate through the counter and add with  -count and keys
        #pop from heap till k elements
        heap=[]
        count=collections.Counter(words)
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        return [heapq.heappop(heap)[1] for _ in range(k)]
     
#        
        
