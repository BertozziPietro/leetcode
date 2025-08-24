# Kids With the Greatest Number of Cies (https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
# Study Plan: LeetCode 75
# Category: Array String
# Problem: Kids With the Greatest Number of Candies

class Solution:
  def kidsWithCandies(
      self,
      candies: list[int],
      extraCandies: int,
  ) -> list[bool]:
    maxCandy = max(candies)
    return [candy + extraCandies >= maxCandy for candy in candies]