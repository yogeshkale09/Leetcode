class Solution:
    def largestNumber(self, nums: List[int]) -> str:
         nums[:] = map(str, nums)
         nums.sort(key=NumCompare, reverse=True)
         return ''.join(nums).lstrip('0') or '0'

class NumCompare:
    def __init__(self, s: str):
        self.s = s
    def __lt__(self, other: str) -> bool:
        return self.s + other.s < other.s + self.s
        