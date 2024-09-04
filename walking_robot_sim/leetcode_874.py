from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, d = 0, 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        max_dist = 0
        obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            if cmd == -2:
                d = (d - 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + direction[d][0] # update the position for x
                    ny = direction[d][1] # update the position for y
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist