class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()
        def backtrack(i, cursum):
            if cursum == target: 
                res.append(cur.copy())
                return 
            if i >= len(candidates) or cursum > target: 
                return
            
            cur.append(candidates[i]) 
            backtrack(i+1, cursum+candidates[i])
            cur.pop()
            
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            backtrack(i+1, cursum) 
        
        backtrack(0,0)
        return res 
            