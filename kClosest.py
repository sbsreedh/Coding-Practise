import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def findDist(x,y):
            distance=0
            x1=0
            y1=0
            distance=pow((pow((x-x1),2)+pow((y-y1),2)),0.5)
            # print(distance)
            return (distance)
        res=[]
        heap=[]
        hashMap={}
        for point in points:
            distance=findDist(point[0],point[1])
            if distance not in hashMap:
                 hashMap[distance]=[]
                 hashMap[distance].append(point)
            else:
                hashMap[distance].append(point)
            
            heapq.heappush(heap,distance)
        print(hashMap)
        while len(res)<K:
            pt=heapq.heappop(heap)
            for i in range(len(hashMap[pt])):
                
                    res.append(hashMap[pt][i])
        return res
    
class Solution(object):
    def kClosest(self, points, K):
        l = [(-(p[0]*p[0]+p[1]*p[1]), p) for p in points]#O(nlogk)
        heapify(l)
        while len(l) > K:
            heappop(l)
        return [p[1] for p in l]
        
