# Longest Subarray of 1's After Deleting One Element (https://leetcode.com/problems/longest-subarray-of-1's-after-deleting-one-element/)
# Study Plan: LeetCode 75
# Category: Sliding Window
# Problem: Longest Subarray of 1's After Deleting One Element

class Solution:
  def longestSubarray(self, nums: list[int]) -> int:
    ans = 0
    zeros = 0

    l = 0
    for r, num in enumerate(nums):
      if num == 0:
        zeros += 1
      while zeros == 2:
        if nums[l] == 0:
          zeros -= 1
        l += 1
      ans = max(ans, r - l)

    return ans