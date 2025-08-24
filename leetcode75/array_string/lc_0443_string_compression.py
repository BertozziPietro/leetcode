# String Compression (https://leetcode.com/problems/string-compression/)
# Study Plan: LeetCode 75
# Category: Array String
# Problem: String Compression

class Solution:
  def compress(self, chars: list[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans