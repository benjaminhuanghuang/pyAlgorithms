'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.
'''
from data_structure.tree_node import TreeNode


class Solution(object):
    # Memory Limit Exceeded
    def buildTree_9(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # write your code here
        if not inorder:
            return None  # inorder is empty
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: 1 + rootPos], inorder[: rootPos])
        root.right = self.buildTree(preorder[rootPos + 1:], inorder[rootPos + 1:])
        return root

    # http://jelices.blogspot.com/2014/05/leetcode-python-construct-binary-tree.html
    def buildTree(self, preorder, inorder):
        return self.buildTreeRec(preorder, inorder, 0, 0, len(preorder))

    def buildTreeRec(self, preorder, inorder, indPre, indIn, element):
        if element == 0:
            return None
        solution = TreeNode(preorder[indPre])
        numElementsLeftSubtree = 0;
        for i in range(indIn, indIn + element):
            if inorder[i] == preorder[indPre]:
                break
            numElementsLeftSubtree += 1
        solution.left = self.buildTreeRec(preorder, inorder, indPre + 1,
                                          indIn, numElementsLeftSubtree)
        solution.right = self.buildTreeRec(preorder, inorder, indPre + numElementsLeftSubtree + 1,
                                           indIn + numElementsLeftSubtree + 1, element - 1 - numElementsLeftSubtree)
        return solution
