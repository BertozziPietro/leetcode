# Container With Most Water (https://leetcode.com/problems/container-with-most-water/)
# Study Plan: LeetCode 75
# Category: Two Pointers
# Problem: Container With Most Water

class Solution:
  def maxArea(self, height: list[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      ans = max(ans, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return ans