# Find Pivot Index (https://leetcode.com/problems/find-pivot-index/)
# Study Plan: LeetCode 75
# Category: Prefix Sum
# Problem: Find Pivot Index

class Solution:
  def pivotIndex(self, nums: list[int]) -> int:
    summ = sum(nums)
    prefix = 0

    for i, num in enumerate(nums):
      if prefix == summ - prefix - num:
        return i
      prefix += num

    return -1