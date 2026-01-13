class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 先清理掉標點符號並且改成空格隔開
        for c in ".,;/'!?":
            paragraph = paragraph.replace(c, " ")
          
        lookup = {}
        for char in paragraph.split():
            if char.lower() not in lookup:
                lookup[char.lower()] = 1
            else:
                lookup[char.lower()] += 1
        
        for words in lookup:
            if words in banned:
                lookup[words] = 0

        max_count = 0
        ans = ""
        for key, value in lookup.items():
            if value > max_count:
                max_count = value
                ans = key
        return ans
