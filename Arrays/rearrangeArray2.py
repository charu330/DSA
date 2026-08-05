# 2149. Rearrange Array Elements by Sign

# with 1 pass and extra space


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Initialize an empty array of the same size
        res = [0] * len(nums)
        
        # Pointers for where the next positive and negative numbers should go
        pos_idx = 0
        neg_idx = 1
        
        for num in nums:
            if num > 0:
                res[pos_idx] = num
                pos_idx += 2  # Move to the next even index
            else:
                res[neg_idx] = num
                neg_idx += 2  # Move to the next odd index
                
        return res
