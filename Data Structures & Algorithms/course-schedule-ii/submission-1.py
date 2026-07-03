class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        res = [] 
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()
        done = set()
        def dfs(course): 
            if not preMap[course]: 
                if course not in done:                    
                    res.append(course)
                    done.add(course)
                return True 
            if course in visited: 
                return False
            
            visited.add(course)
            for pre in preMap[course]: 
                if not dfs(pre): 
                    return False 
            preMap[course] = [] 
            visited.remove(course)
            res.append(course)
            done.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res 
            