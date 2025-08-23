# Find the Highest Altitude (https://leetcode.com/problems/find-the-highest-altitude/)
# Study Plan: LeetCode 75
# Category: Prefix Sum
# Problem: Find the Highest Altitude

class Solution:
  def largestAltitude(self, gain: list[int]) -> int:
    ans = 0
    currAltitude = 0
    for g in gain:
      currAltitude += g
      ans = max(ans, currAltitude)
    return ans