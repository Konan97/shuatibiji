# 739 Daily Temperatures
# use monotonic stack to save index
# {temperature: index}
# 二刷


# 496 Next Greater Element 1
# 非常绕
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [-1 for _ in range(len(nums1))]
        # map key(nums): val(index)
        num1Map = defaultdict(int)
        for i in range(len(nums1)):
            num1Map[nums1[i]] = i
        
        monoStack = []
        monoStack.append(0)

        for j in range(1, len(nums2)):
            # curr num <= stack[-1]
            if nums2[j] <= nums2[monoStack[-1]]:
                monoStack.append(j)
            else:
                while monoStack and nums2[j] > nums2[monoStack[-1]]:
                    if nums2[monoStack[-1]] in num1Map:
                        # index of curr num in nums1
                        index = num1Map[nums2[monoStack[-1]]]
                        result[index] = nums2[j]
                    monoStack.pop()
                monoStack.append(j)
        return result
                        
# 503 Next Greater Element II
# same as 739 496
# circle = nums + nums
