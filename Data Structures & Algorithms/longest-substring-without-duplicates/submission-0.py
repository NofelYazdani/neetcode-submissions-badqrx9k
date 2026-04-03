class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        left = 0
        best = 0
        curr = 0
        for i , j in enumerate(s):  
            while j in unique:
                del unique[s[left]]
                left = left + 1
            curr = i - left
            best = max(best, curr + 1)
            unique[j] = i
        return best



        