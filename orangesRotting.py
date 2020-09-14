class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        res=0
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        if fresh==0:
            return 0
        while q:
            dirs=[[0,1],[1,0],[-1,0],[0,-1]]
            size=len(q)
            for _ in range(size):
                curr=q.popleft()
                
                for dx,dy in dirs:
                    x=curr[0]+dx
                    y=curr[1]+dy
                    if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]==1:
                        fresh-=1
                        grid[x][y]=2
                        q.append((x,y))
            res+=1
        if fresh==0:
            return res-1
        return -1
            
                    
