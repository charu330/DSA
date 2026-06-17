# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0;
        r=len(s)-1
        lowertext=s.lower()
        while (l<r):
            if(not lowertext[l].isalnum()):
                l+=1
            elif(not lowertext[r].isalnum()):
                r-=1
            else:
                if(lowertext[l]!=lowertext[r]):
                    return False
                l+=1
                r-=1
                
        return True
        
