#https://leetcode.com/problems/longest-palindrome/
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        for key, value in counts.items():
            length += value - (value % 2)
            counts[key] = value % 2
        
        if any(counts.values()):
            length += 1

        return length 