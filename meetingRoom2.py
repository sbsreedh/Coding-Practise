TC:O(NlogN)
SC:O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        

        if not intervals: return 0
        
        intervals.sort()
        endTimes = [intervals[0][1]]
        
        for start, end in intervals[1:]:
            nextEnd = heapq.heappop(endTimes)
            if start < nextEnd:
                heapq.heappush(endTimes, nextEnd)
            heapq.heappush(endTimes, end)
        return len(endTimes)
