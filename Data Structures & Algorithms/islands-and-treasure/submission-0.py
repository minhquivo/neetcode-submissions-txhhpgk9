class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        step = 1
        while q: 
            for i in range(len(q)):
                r, c = q.popleft()
                directions = ((1,0),(0,1),(-1,0),(0,-1))
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc 
                    if 0<=nr<m and 0<=nc<n:
                        if grid[nr][nc] == INF: 
                            grid[nr][nc] = step
                            q.append((nr,nc))
            step += 1
        
        return None
