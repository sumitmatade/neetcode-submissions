import heapq
from typing import List


class Solution:

  def swimInWater(self, grid: List[List[int]]) -> int:
    n = len(grid)
    visit = set([(0, 0)])

    # Min-heap stores tuples of (time/elevation, row, col)
    minH = [[grid[0][0], 0, 0]]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while minH:
      t, r, c = heapq.heappop(minH)

      # Reached the bottom-right corner
      if r == n - 1 and c == n - 1:
        return t

      for dr, dc in directions:
        neiR, neiC = r + dr, c + dc

        # Check bounds and if already visited
        if (
            0 <= neiR < n
            and 0 <= neiC < n
            and (neiR, neiC) not in visit
        ):
          visit.add((neiR, neiC))
          # The required time is the max elevation along the path
          heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])