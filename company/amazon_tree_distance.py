class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def sortedArrayToBSTHelper(nums, left, right):
    if left >= right:
        return TreeNode(nums[left])
    mid = left + ((right - left) / 2)
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBSTHelper(nums, left, mid - 1)
    root.right = sortedArrayToBSTHelper(nums, mid + 1, right)
    return root

def sortedArrayToBST(nums):
    if not nums:
        return None
    return sortedArrayToBSTHelper(nums, 0, len(nums) - 1)


def findLowestCommonAncestor(root, val1, val2):
    if not root:
        return None
    if root.val == val1 or root.val == val2:
        return root

    left = findLowestCommonAncestor(root.left, val1, val2)
    right = findLowestCommonAncestor(root.right, val1, val2)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right


def pathLength(root, val):
    if not root:
        return 0

    if root.val == val:
        return 1
    length = pathLength(root.left, val)
    if length > 0:
        return length + 1
    length = pathLength(root.right, val)
    if length > 0:
        return length + 1
    return 0


def findDistance(root, val1, val2):
    if not root:
        return 0
    dist1 = pathLength(root, val1) - 1
    dist2 = pathLength(root, val2) - 1
    lcaVal = findLowestCommonAncestor(root, val1, val2).val
    lcaDist = pathLength(root, lcaVal) - 1
    return (dist1 + dist2) - 2 * lcaDist

def bstDistance(values, n, node1, node2):
    # WRITE YOUR CODE HERE
    values.sort()
    bst = sortedArrayToBST(values)
    dist = findDistance(bst, node1, node2)
    return dist


values = [5, 6, 3, 1, 2, 4]
n = 6
node1 = 2
node2 = 4

print bstDistance(values, n, node1, node2)
