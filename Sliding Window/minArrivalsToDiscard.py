# Minimum Discards to Balance Inventory

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        i=0
        j=0
        ls=[]
        count=0
        mp = dict()
        
        # Track whether the item at each index was kept (True) or discarded (False)
        kept = [False] * len(arrivals)
        
        while(j<len(arrivals)): 
            # Manually handle inserting/incrementing into the dictionary
            if arrivals[j] in mp:
                mp[arrivals[j]] += 1
            else:
                mp[arrivals[j]] = 1
                
            if(j-i+1<w):
                # If the item violates the threshold, discard it immediately
                if(mp[arrivals[j]]>m):
                    count+=1
                    mp[arrivals[j]] -= 1
                    # kept[j] remains False
                else:
                    kept[j] = True
                j+=1
                
            elif(j-i+1==w):
                if(mp[arrivals[j]]>m):
                    count+=1
                    mp[arrivals[j]] -= 1 
                    
                    # Slide the window: Only decrement the left item if it was kept
                    if kept[i]:
                        mp[arrivals[i]] -= 1 
                    i+=1                             
                else: 
                    kept[j] = True
                    # Slide the window: Only decrement the left item if it was kept
                    if kept[i]:
                        mp[arrivals[i]] -= 1 
                    i+=1
                j+=1
                
        return count
