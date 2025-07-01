# NOTE: This defines a new type named "Pair", composing two attributes named
#       "first" and "second". This class, together with the associated "swap"
#       function, implement a pair data structure, which in turn implements
#       the pair ADT.
class Pair:
    """ A pair of elements """

    def __init__(self, first, second):
        # NOTE: Whenever a Pair is created, the first and second values must
        #       be provided.
        self.first = first
        self.second = second

    def __eq__(self, other):
        # NOTE: Two Pairs are considered equal if and only if they contain the
        #       same two values in the same order.
        return (type(other) == type(self)
                and self.first == other.first
                and self.second == other.second)

    def __repr__(self):
        # NOTE: The interpreter has no idea what a Pair is aside from our
        #       definition; it does not, for example, know how to print it out.
        return "Pair(%r, %r)" % (self.first, self.second)


def swap(pair):
    """
    Swap the elements of a pair.

    :param pair: A pair of elements
    :return: A new pair with those elements swapped
    """
    return Pair(pair.second, pair.first)


# NOTE: Pairs are similar to lists -- both are finite, ordered collections of
#       elements -- but pairs can only ever contain *exactly two* elements. But
#       the second element could be another Pair...
lst = Pair('a', Pair('b', Pair('c', None)))
