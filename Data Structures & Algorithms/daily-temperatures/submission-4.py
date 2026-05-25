class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        
        res = [0 for _ in range(len(temperatures))] 
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                pt,pi = stack.pop()
                res[pi] = i - pi


            stack.append([temp,i])
        return res


