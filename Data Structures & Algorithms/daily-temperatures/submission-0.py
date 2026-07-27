class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n 
        stack = [] 

        stack.append(0)
        for i in range(1, n): 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()  
            stack.append(i) 
        
        return res 