# Maximum Average Subarray I (https://leetcode.com/problems/maximum-average-subarray-i/)
# Study Plan: LeetCode 75
# Category: Sliding Window
# Problem: Maximum Average Subarray I

class Solution:
  def findMaxAverage(self, nums: list[int], k: int) -> float:
    summ = sum(nums[:k])
    ans = summ

    for i in range(k, len(nums)):
      summ += nums[i] - nums[i - k]
      ans = max(ans, summ)

    return ans / k