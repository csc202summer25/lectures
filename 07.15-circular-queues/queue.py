class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity

        # NOTE: Operating on the beginning of an array list is O(n), but only
        #       because we have to shift elements to maintain indices -- and
        #       queues don't have indices. Essentially, rather than insisting
        #       that elements fall between indices 0 and size - 1, we'll allow
        #       them to range between arbitrary indices front and back.

        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


def enqueue(queue, value):
    # NOTE: Three possibilities exist:
    #         * If front < 0 and back < 0, then the queue is [].
    #         * Else, if front <= back, then the queue is [front:back + 1].
    #         * Else, the queue is [front:capacity] + [0:back + 1].
    #       ...that is, the elements of the queue must be allowed to "wrap
    #       around" the end of the array, so as to avoid increasing the
    #       capacity unless absolutely necessary.
    #
    # If (the size of the queue) equals the queue's capacity, then:
    #     Set the queue's capacity to the queue's capacity * 2.
    #     Create a new array of the queue's capacity.
    #
    #     For i from 0 to the (the size of the queue), do:
    #         Set the new array at i to the lst's array at
    #          (front + i) mod (the size of the queue).
    #
    #     Set the queue's array to the new array.
    #     Set the queue's front to 0.
    #     Set the queue's back to (the size of the queue - 1).
    #
    # NOTE: When increasing capacity, the elements must then be "unwrapped",
    #       since the end of the array has moved. This is not actually any less
    #       efficient, since we were going to have to iterate through the
    #       elements to increase capacity anyways.
    #
    # If the queue's front and back are both negative, then:
    #     Set the queue's front and back to 0.
    # Else, do:
    #     Increment the queue's back and mod it by the capacity.
    #
    # Set the queue's array at the queue's back to the given value.
    pass


def dequeue(queue):
    # If the queue's front equals the queue's back, then:
    #     Set the queue's front and back to -1.
    # Else, do:
    #     Increment the queue's front and mod it by the capacity.
    pass


def peek(queue):
    # Return the queue's array at the queue's front.
    pass
