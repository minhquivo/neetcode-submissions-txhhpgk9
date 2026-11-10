class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n 

        def find(node): 
            if node != par[node]: 
                par[node] = find(par[node])
            
            return par[node] 
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if p1 != p2: 
                if rank[p1] >= rank[p2]: 
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else: 
                    par[p1] = p2
                    rank[p2] += rank[p1] 

        for node1, node2 in edges: 
            union(node1, node2) 
        
        count = 0
        for node in range(n): 
            if par[node] == node:
                count += 1
        
        return count 