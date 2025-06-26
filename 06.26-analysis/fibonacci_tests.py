import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):
    def test01(self):
        # NOTE: This test alone is not enough to conclude that a function is
        #       correct; a function that simply always returned 0 would pass
        #       this test.
        self.assertEqual(fib.fibonacci(0), 0)

    def test02(self):
        # NOTE: These two tests alone are still not enough to even be confident
        #       that a function is correct; they don't cover the recursive case
        #       of the recursive function.
        self.assertEqual(fib.fibonacci(1), 1)

    def test03(self):
        # NOTE: No finite number of tests can ever be enough to know for sure
        #       that a function is correct; for any non-trivial problem, there
        #       are infinitely many inputs and outputs to be tested.
        self.assertEqual(fib.fibonacci(5), 5)

    def test04(self):
        # NOTE: The above tests are so small that we learn nothing about how
        #       fast or how slow a function actually is -- they are so small
        #       that pretty much any function would finish quickly.
        self.assertEqual(fib.fibonacci(30), 832040)


if __name__ == "__main__":
    unittest.main()
