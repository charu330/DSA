# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        max_len=1
        if len(s)==0:
            return 0
        while(j<len(s)):
            new_s=s[i:(j+1)]
            if(len(new_s)==len(set(new_s))):
                maxlen=j-i+1
                max_len= max(max_len, maxlen)
                j+=1
            elif(len(new_s)>len(set(new_s))):
                while(len(new_s)>len(set(new_s))):
                    i+=1
                    new_s=s[i:j+1]
                j+=1                
        return max_len



        
