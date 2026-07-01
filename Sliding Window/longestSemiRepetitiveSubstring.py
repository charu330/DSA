# Find the Longest Semi-Repetitive Substring

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        i=0
        j=0
        count=1
        maxlen=1
        for j in range(1, len(s)):
            if(s[j]==s[j-1]):
                count+=1
            if(count<=2):
                maxl=j-i+1
                maxlen=max(maxlen, maxl)
                j+=1
            elif(count>2):
                while(count>2):
                    if(s[i]==s[i+1]):
                        count-=1
                    
                    i+=1
                j+=1
        return maxlen
        
