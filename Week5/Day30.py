# 452 Minimum Number of Arrows to Burst Balloons
# sort based on left
# use the first balloons right as the left limit

# 435 Non-overlapping Intervals
# more practice
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        overlap = 0
        # find number of overlaps
        for i in range(1, len(intervals)):
            
            if intervals[i-1][1] > intervals[i][0]:
                overlap += 1
                # find right end of the prev overlap 
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
            
        return overlap

# 763 Partition Labels
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = [-1]
        output = []
        limit = 0
        s_map = defaultdict(int)
        for i in range(len(s)):
            s_map[s[i]] = i

        for i in range(len(s)):
            # 找区间内所有元素的最远值
            limit = max(limit, s_map[s[i]])
            if limit == i:
                output.append(i-res[-1])
                res.append(i)
                
        return output
