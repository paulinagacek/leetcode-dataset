\'\'\'
https://leetcode.com/problems/valid-palindrome/submissions/
Runtime: 40 ms, faster than 98.66% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.2 MB, less than 9.52% of Python3 online submissions for Valid Palindrome.
\'\'\'
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]",\'\',s.lower())
        return s == \'\'.join(reversed(s))