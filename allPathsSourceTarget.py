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
    #backtrack solution
   
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
            q=deque()
            results=[]
            if graph:
                q.append(0)
            target=len(graph)-1
            def dfs(n,q):
                if n ==target:
                    results.append(list(q))
                for x in graph[n]:
                    
                    q.append(x)
                    dfs(x,q)
                    q.pop()
            dfs(0,q)
            return results
                       
