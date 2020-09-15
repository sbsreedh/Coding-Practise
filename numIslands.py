class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate thru all elements
        count=0
        def helper(i,j):
            
            dirs=[[0,1],[0,-1],[1,0],[-1,0]]
            
                
            grid[i][j]="2"
            # print(grid)
            for dx,dy in dirs:
                x=dx+i
                y=dy+j
                if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]=="1":
                    
                     helper(x,y)
        


            # return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    helper(i,j)
        return count
