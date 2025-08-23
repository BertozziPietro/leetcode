# Max Number of K-Sum Pairs (https://leetcode.com/problems/max-number-of-k-sum-pairs/)
# Study Plan: LeetCode 75
# Category: Two Pointers
# Problem: Max Number of K-Sum Pairs

import collections

class Solution:
  def maxOperations(self, nums: list[int], k: int) -> int:
    count = collections.Counter(nums)
    return sum(min(count[num], count[k - num])
               for num in count) // 2