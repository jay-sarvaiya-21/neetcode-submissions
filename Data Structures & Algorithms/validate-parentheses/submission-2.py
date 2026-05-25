class Solution:
    def isValid(self, s: str) -> bool:
        mapp={'}':'{', ']':'[', ')':'('}
        stack = []

        for ele in s:
            if ele not in mapp:
                stack.append(ele)
            else:
                if len(stack) == 0 :
                    return False
                peek=stack.pop()
                if mapp[ele] == peek:
                    continue
                else:
                    return False
        return len(stack) == 0        