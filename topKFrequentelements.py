#TC:O(Nlogk)
#SC:O(N)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count=collections.Counter(nums)
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        return [heapq.heappop(heap)[1] for _ in range(k)]
