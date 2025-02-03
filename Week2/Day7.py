# 1 two sum

# 454 4sumII

# 383 Ransom Note
# use hashMap

# 15 3Sum
# use two pointers
# a去重, 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # remove a duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # remove b and c duplicates
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: 
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res
    

# 18 4 sum 
# for loop then 3Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= target and nums[i] > 0:
                break
            # remove duplicates
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            for j in range(i+1, len(nums)):
                # 剪枝
                if nums[i] + nums[j] >= target and nums[i] + nums[j] > 0:
                    break
                # remove duplicates
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
        return res


            
    

        