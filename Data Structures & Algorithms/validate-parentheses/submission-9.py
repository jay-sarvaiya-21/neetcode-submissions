class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashMap = { "{": "}", "[": "]", "(":")"}


        for i in range(len(s)):
            if s[i] in hashMap:
                stack.append(s[i])
            else: 
                if not stack or s[i] not in hashMap.values() or  hashMap[stack[-1]] != s[i]:
                    print("here")
                    return False
                
                stack.pop()
        if len(stack) > 0:
            print(stack)
            return False
        print(s)
        return True

        