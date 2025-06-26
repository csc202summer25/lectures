import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):
    def test01(self):
        self.assertEqual(fib.fibonacci(0), 0)


if __name__ == "__main__":
    unittest.main()
