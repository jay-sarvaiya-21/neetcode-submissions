# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root,subRoot):
            if not root and not subRoot:
                return True
            if root and not subRoot or subRoot and not root or root.val != subRoot.val :
                return False
            return dfs(root.left,subRoot.left) and dfs(root.right,subRoot.right)

        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                root = q.popleft()
                if dfs(root,subRoot):
                    return True
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return False
        
        