# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        que = [] 
        que.append(root) 
        while len(que) > 0:
            nodes = [] 
            for _ in range(len(que)):
                node = que.pop(0) 
                nodes.append(node.val)
                if node.left != None:
                    que.append(node.left)
                if node.right != None:
                    que.append(node.right)
            ans.insert(0,nodes)
        return ans