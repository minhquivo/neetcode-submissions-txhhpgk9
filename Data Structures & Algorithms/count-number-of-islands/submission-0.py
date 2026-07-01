class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def bfs(start_r, start_c): 
            q = deque()
            visited[start_r][start_c] = True 
            q.append((start_r, start_c)) 
            
            directions = ((1,0),(0,1),(-1,0),(0,-1))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc 
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] =='1' and not visited[nr][nc]: 
                        visited[nr][nc] = True 
                        q.append((nr,nc))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    res += 1 

        return res 


            