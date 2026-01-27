from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # 把名字和身高綁在一起
        people = list(zip(names, heights))
        
        # 依照身高由大到小排序
        people_sorted = sorted(people, key=lambda x: x[1], reverse=True)
        
        ans = []
        # 用 for 迴圈逐一取出排序後的名字
        for person in people_sorted:
            name, height = person
            ans.append(name)
        
        return ans
