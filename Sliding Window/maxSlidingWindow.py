# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = 0
        resl = []
        dq = deque()  # Stores INDICES instead of values
        
        while(j < len(nums)):
            # 1. Maintain monotonic property: remove smaller elements from back
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
                
            dq.append(j)
            
            if(j - i + 1 < k):
                j += 1
            elif(j - i + 1 == k):
                # 2. The front of the deque always holds the index of the maximum
                resl.append(nums[dq[0]])
                
                # 3. Slide the window: if the max element is leaving the window, pop it
                if dq[0] == i:
                    dq.popleft()
                    
                i += 1
                j += 1
                
        return resl
