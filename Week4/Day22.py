# BackTrack
# used for brute force search
# a "combination" the order of the items doesn't matter, 
# while a "permutation" the order of the items does matter
# Tree structure
'''for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
    处理节点;
    backtracking(路径，选择列表); // 递归
    回溯，撤销处理结果
}'''

# 77 Combination
# backTrack() tree

# 216 Combination Sum III
# same as 77
# add more stop conditions

# 17 Letter Combination of a Phone number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = ['', '', 'abc','def','ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        self.backTrack(digits, 0, phone, [], res)
        return res

    def backTrack(self, digits, i, phone, path, res):
        # stop condition
        if len(path) == len(digits):
            res.append("".join(path[:]))
            return
        curDigit = int(digits[len(path)])
        print(curDigit)
        for i in range(len(phone[curDigit])):
            path.append(phone[curDigit][i])
            self.backTrack(digits, i + 1, phone, path, res)
            path.pop()




