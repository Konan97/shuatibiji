# 463 Island Perimeter
# land*4-neighbor*2

# 841 Keys and Rooms
# recursive dfs
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        self.dfs(rooms, 0, visited)
        # print(visited)
        return len(visited) == len(rooms)
    
    def dfs(self, rooms, cur, visited):
        if cur in visited:
            return

        visited.add(cur)
        for i in rooms[cur]:
            self.dfs(rooms, i, visited)

# 210 Course Schedule II
# topological sort
# run dfs on all nodes
# if we find a cycle, return []
