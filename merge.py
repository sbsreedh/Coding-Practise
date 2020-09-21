#TC:O(NlogN)
#SC:O(N)-result

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
       
        start1=intervals[0][0]
        end1=intervals[0][1]
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            start1,end1=res[-1]
            start2,end2=intervals[i]
            if end1<start2:
                res.append(intervals[i])
            else:#end1>start2
                res[-1]=(start1,max(end1,end2))
        return res
            
