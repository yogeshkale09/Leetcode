class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        cnt = [float('inf')] * 32 # idx 0 to 31
        mask = maxval = 0 
        for i, c in enumerate(s):
            if c in m:
                mask ^= 1 << m[c] # update bit mask
                cnt[mask] = min(cnt[mask], i) # remember of leftmost index for same mask
            maxval = max(maxval, i + 1) if mask == 0 else max(maxval, i - cnt[mask]) 
                
        return maxval

        