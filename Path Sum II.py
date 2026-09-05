# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, total, path):
            if not node:
                return

            path.append(node.val)
            total += node.val

            if not node.left and not node.right and total == targetSum:
                result.append(path[:])

            dfs(node.left, total, path)
            dfs(node.right, total, path)

            path.pop()

        dfs(root, 0, [])
        return result 
