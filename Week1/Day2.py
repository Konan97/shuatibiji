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
        