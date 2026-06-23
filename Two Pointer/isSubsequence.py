# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while (i<len(t) and j<len(s)):
            if(s[j]==t[i]):
                j+=1
            i+=1
        if(j==len(s))  :
            return True
        else:
            return False

        
