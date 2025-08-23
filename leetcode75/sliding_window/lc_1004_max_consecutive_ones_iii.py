# Max Consecutive Ones III (https://leetcode.com/problems/max-consecutive-ones-iii/)
# Study Plan: LeetCode 75
# Category: Sliding Window
# Problem: Max Consecutive Ones III

class Solution:
  def longestOnes(self, nums: list[int], k: int) -> int:

    ans = 0
    l = 0

    for r, num in enumerate(nums):
      if num == 0:
        k -= 1
      while k < 0:
        if nums[l] == 0:
          k += 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans