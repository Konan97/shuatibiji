# 99 number of islands (ACM)
# 200 number of islands (LeetCode)
# bfs <><><><><><><><><><><><><><><><><><><>
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = set()
        island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, (i, j), visited)
                    island += 1
        return island
        
        
    def bfs(self, grid, start, visited):
        row, col = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = []
        queue.append(start)
        while queue:
            node = queue.pop(0)
            X = node[0]
            Y = node[1]
            for d in directions:
                newX = X + d[0]
                newY = Y + d[1]
                if 0 > newX or newX >= row or 0 > newY or newY >= col or grid[newX][newY] == "0" or (newX, newY) in visited:
                    continue
                visited.add((newX, newY))
                queue.append((newX, newY))

# dfs <><><><><><><><><><><><><><><><><><><><><><><><>
def dfs(grid, visited, x, y):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i, j in directions:
        newX = x + i
        newY = y + j
        if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]):
            if visited[newX][newY] == False and grid[newX][newY] == 1:
                visited[newX][newY] = True
                dfs(grid, visited, newX, newY)


if __name__ == '__main__':
    n, m = map(int, input().split())
    
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    print(grid)
    

    visited = [[False for _ in range(m)] for _ in range(n)]
    print(visited)
    res = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                res += 1
                dfs(grid, visited, i, j)

    print(res)


# 99 bfs 加入列队立刻标记visited

# 100 max area of island


# 286 Walls and Gates
# start from Gates at the same time