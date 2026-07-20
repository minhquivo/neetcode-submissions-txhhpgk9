class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for nodeA, nodeB in edges:
            adj[nodeA].append(nodeB)
            adj[nodeB].append(nodeA)
        
        visited = set()

        def dfs(node, parent):
            if node in visited: 
                return False 
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue 
                if not dfs(neighbor, node):
                    return False
            return True 
            

        if not dfs(0, -1):
            return False
        if len(visited) != n:
            return False
        
        return True 
            