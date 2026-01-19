class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index = 0
        current_num = 1
        operation_stack = []

        while index <= len(target) - 1:
            # 判斷是否等於當前的數字
            # 若是則index += 1，若不是則把它pop，並且用current_num += 1的方式去湊target[index]
            operation_stack.append("Push")
            if target[index] == current_num:
                index += 1
            else: # target[index] != current_num
                operation_stack.append("Pop")
            
            current_num += 1
        
        return operation_stack

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.34 MB Beats 12.15 %
