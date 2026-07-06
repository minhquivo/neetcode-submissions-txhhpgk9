class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()

        def dfs(i, prev): 
            if i in visited: 
                return False 
            visited.add(i)
            for j in adj[i]: 
                if j == prev: 
                    continue 
                if not dfs(j, i):
                    return False
            return True 
        
        if not dfs(0,-1): 
            return False
        if len(visited) != n: 
            return False

        return True 