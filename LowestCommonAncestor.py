from Node import Node


def findLowestCommonAncestor(root, x, y):
    if root is None: return None
    if root.key == x or root.key == y: return root

    LowestCommonAncestorLeft = findLowestCommonAncestor(root.left, x, y)
    LowestCommonAncestorRight = findLowestCommonAncestor(root.right, x, y)

    if LowestCommonAncestorLeft and LowestCommonAncestorRight: return root
    if LowestCommonAncestorLeft is not None:
        return LowestCommonAncestorLeft
    else:
        return LowestCommonAncestorRight
