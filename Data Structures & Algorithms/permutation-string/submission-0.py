class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge cases
        if not s1:
            return True
        if len(s1) > len(s2):
            return False

        # frequency needed from s1
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        remaining = len(s1)   # how many chars from s1 still needed

        for right, ch in enumerate(s2):
            # if this char can be consumed, consume it
            if ch in need and need[ch] > 0:
                need[ch] -= 1
                remaining -= 1
                if remaining == 0:
                    return True
            else:
                # otherwise, shrink window from the left until
                # either we collapse to right (left==right) or
                # the offending char becomes available (need[ch] > 0)
                while left < right and (ch not in need or need[ch] == 0):
                    left_ch = s2[left]
                    if left_ch in need:
                        need[left_ch] += 1
                        remaining += 1
                    left += 1

                # after shrinking, try to consume ch (if possible)
                if ch in need and need[ch] > 0:
                    need[ch] -= 1
                    remaining -= 1
                    if remaining == 0:
                        return True
                # if ch is still not usable (not in need), do nothing; continue scanning

        return False


            





        