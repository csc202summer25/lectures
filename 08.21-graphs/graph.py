import dictionary as dct


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # NOTE: A 2D dictionary can be smaller than a true adjacency matrix and
        #       faster than an adjacency list:
        #         * The "outer" dict. maps vertices to "inner" dicts.
        #         * Each "inner" dict. maps neighboring vertices to 1's.
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()

        # NOTE: The number of vertices is thus the size of the "outer" dict.,
        #       but the number of edges cannot be computed in constant time:
        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    # Create a new empty dictionary (the new vertex has no neighbors).
    # Insert the given vertex into the matrix, mapped to that dictionary.
    pass


def add_edge(graph, vertex_u, vertex_v):
    # Get vertex_u's dictionary from the matrix.
    # Insert vertex_v into vertex_u's dictionary, mapped to 1.
    # Get vertex_v's dictionary from the matrix.
    # Insert vertex_u into vertex_v's dictionary, mapped to 1.
    # Increment the size.
    pass


def remove_vertex(graph, vertex):
    # NOTE: It makes no sense to have an edge with no vertices, so before we
    #       can remove a vertex, we first have to remove all of its incident
    #       edges -- every occurrence of that vertex in an "inner" dict.
    #
    # Get the given vertex's dictionary from the matrix.
    # Get the list of that dictionary's keys (the list of neighbors).
    #
    # For i from 0 to the size of that list (for each neighbor), do:
    #     Get the i'th element from the list (the i'th neighbor).
    #     Remove the edge between the given vertex and the i'th element.
    #
    # Remove the given vertex from the matrix.
    pass


def remove_edge(graph, vertex_u, vertex_v):
    # Get vertex_u's dictionary from the matrix.
    # Remove vertex_v from vertex_u's dictionary.
    # Get vertex_v's dictionary from the matrix.
    # Remove vertex_u from vertex_v's dictionary.
    # Decrement the size.
    pass


def path(graph, vertex_u, vertex_v):
    # NOTE: Like a level-order traversal, a breadth-first search stores
    #       vertices to be explored in a queue, such that closer vertices are
    #       encountered, enqueued, dequeued, and explored first.
    #
    # Create an empty queue (of vertices to be explored).
    # Enqueue the given vertex_u.
    #
    # NOTE: Unlike a level-order traversal, a breadth-first search may find a
    #       path to a vertex that has already been explored before, since there
    #       are no restrictions on when vertices can connect to other vertices.
    #
    # Create an empty dictionary (of predecessors along computed paths).
    # Insert the given vertex_u into the dictionary, mapped to itself.
    #
    # While the queue is not empty, do:
    #     Dequeue a current vertex from the queue.
    #
    #     If the current vertex is vertex_v, then:
    #         (the path can be derived from the predecessors dictionary)
    #
    #     Get the current vertex's dictionary from the matrix.
    #     Get the list of that dictionary's keys (the list of neighbors).
    #
    #     For i from 0 to the size of that list (for each neighbor), do:
    #         Get the i'th element from the list (the i'th neighbor).
    #         If the i'th element is not in the predecessors dictionary, then:
    #             Enqueue the i'th element (to the queue of vertices to be
    #              explored).
    #             Insert the i'th element (into the predecessors dictionary),
    #              mapped to the current vertex.
    #
    # NOTE: If we break out of the above loop normally, there are no more
    #       vertices to explore (the queue is empty), and we also never found a
    #       path (we never returned early).
    #
    # (there are no paths)
    pass
