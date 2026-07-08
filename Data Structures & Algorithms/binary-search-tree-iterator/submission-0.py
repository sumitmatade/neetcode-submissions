# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.itr = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)

    def next(self) -> int:
        val = self.arr[self.itr]
        self.itr += 1
        return val

    def hasNext(self) -> bool:
        return self.itr < len(self.arr)