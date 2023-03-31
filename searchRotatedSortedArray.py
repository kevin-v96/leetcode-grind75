#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            
            if curr < nums[right]:
                if curr < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < curr:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1