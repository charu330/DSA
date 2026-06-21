#2109. Adding Spaces to a String

#You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        leng=len(spaces) + len(s)
        new_s = s.rjust(leng)
        i=0
        j=0
        res=[]
        
        while (i<len(s)):
            if(j<len(spaces) and i == spaces[j]):
                res.append(" ")
                j+=1
            
            res.append(s[i])
            i+=1
        return "".join(res)
