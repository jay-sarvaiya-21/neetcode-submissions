class Solution:
    def trap(self, height: List[int]) -> int:
     
        n = len(height)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        left[0] = height[0]
        for i in range(1,n):
            l = max(left[i-1],height[i])
            left[i] = l
        right[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            r = max(right[i+1],height[i])
            right[i] = r
        print(left)
        print(right)
        area = 0 
        
        for i in range(n):
            
            area += min(left[i],right[i]) - height[i]
            print(min(left[i],right[i]) - height[i])

        return area