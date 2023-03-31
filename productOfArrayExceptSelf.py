#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product = [1] * length
        prefix = 1
        postfix = 1

        for i in range(length):
            product[i] *= prefix
            prefix = prefix * nums[i]
            product[length - i - 1] *= postfix
            postfix = postfix * nums[length - i - 1]

        return product