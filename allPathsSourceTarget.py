#TC:O(v+e)
#SC:O(e)

#Iterative Solution:

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q=deque()
        if graph:
            q.append([0])
        target=len(graph)-1
        # print(target)
        result=[]
        while q:
            print(q)
            pathlen=len(q)
            for _ in range(pathlen):
                curr=q.popleft()
                lastNode=curr[-1]
                for n in graph[lastNode]:
                    if n==target:
                        result.append(curr+[n])
                    else:
                        q.append(curr+[n])
        return result
                       
