# Append Characters to String to Make Subsequence


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count=0
        max_count=0
        i=0
        j=0
        while(i<len(s) and j< len(t)):
            if(s[i]==t[j]):
                i+=1
                j+=1
            else:
                while(i<len(s) and s[i]!=t[j]):
                    i+=1
                if(i==len(s)):
                    break
        count=len(t)-j
        return count
            
            

        
