# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def splitBinaryTree(tree):
    desiredSubtreeSum = getTreeSum(tree) / 2
    caBeSplit = trySubtree(tree, desiredSubtreeSum)[1]
    return desiredSubtreeSum if caBeSplit else 0

def trySubtree(tree, desiredSubtreeSum):
    if tree is None:
        return (0, False)
    leftSum, leftCanBeSplit = trySubtree(tree.left, desiredSubtreeSum)
    rightSum, reightCanBeSplit = trySubtree(tree.right, desiredSubtreeSum)

    currentTreeSum = tree.value + leftSum + rightSum
    canBeSplit = leftCanBeSplit or reightCanBeSplit or currentTreeSum == desiredSubtreeSum
    return (currentTreeSum, canBeSplit)

def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)
