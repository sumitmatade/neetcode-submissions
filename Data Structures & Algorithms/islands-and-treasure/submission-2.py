from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """

        if not grid:
            return

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        queue = deque()

        # Add all treasure cells to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Multi-source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    grid[nr][nc] != INF
                ):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))