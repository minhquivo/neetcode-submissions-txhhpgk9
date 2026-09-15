class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int) 
        for c in t: 
            t_map[c] += 1
        
        s_map = {}
        for key in t_map.keys(): 
            s_map[key] = 0 
        
        need = len(t_map) 
        have = 0 
        l, r = 0,0 
        shortest = len(s) + 1
        res = ""

        while r < len(s): 
            if s[r] in s_map: 
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]: 
                    have += 1 
            
            while have == need:  
                if r - l + 1 < shortest: 
                    shortest = r - l + 1
                    res = s[l:r+1] 
                
                if s[l] in s_map: 
                    s_map[s[l]] -= 1
                    if s_map[s[l]] < t_map[s[l]]: 
                        have -= 1
                    l += 1
                else: 
                    l += 1 

            r += 1

        if shortest == len(s) + 1: 
            return ""
        
        return res 
