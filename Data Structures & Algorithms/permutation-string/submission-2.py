class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1, d2 = [0] * 26, [0] * 26
        k = len(s1)
        m = len(s2)
        for i in (s1):
            d1[ord(i) - ord('a')] += 1
        for i in range(len(s1)):
            d2[ord(s2[i]) - ord('a')] += 1
        if d1 == d2:

            return True
        for i in range(k, m):
            d2[ord(s2[i]) - ord('a')] += 1
            d2[ord(s2[i - k]) - ord('a')] -= 1
            if d1 == d2:
                return True
        return False
            



            





        