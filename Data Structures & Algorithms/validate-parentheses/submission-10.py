class Solution:
    def isValid(self, s: str) -> bool:
        openning_brackets = {"{":"}","[":"]","(":")"}
        # closing_breackets = {"}","]",")"}

        stack = []

        for curr in s:
            if curr in openning_brackets:
                stack.append(curr)
            else:
                if not stack or openning_brackets[stack[-1]] != curr:
                    return False
                stack.pop()
        if stack:
            return False
        return True