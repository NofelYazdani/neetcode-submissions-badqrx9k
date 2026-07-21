class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        charset = set()
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[left])
                left = left + 1
            charset.add(s[i])
            res = max(res, i - left + 1)
        return res



        