class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = {}
        w2 = {}
        if len(s) != len(t):
            return False
        counter = 0
        for i, j in zip(s, t):
            if i in w1:
                w1[i] += 1
            else:
                w1[i] = 1
            if j in w2:
                w2[j] += 1
            else:
                w2[j] = 1
        return w1 == w2


        