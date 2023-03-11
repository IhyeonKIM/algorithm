# https://leetcode.com/problems/valid-parentheses/
# (){}[]를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오. 

# 괄호는 짝수
# 여는 것이 먼저오고, 여는게 있으면 같은 짝으로 닫는게 있어야 

# 여는 건 1 , 닫는건 -1 -> 총 0 이 도출되어야 
# 음수가 되는 순간 F 

# Stack 이용해서 문제 풀이 



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0 : 
            return False 

        for p in s :
            if p == "(": stack.append(")")
            elif p =="[": stack.append("]")
            elif p =="{": stack.append("}")
            elif p in ["]",")","}"]: 
                if not stack or stack[-1] != p: 
                    return False 
                else: 
                    stack.pop()
        return not stack