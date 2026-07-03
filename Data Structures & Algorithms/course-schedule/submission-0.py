class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites: 
            preMap[course].append(pre)
        def dfs(course):
            if not preMap[course]: 
                return True 
            if course in visited:
                return False 
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False 
            preMap[course] = []
            visited.remove(course)
            return True 

        for i in range(numCourses): 
            if not dfs(i): 
                return False

        return True 

