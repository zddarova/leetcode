#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (65.33%)
# Likes:    16469
# Dislikes: 1146
# Total Accepted:    5.1M
# Total Submissions: 7.9M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
#
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
#
# Example 2:
#
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 3:
#
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
#
#

# @lc code=start
from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntMap: Dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        subtractFromMap: Dict[str, list[str]] = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"],
        }
        result = 0
        i = 0

        while i < len(s):
            currentItem: str = s[i]
            mappedInt: int = romanToIntMap[currentItem]
            subtractFrom: list[str] | None = subtractFromMap.get(currentItem)
            isLastItem = i == len(s) - 1
            if subtractFrom == None or isLastItem:
                result += mappedInt
                i += 1
                continue
            else:
                nextItem: str = s[i + 1]
                if nextItem not in subtractFrom:
                    result += mappedInt
                    i += 1
                    continue
                else:
                    c: int = romanToIntMap[currentItem]
                    n: int = romanToIntMap[nextItem]
                    d: int = n - c
                    result += d
                    i += 2
                    continue

        return result


# @lc code=end


# assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("MCMXCIV") == 1994
