"""LeetCode Problem 1"""
"""
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution1(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    preMap = {} # value : index
        n = len(nums)
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in preMap:
                return [preMap[diff], i]
            preMap[num] = i
        return []  

class Solution2(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
        for i, num in enumerate(nums):
            for j in range(i + 1, n):
                if num + nums[j] == target:
                    return [i, j]
        return []     


class Solution3(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
