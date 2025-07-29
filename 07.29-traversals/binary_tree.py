class BinaryTree:
    """ A binary tree """

    def __init__(self, value = None):
        # NOTE: The trees of zero and one node are the smallest possible trees.
        #       All other, larger trees can be created by combining existing,
        #       smaller trees.
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
    # NOTE: Since trees are defined recursively, they can be traversed by
    #       recursive functions. However, BinaryTrees are not recursive -- they
    #       do not contain other BinaryTrees -- rather, Nodes are recursive.
    #       Every Node contains 0, 1, or 2 other Nodes.
    #
    # Traverse the given tree's root.
    pass


def _traverse(node):
    # If the given node is None, then:
    #     (there is no node to traverse -- perform whatever default action
    #      ought to be performed on empty trees, e.g., do nothing)
    # Else, do:
    #     Recurse on the given node's left.
    #     Recurse on the given node's right.
    #     (traverse the given node -- perform whatever action ought to be
    #      performed on a traversed node, e.g., add it to a queue)
    pass


def preorder(tree):
    # NOTE: A pre-order traversal could certainly be done recursively, but any
    #       recursive function can be made iterative by maintaining a "stack of
    #       jobs": just like stacks, function calls are LIFO. The first to be
    #       called is last to return; the last to be called is first to return.
    #
    # Start with an empty stack.
    # If the given tree's root is not None, then:
    #     Push the given tree's root onto the stack.
    #
    # NOTE: The stack essentially contains nodes that we know exist in the tree
    #       but which we have yet to traverse -- jobs that we have identified
    #       but which we have not yet completed. On each iteration, we will pop
    #       one job off of the stack and complete it.
    #
    # While the stack is not empty, do:
    #     Pop a current node off of the stack.
    #     (traverse the current node -- perform whatever action ought to be
    #      performed on a traversed node, e.g., add it to a queue)
    #
    #     If the current node's right is not None, then:
    #         Push the current node's right onto the stack.
    #     If the current node's left is not None, then:
    #         Push the current node's left onto the stack.
    #
    # NOTE: Once the stack is empty, there are no more nodes to be traversed.
    #       There are no more jobs that have yet to be completed.
    pass


def levelorder(tree):
    # NOTE: Siblings will always be encountered before children. With a stack,
    #       siblings are pushed before children, thus children are popped and
    #       traversed before siblings. If we instead wish to traverse siblings
    #       before children, we can replace the stack with a queue.
    #
    # Start with an empty queue.
    # If the given tree's root is not None, then:
    #     Enqueue the given tree's root to the queue.
    #
    # While the queue is not empty, do:
    #     Dequeue a current node from the queue.
    #     (traverse the current node -- perform whatever action ought to be
    #      performed on a traversed node, e.g., add it to a queue)
    #
    #     If the current node's left is not None, then:
    #         Enqueue the current node's left to the queue.
    #     If the current node's right is not None, then:
    #         Enqueue the current node's right to the queue.
    pass
