class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        left = 0 
        maxf = 0 
        freq = defaultdict(int) 
        
        for right in range(len(s)):
            freq[s[right]] += 1
            maxf = max(maxf, freq[s[right]])

            while (right-left+1) - maxf > k: 
                freq[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)

        return res 