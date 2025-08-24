# Increasing Triplet Subsequence (https://leetcode.com/problems/increasing-triplet-subsequence/)
# Study Plan: LeetCode 75
# Category: Array String
# Problem: Increasing Triplet Subsequence

import math

class Solution:
  def increasingTriplet(self, nums: list[int]) -> bool:
    first = math.inf
    second = math.inf

    for num in nums:
      if num <= first:
        first = num
      elif num <= second:  # first < num <= second
        second = num
      else:
        return True  # first < second < num (third)

    return False