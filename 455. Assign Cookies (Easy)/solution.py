class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        children.sort()
        cookies.sort()
        children_index, cookies_index = 0, 0

        while children_index < len(children) and cookies_index < len(cookies):
            # 如果說該餅乾 >= 小孩的飢餓程度，則把children_index += 1
            if cookies[cookies_index] >= children[children_index]:
                children_index += 1
            cookies_index += 1
        
        return children_index

# Runtime: 19 ms Beats 79.62 %
# Memory: 22.08 MB Beats 50.32 %
