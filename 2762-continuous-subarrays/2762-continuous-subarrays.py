class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def search(j, x, y):
            if j >= n:
                return 0
            xx = min(x, nums[j])
            yy = max(y, nums[j])
            if abs(xx - yy) <= 2:
                return 1 + search(j + 1, xx, yy)
            return 0
        ans = 0
        for i in range(n):
            ans += search(i, nums[i], nums[i])
        return ans
        