class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        while r > l:
            if not s[r].isalnum():
                r = r - 1
            elif not s[l].isalnum():
                l = l + 1
            elif s[r].lower() == s[l].lower():
                r = r - 1
                l = l + 1
            else:
                return False
        return True

        