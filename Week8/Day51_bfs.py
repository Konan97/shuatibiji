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

# 542 01 Matrix
# start bfs from 0 at the same time
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(mat), len(mat[0])
        mat_copy = [line[:] for line in mat]
        queue = []
        visited = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 0
        while queue:
            length = len(queue)
            distance += 1
            for i in range(length):
                root = queue.pop(0)
                X, Y, distance = root[0], root[1], root[2]
                for d in directions:
                    newX = X + d[0]
                    newY = Y + d[1]
                    if newX < 0 or newX >= row or newY < 0 or newY >= col:
                        continue
                    
                    if (newX, newY) not in visited:
                        queue.append((newX, newY, distance+1))
                        visited.add((newX, newY))
                        mat_copy[newX][newY] = distance + 1
                    
        return mat_copy


# 752 Open the Lock
# BFS guarantees the shortest path in an unweighted graph, so as soon as we find an answer, we know it is the optimal one.


# 841 Keys and Rooms
# BFS

# 127 Word ladder
# BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # hit -xit -hxt -hix
        # -x
        adjList = defaultdict(set)
        for i in range(len(beginWord)):
            for w in wordList:
                # print(beginWord[0:i], beginWord[i+1:], w[0:i], w[i+1:])
                adjList[w[0:i] + "*" + w[i+1:]].add(w)
        # print(adjList)
        # bfs
        return self.bfs(adjList, beginWord, endWord)

    def bfs(self, adjList, beginWord, endWord):
        queue = []
        queue.append((beginWord, 0))
        visited = set()
        visited.add(beginWord)
        distance = 0
        while queue:
            length = len(queue)
            
            node, distance = queue.pop(0)
            if node == endWord:
                return distance + 1
            for j in range(len(node)):
                tmp = node[0:j] + "*" + node[j+1:]
                if tmp in adjList:
                    for w in adjList[tmp]:
                        if w not in visited:
                            queue.append((w, distance + 1))
                            visited.add(w)
                            
        return 0
