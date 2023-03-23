#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverseDict = {}
        for idx, num in enumerate(nums):
            residue = target - num
            if residue in reverseDict:
                return [reverseDict[residue], idx]
            reverseDict[num] = idx