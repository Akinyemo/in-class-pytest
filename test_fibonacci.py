import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(fibonacci.fibonacci(5),5)

    def test_incorrect(self):
        self.assertEqual(fibonacci.fibonacci(-10),-1)
    
    def test_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(fibonacci.fibonacci('String'))

if __name__ == "__main__":
    unittest.main()