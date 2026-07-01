class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0 
        visited = [[False] * n for _ in range(m)]

        def bfs(r,c): 
            area = 1
            q = deque() 
            visited[r][c] = True 
            q.append((r,c))
            
            directions = ((1,0),(0,1),(-1,0),(0,-1))
            while q: 
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1 and not visited[nr][nc]:
                        q.append((nr,nc))
                        visited[nr][nc] = True
                        area += 1
            
            return area 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, bfs(i,j))
        
        return res 