from tree_node import TreeNode


def is_tree_same(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 and t2 and t1.val == t2.val:
        return is_tree_same(t1.left, t2.left) and is_tree_same(t1.right, t2.right)

    return False


def is_tree_same_dfs(t1, t2):
    if t1 is None and t2 is None:
        return True

    stack = [(t1, t2)]
    while stack:
        n1, n2 = stack.pop()
        if n1 == None or n2 == None:
            continue
        elif n1 and n2 and n1.val == n2.val:
            stack.append(n1.left, n2.left)
            stack.append(n1.righ, n2.right)
        else:
            return False
    return True


def invert_binary_tree(root):
    if root is None:
        return None

    if root.left:
        invert_binary_tree(root.left)
    if root.right:
        invert_binary_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


def invertTree_dfs(root):
    if root is None:
        return None
    queue = [root]
    while queue:
        front = queue.pop(0)
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)
        front.left, front.right = front.right, front.left
    return root


def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    if root is None:
        return []
    return [root.val] + inorderTraversal(root.left) + inorderTraversal(root.right)


def build_tree(nums):
    if not nums:
        return None

    root = TreeNode(nums.pop(0))

    stack = [root]
    while stack and nums:
        new_stack = []
        for i in xrange(len(stack)):
            if len(nums) <= 0:
                return root
            else:
                left = TreeNode(nums.pop(0))
                stack[i].left = left
                new_stack.append(left)

            if len(nums) <= 0:
                return root
            else:
                right = TreeNode(nums.pop(0))
                stack[i].right = right
                new_stack.append(right)
        stack = new_stack

    return root


def printTree(root):
    queue = list()
    queue.append(root)
    res = []
    while queue:
        rowVal = []
        tmpRow = []
        for node in queue:
            if node:
                rowVal.append(node.val)
                tmpRow.append(node.left)
                tmpRow.append(node.right)
        queue = tmpRow
        if rowVal:
            res.append(rowVal)
    return res


def printTree_2(root):
    level = [root]
    res = []
    while level:
        next_level = []
        level_val =[]
        for node in level:
            if node:
                level_val.append(node.val)
                next_level.append(node.left)
                next_level.append(node.right)
        level = next_level
        if level_val:
            res.append(level_val)
    return res


tree = build_tree([1, 2, 3, 4, 5, None, 6])

print_tree = printTree_2(tree)

for i in print_tree:
    print i
