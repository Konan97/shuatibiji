# 99 number of islands (ACM)
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