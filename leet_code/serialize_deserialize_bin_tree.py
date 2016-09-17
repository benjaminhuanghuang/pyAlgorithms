'''
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to
follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms
should be stateless.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        level = [root]
        while level:
            next_level = []
            for node in level:
                if node:
                    res.append(str(node.val))
                else:
                    res.append('null')
                next_level.append(str(node.left))
                next_level.append(str(node.right))
            level = next_level
        return "[{0}]".format(",".join(res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "null":
            return None

        values = data[1:-1].split(",")
        root = TreeNode(values[0])
        nodes = [root]
        index = 0
        is_left = True
        for value in values:
            if value != "null":
                node = TreeNode(int(value))
                if is_left:
                    nodes[index].left = node
                else:
                    nodes[index].right = node
                    nodes.append(node)
            if not is_left:
                index += 1
            is_left = not is_left
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
