class BinarySearchTree:
    """ A binary search tree """

    def __init__(self):
        # The root of this tree:
        self.root = None
        # The number of nodes in this tree:
        self.size = 0


class Node:
    """ A single node in a binary search tree """

    def __init__(self, key, left, right):
        # The key contained in this node:
        self.key = key
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def find(bst, key):
    # Return the result of finding the given key at the root.
    pass


def _find(node, key):
    # NOTE: This is the basic pattern for operating on a BST, a recursive
    #       function with four cases depending on how the given key compares
    #       to the current node's key.
    #
    # If the given node is None, then:
    #     (the given key does not exist in the tree)
    # Else if the given key is equal to the node's key, then:
    #     (the given key is in the node)
    # Else if the given key is less than the node's key, then:
    #     Return the result of recursing on the left.
    # Else, do:
    #     Return the result of recursing on the right.
    pass


def insert(bst, key):
    # NOTE: Inserting an existing key does not create a new node, so we cannot
    #       increment the size here -- not all insertions necessarily increase
    #       the number of nodes in the tree.
    #
    # Set the root to the result of inserting the given key at the root.
    pass


def _insert(bst, node, key):
    # NOTE: This function takes as argument a problem (the root of a tree that
    #       does not contain the key) and produces as return value a solution
    #       (the root of a tree that does contain the key -- which may or may
    #       not be the same root we started with).
    #
    # If the given node is None, then:
    #     Create a new node containing the given key.
    #     Increment the size.
    #     Return the new node.
    # Else if the given key is equal to the node's key, then:
    #     (the given key is already in the tree)
    #     Return the node.
    # Else if the given key is less than the node's key, then:
    #     Set the left to the result of recursing on the left.
    #     Return the node.
    # Else, do:
    #     Set the right to the result of recursing on the right.
    #     Return the node.
    pass


def remove(bst, key):
    # Set the root to the result of removing the given key at the root.
    pass


def _remove(bst, node, key):
    # If the given node is None, then:
    #     (the given key does not exist in the tree)
    # Else if the given key is equal to the node's key, then:
    #     If the right is None, then:
    #         Decrement the size.
    #         Return the left.
    #     Else if the left is None, then:
    #         Decrement the size.
    #         Return the right.
    #     Else, do:
    #
    #         NOTE: We don't actually want to remove the *node*, which is the
    #               only thing keeping the left and right subtrees connected;
    #               we want to remove its *key*. Consider the smallest key in
    #               the right subtree:
    #                 * By definition, it's larger than any to the left.
    #                 * By construction, it's smaller than any to the right.
    #               ...that key could take our place, and, because it cannot
    #               have a left child, it's not critical for keeping the rest
    #               of the tree connected.
    #
    #         Set the node's key to the minimum of the right.
    #         Set the node's right to the result of removing that minimum key
    #          from the right.
    #         Decrement the size.
    #         Return the node.
    #
    # Else if the given key is less than the node's key, then:
    #     Set the left to the result of recursing on the left.
    #     Return the node.
    # Else, do:
    #     Set the right to the result of recursing on the right.
    #     Return the node.
    pass


def _min(node):
    # If the given node is None, then:
    #     (there is no smallest key)
    # Else if the left is None, then:
    #     Return the node's key.
    # Else, do:
    #     Return the result of recursing on the left.
    pass


def inorder(bst):
    # Traverse the given tree's root.
    pass


def _traverse(node):
    # If the given node is None, then:
    #     (there is no node to traverse -- perform whatever default action
    #      ought to be performed on empty trees, e.g., do nothing)
    # Else, do:
    #     Recurse on the given node's left.
    #     (traverse the given node -- perform whatever action ought to be
    #      performed on a traversed node, e.g., add it to a queue)
    #     Recurse on the given node's right.
    pass
