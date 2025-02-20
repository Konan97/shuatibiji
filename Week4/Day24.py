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
    
# 78 Subsets
# visit entire tree

# 90 Subsets II
# combine 78 frame and 40 filter
# if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
#      continue
# used[i - 1] == 1，说明同一树枝candidates[i - 1]使用过
# used[i - 1] == 0，说明同一树层candidates[i - 1]使用过