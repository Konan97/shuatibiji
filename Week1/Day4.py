# 24 Swap Nodes in Pairs
# dummy 
# cur -> 1 -> 2 -> 3
# step1 cur -> 2
# step2 2 -> 1
# step3 1 -> 3
# step4 cur move 2 steps cur = cur.next.next
# 画图
# 二刷

# 19 Remove Nth Node from End of List
# fast, slow, dummy pointers 
# two steps
# 不难 但是loop要小心
# fast 先走 n 步 然后slow 走
# 二刷

# 142 
# fast = x + n(y + z) + y
# slow = x + y
# fast = 2 * slow
# 推到数学公式 得出 x = z
# 或者集合法 set() 简直作弊😂
# 二刷 set做的