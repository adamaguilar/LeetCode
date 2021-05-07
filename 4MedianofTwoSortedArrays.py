'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        median = 0
        nums = []
        while nums1 or nums2:
            if not nums2:
                nums.append(nums1[0])
                nums1.pop(0)
            elif not nums1:
                nums.append(nums2[0])
                nums2.pop(0)
            elif nums1[0] < nums2[0]:
                nums.append(nums1[0])
                nums1.pop(0)
            else:
                nums.append(nums2[0])
                nums2.pop(0)
        if len(nums) % 2 == 0:
            median = (nums[(len(nums) // 2) - 1] + nums[len(nums) // 2]) / 2
        else:
            median = nums[len(nums) // 2]
        return median
        
print(Solution.findMedianSortedArrays("test", [], [2, 3]))