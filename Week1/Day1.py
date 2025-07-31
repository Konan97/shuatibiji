# 704. Binary Search
# 规范区间 [left, right]
# 二刷
left, right = 0, len(intervals) - 1
while left <= right:
    mid = left + (right - left)/2
    if intervals[mid][0] <= newInterval[0]:
        left = mid + 1
    elif intervals[mid][0] > newInterval[0]:
        right = mid - 1

# 27. Remove Element
# Fast, slow pointers
# 二刷

# 977. Squares of a sorted array
# two pointers, 中间小 两头大
# 二刷
