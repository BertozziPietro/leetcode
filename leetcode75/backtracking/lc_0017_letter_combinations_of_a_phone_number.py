# Letter Combinations of a Phone Number (https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
# Study Plan: LeetCode 75
# Category: Backtracking
# Problem: Letter Combinations of a Phone Number

class Solution:
  def letterCombinations(self, digits: str) -> list[str]:
    if not digits:
      return []

    digitToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []

    def dfs(i: int, path: list[str]) -> None:
      if i == len(digits):
        ans.append(''.join(path))
        return

      for letter in digitToLetters[int(digits[i])]:
        path.append(letter)
        dfs(i + 1, path)
        path.pop()

    dfs(0, [])
    return ans