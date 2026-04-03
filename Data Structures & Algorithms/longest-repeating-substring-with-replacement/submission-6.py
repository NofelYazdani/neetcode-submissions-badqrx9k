class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0 
        for right, j in enumerate(s):
            if j in count:
                count[j] = count[j] + 1
            else:
                count[j] = 1
            while (right - left + 1) - max(count.values())  > k and right >= left:
                index = s[left]
                count[index] = count[index] - 1
                left = left + 1
            result = max(right - left + 1, result)
        return result

        