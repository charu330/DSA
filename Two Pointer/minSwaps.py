# Minimum Number of Swaps to Make the String Balanced
# Need to revise

class Solution:
    def minSwaps(self, s: str) -> int:
        
        count=0
        max_imbalance=0
        i=0
        while i in range(len(s)):
            if(s[i]==']'):
                count+=1
            else:
                count-=1
            i+=1
            max_imbalance = max(max_imbalance, count)
        
          
        return int((max_imbalance+1)/2)
