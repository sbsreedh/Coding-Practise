#TC:O(v+e)
#SC:O(v)

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        result=[]
        self.time=0
        graph=[[] for _ in range(n)]
        discovery=[-1]*n
        lower=[0]*n
        for e in connections:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        
        #dfs function
        def dfs(v,u,discovery,lower):
            if discovery[v]!=-1:
                return 
            discovery[v]=self.time
            lower[v]=self.time
            self.time+=1
            for n in graph[v]:
                if n==u:continue
                dfs(n,v,discovery,lower)
                if lower[n]>discovery[v]:
                    result.append([n,v])
                lower[v]=min(lower[n],lower[v])
        dfs(0,0,discovery,lower)
        return result

     
