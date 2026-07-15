class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0]* len(height)
        suffix_max= [0]* len(height)

        premax = 0
        for i in range(1, len(height)):
            premax = max(premax, height[i-1])
            prefix_max[i] = premax
        suffmax = 0 
        for i in range(len(height)-2, -1, -1):
            suffmax = max(suffmax, height[i+1])
            suffix_max[i] = suffmax 
        
        res = 0
        for i in range(len(height)):
            cur = min(prefix_max[i], suffix_max[i])
            if cur - height[i] > 0: 
                res += cur - height[i]
        
        return res