class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        union = {}
        final = []
        for i in nums1:
            union[i] = 0
        for i in nums2:
            if i in union:
                union[i] += 1
                if union[i] == 1:
                    final.append(i)
        return final
        