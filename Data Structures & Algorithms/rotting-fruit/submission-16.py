class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [0,1],[0,-1],[-1,0]]
        time ,fresh = 0, 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = r + dr, c+dc
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh = fresh - 1
            time = time + 1
        if fresh > 0:
            return -1
        return time




