class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"(":")","[":"]","{":"}"}
        stack = []

        for char in s:
            if char in braces:
                stack.append(char)
                continue
            if stack and char not in braces.keys() and braces[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return True if not stack else False
            