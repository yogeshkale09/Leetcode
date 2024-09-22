class Solution:
    # Helper function to count the steps from current prefix within range.
    def countSteps(self, curr: int, n: int) -> int:
        steps = 0
        first, last = curr, curr
        while first <= n:
            steps += min(n + 1, last + 1) - first
            first *= 10
            last = last * 10 + 9
        return steps
    
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1  # Start from the first prefix
        k -= 1  # Decrement k to make it zero-indexed
        
        while k > 0:
            steps = self.countSteps(curr, n)
            if steps <= k:
                curr += 1  # Move to the next prefix
                k -= steps
            else:
                curr *= 10  # Dive deeper into the current prefix
                k -= 1
        
        return curr
        