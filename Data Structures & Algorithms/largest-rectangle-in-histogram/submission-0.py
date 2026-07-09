class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0 
        for idx, height in enumerate(heights): 
            start = idx
            while stack: 
                top_idx, top_height = stack[-1]
                if top_height > height: 
                    stack.pop() 
                    res = max(res, (idx-top_idx)*top_height)
                    start = top_idx
                else: break 
            stack.append((start, height))
        
        while stack: 
            idx, height = stack.pop()
            res = max(res, (len(heights) - idx) * height)
        return res 
