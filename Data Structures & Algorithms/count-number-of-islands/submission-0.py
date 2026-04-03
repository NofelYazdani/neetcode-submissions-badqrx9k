class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        result = 0
        visited = set()
        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                row_1, col_1 = queue.popleft()
                directions = [[1,0], [-1,0], [0, 1], [0, -1]]
                for i , j in directions:
                    r = row_1 + i
                    c = col_1 + j
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r,c))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    result +=1
        return result 



    

    
        