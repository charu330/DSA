class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        if k == 0:
            return [0] * n
            
        # Define the initial window boundaries
        if k > 0:
            start, end = 1, k
        else:
            start, end = n + k, n - 1
            
        # Sum the initial window
        window_sum = sum(code[i % n] for i in range(start, end + 1))
        result = []
        
        # Slide the window across the array
        for i in range(n):
            result.append(window_sum)
            
            # Slide the window forward by 1 position
            window_sum -= code[start % n]  # Remove old start
            start += 1
            end += 1
            window_sum += code[end % n]    # Add new end
            
        return result