# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        count=0
        l=0
        r=len(s)-1
        while(l<r):
            if(s[l]==s[r]):
                l+=1
                r-=1
            else:
                if self.ispalindrome(s[l+1 : r+1]) or self.ispalindrome(s[l : r]):
                    return True
                else:
                    return False
        return True
       
    def ispalindrome(self, s:str) -> bool:
        l=0
        r=len(s)-1
        if(len(s)==1):
            return True
        while(l<r):
            if(s[l]==s[r]):
                l+=1
                r-=1
            else:
                return False
        return True
            
