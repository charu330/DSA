# Lexicographically Smallest Palindrome
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        count=0
        l=0
        r=len(s)-1
        s_list = list(s)
        while(l<r):
            if(s_list[l]==s_list[r]):
                l+=1
                r-=1
            else:
                if(s_list[l]<s_list[r]):
                    s_list[r]=s_list[l]
                    l+=1
                    r-=1
                    count+=1
                else:
                    s_list[l]=s_list[r]
                    l+=1
                    r-=1
        s = "".join(s_list)
        return s        
