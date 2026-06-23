
# Given an input string s, reverse the order of the words.

class Solution:
    def reverseWords(self, s: str) -> str:
        text=s.split()
        reverse= text[::-1]
        result= " ".join(reverse)
        return result

        
