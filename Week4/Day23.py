# 回溯法抽象为树形结构后，其遍历过程就是：for循环横向遍历，递归纵向遍历，回溯不断调整结果集。
# 39. Combination sum
# Similar to 77 & 216

# 40. Combination sum II
# 去重的逻辑有点难
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        used = [0 for _ in range(len(candidates))] 
        res = []
        self.backTrack(candidates, target, 0, [], res, used)
        return res
    
    def backTrack(self, candidates, target, startIndex, path, res, used):
        # stop condition
        if sum(path) > target:
            return
        if sum(path) == target:
            res.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            # trim width: if prev is used then it is listed in prior branch
            if i > 0 and candidates[i] == candidates[i-1] and used[i-1] == 0:
                continue
            path.append(candidates[i])
            used[i] = 1
            self.backTrack(candidates, target, i + 1, path, res, used)
            path.pop()
            used[i] = 0
        

# 131 Palindrome partitioning
# more practice
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.backTrack(s, [], 0, res)
        return res
    
    def backTrack(self, s, path, startIndex, res):
        if startIndex >= len(s):
            res.append(path[:])
            return
        
        for i in range(startIndex, len(s)):
            # find if cur string slice is Pali
            if self.isPalindrome(s, startIndex, i):
                path.append(s[startIndex:i+1])
            else:
                continue
            self.backTrack(s, path, i + 1, res)
            path.pop()
        

    def isPalindrome(self, s, startIndex, i):
        # print(s[startIndex:i+1])
        while startIndex <= i:
            if s[startIndex] != s[i]:
                return False
            startIndex += 1
            i -= 1
        return True

# 93 Restore IP addresses
# more practice similar to 131
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.backTrack(s, 0, [], res)
        return res

    def backTrack(self, s, startIndex, path, res):
        # stop condition
        if startIndex == len(s) and len(path) == 4:
            res.append(".".join(path[:]))
            return
        if len(path) > 4:
            return

        for i in range(startIndex, len(s)):
            # filter
            if self.isValid(s[startIndex:i+1]):
                path.append(s[startIndex:i+1])
                self.backTrack(s, i + 1, path, res)
                path.pop()                 
            
    def isValid(self, slice):
        if not slice:
            return False
        if slice[0] == '0' and len(slice) > 1:
            return False
        num = 0
        for i in slice:
            if not i.isdigit():
                return False
            num = num * 10 + int(i)
            if num > 255:
                return False
        return True
        