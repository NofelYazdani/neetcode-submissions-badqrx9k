class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix) - 1, len(matrix[0]) - 1

        top, bottom = 0, rows

        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bottom = m - 1
            else:
                break
        if not top <= bottom:
            return False
        start, end = 0, col

        while start <= end:
            cm = (start + end) // 2
            if matrix[m][cm] > target:
                end = cm - 1
            elif matrix[m][cm] < target:
                start = cm + 1
            else:
                return True
        return False


             



        