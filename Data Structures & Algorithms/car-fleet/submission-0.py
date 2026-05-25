class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet = [(position[x],speed[x]) for x in range(len(position))]
        stack = []
        for p,s in sorted(fleet)[::-1]:
            stack.append((target - p ) / s )
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)




         





        
        