# 42 Trapping Rain Watr
# 三个元素来接水 画图helps
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        monoStack = []
        monoStack.append(0)
        volume = 0
        for i in range(1, len(height)):
            if height[i] < height[monoStack[-1]]:
                monoStack.append(i)
            elif height[i] == height[monoStack[-1]]:
                monoStack.pop()
                monoStack.append(i)
            else:
                while monoStack and height[i] > height[monoStack[-1]]:
                    # 每次只把mid除去
                    mid = monoStack[-1]
                    monoStack.pop()
                    if monoStack:
                        
                        h = min(height[monoStack[-1]], height[i]) - height[mid]
                        w = i - (monoStack[-1] + 1)
                        volume += h*w
                        print(monoStack[-1], h, h*(i-monoStack[-1]-1))
                        # monoStack.pop()
                monoStack.append(i)

        return volume



