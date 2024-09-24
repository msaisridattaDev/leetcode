##########3#########
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float("inf")

        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath

            if not node:
                return 0

            gainFromLeft = max(gainFromSubtree(node.left), 0)
            gainFromRight = max(gainFromSubtree(node.right), 0)

            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)

            return max(gainFromLeft + node.val, gainFromRight + node.val)

        gainFromSubtree(root)
        return maxPath