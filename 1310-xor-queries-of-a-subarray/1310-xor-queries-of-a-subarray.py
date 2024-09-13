class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr = list(accumulate(arr, xor, initial = 0))
        return [arr[l]^arr[r+1] for l,r in queries]
        