class BinaryTree:
    """ A binary tree """

    def __init__(self, value = None):
        # NOTE: The trees of zero and one node are the smallest possible trees.
        #       All other trees can be created by combining existing smaller
        #       trees.
        #
        if value is None:
            # The root of this empty tree:
            self.root = None
            # The number of nodes in this tree:
            self.size = 0
        else:
            # The root of this singleton tree:
            self.root = Node(value, None, None)
            # The number of nodes in this tree:
            self.size = 1


class Node:
    """ A single node in a binary tree """

    def __init__(self, value, left, right):
        # NOTE: A tree is essentially a linked list in which nodes may have
        #       multiple successors. Rather than a single "next", a node in a
        #       binary tree may have both a "left" and a "right".
        #
        # The value contained in this node:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def combine(value, left, right):
    # NOTE: Trees are inherently recursive: every non-trivial tree contains two
    #       smaller subtrees. Every node in the left subtree, and every node in
    #       the right subtree, is also a node in the overall tree, together
    #       with the root.
    #
    # Create a new tree containing the given value.
    # Set the new tree's root's left to the given left's root.
    # Set the new tree's root's right to the given right's root.
    # Set the new tree's size to (the left's size + the right's size + 1).
    pass


def postorder(tree):
    pass


def preorder(tree):
    pass


def levelorder(tree):
    pass
