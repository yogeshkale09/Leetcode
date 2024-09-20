class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        for i in range(1, len(s)):
            if s[-i:][::-1]+s == (s[-i:][::-1]+s)[::-1]:
                return s[-i:][::-1]+s
        