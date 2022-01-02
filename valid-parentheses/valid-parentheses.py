class Solution:
    def isValid(self, s: str) -> bool:
        next = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for bracket in s:
            if bracket in next.keys():
                stack.append(bracket)
            elif stack and bracket == next[stack[-1]]:
                stack.pop()
            else: 
                return False
        return stack == []
            
        