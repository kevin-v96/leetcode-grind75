#https://leetcode.com/problems/majority-element/
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums)
        for key, value in counts.items():
            if value > n // 2:
                return key