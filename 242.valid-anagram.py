#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (67.04%)
# Likes:    13439
# Dislikes: 450
# Total Accepted:    5.2M
# Total Submissions: 7.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start
from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        entriesCount: Dict[str, int] = {}

        for i in range(len(s)):
            a: str = s[i]
            count: int | None = entriesCount.get(a)
            if count == None:
                entriesCount[a] = 1
            else:
                entriesCount[a] = entriesCount[a] + 1

        for i in range(len(t)):
            a = t[i]
            count = entriesCount.get(a)
            if count == None:
                return False
            elif count > 0:
                entriesCount[a] = entriesCount[a] - 1
                if entriesCount[a] == 0:
                    entriesCount.pop(a)

        return len(entriesCount) == 0


# @lc code=end
