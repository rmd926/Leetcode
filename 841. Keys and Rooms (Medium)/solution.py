class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(room):
            visited[room] = True # 把拜訪過的房間標示成True

            for key in rooms[room]: # 把所有房間內的鑰匙取出來
                if not visited[key]: # 如果尚未拜訪過，則去跑一次dfs
                    dfs(key)
        dfs(0)

        return sum(visited) == n

# Runtime: 0 ms Beats 100.00 %
# Memory: 20.24 MB Beats 24.03 %
