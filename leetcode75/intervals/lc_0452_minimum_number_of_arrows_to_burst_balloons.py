# Minimum Number of Arrows to Burst Balloons (https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
# Study Plan: LeetCode 75
# Category: Intervals
# Problem: Minimum Number of Arrows to Burst Balloons

import math

class Solution:
  def findMinArrowShots(self, points: list[list[int]]) -> int:
    ans = 0
    arrowX = -math.inf

    for point in sorted(points, key=lambda x: x[1]):
      if point[0] > arrowX:
        ans += 1
        arrowX = point[1]

    return ans