from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)

        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n

if __name__=="__main__":
    a=Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
    print(a)
