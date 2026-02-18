from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_cities = len(isConnected)
        visited = [False] * num_cities
        province_count = 0

        def dfs(node: int) -> None:
            visited[node] = True
            for neighbor in range(num_cities):
                # 若兩城市之間有路，且該neighbor並未拜訪過則做一次dfs
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for city in range(num_cities):
            # 若此城市尚未被拜訪過，則把省份+1
            if not visited[city]:
                province_count += 1
                dfs(city)

        return province_count

# Runtime: 7 ms Beats 52.42 %
# Memory: 21.51 MB Beats 19.30 %
