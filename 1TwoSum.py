'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in range(len(nums)):
            num2 = num + 1
            while num2 < len(nums):
                result = nums[num] + nums[num2]
                if result == target:
                    return [num, num2]
                num2 = num2 + 1

print(Solution().twoSum([2, 7, 11, 15], 9))