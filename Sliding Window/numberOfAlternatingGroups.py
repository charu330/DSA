# Alternating Groups II

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        i = 0
        count = 0
        n = len(colors)
        
        # Loop through the logical circular extension (up to n + k - 2)
        for j in range(1, n + k - 1):
            # 1. If colors match, the alternating streak breaks. 
            # Move the start pointer 'i' to the current position 'j'.
            if colors[j % n] == colors[(j - 1) % n]:
                i = j
            
            # 2. If the current valid alternating window length reaches k, we found a group!
            if j - i + 1 == k:
                count += 1
                i += 1  # Slide the left pointer forward to maintain a maximum window size of k
                
        return count
