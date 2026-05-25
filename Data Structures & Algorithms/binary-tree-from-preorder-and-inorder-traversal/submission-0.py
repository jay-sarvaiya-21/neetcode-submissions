# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder,inorder,i):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[i]) # -> int
            ind = inorder.index(root.val) 
            root.left = dfs(preorder[i + 1: i + 1 + ind],inorder[:ind+ 1],i)
            root.right = dfs(preorder[ind+1: ],inorder[ind+ 1:],i)

            return root 

        return dfs(preorder,inorder,0)
