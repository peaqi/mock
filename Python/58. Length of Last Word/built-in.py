class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        if len(s) == 1:
            return len(s[0])
        return len(s[-1])
        #O(n), O(1)