class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) == 1: return 1
        dp = [0]*len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2': return 0
                if i - 2 < 0: dp[i] = 1
                else: dp[i] = dp[i-2]
            
            elif s[i] != '0':
                if s[i-1] != '0' and int(s[i-1:i+1]) <= 26: 
                    if i - 2 < 0: 
                        dp[i] = 2
                    else: 
                        dp[i] = dp[i-1] + dp[i-2]
                else: 
                    dp[i] = dp[i-1] 
        
        print(dp)
        return dp[-1] 