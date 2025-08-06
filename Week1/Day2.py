# 209. Minimum Size Subarray Sum
# sliding window
# 二刷 while loop

# 59. Spiral Matrix II
# 2D array 
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        loop = n / 2
        startx, starty = 0, 0 # starting point
        count = 1 
        offSet = 1 # each loop Offset += 1
        mid = n / 2 
        res = [[0 for _ in range(n)] for _ in range(n)] 
        while loop:
            i = startx
            j = starty
            while j < n-offSet:
                res[i][j] = count
                count += 1
                j += 1

            while i < n-offSet:
                res[i][j] = count
                count += 1
                i += 1

            while j > starty:
                res[i][j] = count
                count += 1
                j -= 1
            
            while i > startx:
                res[i][j] = count
                count += 1
                i -= 1

            startx += 1
            starty += 1
            loop -= 1
            offSet += 1 # control length of each side
        if n % 2 == 1:
            res[mid][mid] = count
        return res
        
# 289. Game of Life
# 2D array
# dead cell: 1 -> -1
# live cell: 0 -> 2

# 1428 Leftmost Column with at least a One
# binary search on each row
# 

# 48 rotate image

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # rotate in a group of four
        # [0,0][0,1][0,2][0,3]
        # [1,0][1,1][1,2][1,3]
        # [2,0][2,1][2,2][2,3]
        # [3,0][3,1][3,2][3,3]

        n = len(matrix)
        for i in range(n/2+n%2):
            for j in range(n/2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp

# 947 Most Stones Removed with Same Row or Column
# list or array problem but solving using graph connected component
# BFS
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # BFS find connected components
        row, col = defaultdict(list), defaultdict(list)

        for i in range(len(stones)):

            row[stones[i][0]].append(i)
            col[stones[i][1]].append(i)

        queue = []
        visited = set()

        connected = 0
        for i in range(0, len(stones)):
            if tuple(stones[i]) not in visited:
                queue.append(stones[i])
                visited.add(tuple(stones[i]))
                while queue:
                    top = queue.pop()
                    x, y = top[0], top[1]
                    for neighbor in row[x]:
                        if tuple(stones[neighbor]) not in visited:
                            queue.append(stones[neighbor])
                            visited.add(tuple(stones[neighbor]))
                    for neighbor in col[y]:
                        if tuple(stones[neighbor]) not in visited:
                            queue.append(stones[neighbor])
                            visited.add(tuple(stones[neighbor]))
                connected += 1


        return len(stones) - connected