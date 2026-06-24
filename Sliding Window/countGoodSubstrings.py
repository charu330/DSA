# Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i=0
        j=0
        count=0
        k=3
        while (j<len(s)):
            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                new_s=s[i:(j+1)]
                if(len(new_s)==len(set(new_s))):
                    count+=1
                j+=1
                i+=1
        return count
        
