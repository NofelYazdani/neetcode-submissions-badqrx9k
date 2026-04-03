class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp, index]
        result = [0] * len(temperatures)
        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                index = stack.pop()[1]
                result[index] = (i - index)
            stack.append([j, i])
        return result 

             

        