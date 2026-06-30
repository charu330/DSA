# Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=0
        j=0
        count=0
        mp=dict()
        maxlen=1
        while(j<len(fruits)):

            if fruits[j] not in mp:
                mp[fruits[j]] = 1  # Insert it with a count of 1
            else:
                mp[fruits[j]] += 1 

            if(len(mp)<2):
                maxl=j-i+1
                maxlen=max(maxl, maxlen)
                j+=1
            elif(len(mp)==2):
                maxl=j-i+1
                maxlen=max(maxl, maxlen)
                j+=1

            elif(len(mp)>2):
                while(len(mp)>2):
                    mp[fruits[i]]-=1
                    if(mp[fruits[i]]==0):
                        del mp[fruits[i]]
                    i+=1
                j+=1
            
        return maxlen

        
