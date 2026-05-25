# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        visit = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            visit.append(root.val)
            dfs(root.right)
            
                

        dfs(root)
        print(visit)
        return visit[k-1]





        

    
        