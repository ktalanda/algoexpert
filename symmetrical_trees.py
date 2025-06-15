class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def symmetricalTree(tree):
    return areSymmetrical(tree.left, tree.right)

def areSymmetrical(left, right):
    if left is not None and right is not None and left.value == right.value:
        return areSymmetrical(left.left, right.right) and areSymmetrical(left.right, right.left)
    return left == right

def symmetricalTreeIterative(tree):
    stackLeft = [tree.left]
    stackRight = [tree.right]

    while len(stackLeft) > 0:
        left = stackLeft.pop()
        right = stackRight.pop()

        if left is None and right is None:
            continue

        if left is None or right is None or left.value != right.value:
            return False

        stackLeft.append(left.left)
        stackLeft.append(left.right)
        stackRight.append(right.right)
        stackRight.append(right.left)

    return True
