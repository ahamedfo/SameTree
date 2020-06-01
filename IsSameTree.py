# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            print
            1
            return False
        if p.val != q.val:
            print
            1
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """