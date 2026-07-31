from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Add all rotten oranges to the queue
        # Count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # No fresh oranges to begin with
        if fresh == 0:
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nc < 0 or
                        nr >= rows or nc >= cols or
                        grid[nr][nc] != 1
                    ):
                        continue

                    # Rot the fresh orange
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

            # Only count another minute if there are oranges
            # that will rot in the next layer.
            if queue:
                minutes += 1

        return minutes if fresh == 0 else -1