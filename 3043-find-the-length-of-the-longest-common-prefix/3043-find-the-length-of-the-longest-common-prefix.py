class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def findCommonPrefixLength(x, y):
            common_prefix_length = 0
            min_length = min(len(x), len(y))

            for i in range(min_length):
                if x[i] == y[i]:
                    common_prefix_length += 1
                else:
                    break

            return common_prefix_length

        a = [str(x) for x in arr1]
        b = [str(x) for x in arr2]
        
        a.sort()
        b.sort()
        
        ans = 0
        n = len(a)
        for i in range(len(b)):
            idx = bisect_left(a, b[i])
            if idx < n:
                ans = max(ans, findCommonPrefixLength(a[idx], b[i]))
            if idx > 0:
                ans = max(ans, findCommonPrefixLength(a[idx - 1], b[i]))
        return ans

        