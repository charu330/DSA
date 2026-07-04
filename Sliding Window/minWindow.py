# 76. Minimum Window Substring



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        i = 0
        j = 0
        t_mp = dict()       # Map 1: Stores target counts from t
        window_mp = dict()  # Map 2: Stores current window counts from s
        
        count = 0           # Tracks unique characters fully satisfied
        index = -1
        minlen = float('inf')
        
        # 1. Populate Target Map (t_mp)
        for idx in range(len(t)):
            if t[idx] in t_mp:
                t_mp[t[idx]] += 1
            else:
                t_mp[t[idx]] = 1
                
        # Unique characters needed from t
        required = len(t_mp)
        
        # 2. Expand Window
        while j < len(s):
            char_j = s[j]
            if char_j in t_mp:
                window_mp[char_j] = window_mp.get(char_j, 0) + 1

                
                # If current window match matches target requirement exactly
                if window_mp[char_j] == t_mp[char_j]:
                    count += 1
            
            # 3. Shrink Window
            while count == required:
                minl = j - i + 1
                if minl < minlen:
                    minlen = minl
                    index = i
                
                char_i = s[i]
                if char_i in t_mp:
                    window_mp[char_i] -= 1
                    # If we fall below target requirements, we lose a matching unique character
                    if window_mp[char_i] < t_mp[char_i]:
                        count -= 1
                i += 1
            j += 1
            
        if index == -1:
            return ""
            
        return s[index : index + minlen]
