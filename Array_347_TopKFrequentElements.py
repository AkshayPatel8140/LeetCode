"""LeetCode Problem 347"""
"""
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prelist = {}
        res = []
        lis = []

        for i, n in enumerate(nums):
            if n in prelist:
                prelist[n] += 1  
            else:
                prelist[n] = 1  
        for i in prelist.values():
            lis.append(i)
        lis.sort()
        lis=lis[-k:]
        for i in lis[:k]:
            for j in prelist:
                if prelist[j]==i and j not in res:
                    res.append(j)
        return res
        
