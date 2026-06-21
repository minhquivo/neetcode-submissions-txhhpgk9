class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = [] 
        visited = [False] * len(nums)

        def backtrack(): 
            if len(cur) == len(nums): 
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] == False: 
                    visited[i] = True 
                    cur.append(nums[i])
                    backtrack()
                    cur.pop()
                    visited[i] = False
        
        backtrack()

        return res 