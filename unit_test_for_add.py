import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_add_zero(self):
        result = add(0, 10)
        self.assertEqual(result, 10)


# In this example, we have a simple add function that takes two numbers as input and returns their sum. The TestAddFunction class inherits from unittest.TestCase and defines multiple test methods. Each test method begins with the prefix test_ and uses various assertions provided by unittest.TestCase to verify the expected behavior.

# To run the unit tests, execute the script, and the unittest.main() function will discover and run all the test methods within the TestAddFunction class.

# The output will indicate whether the tests pass or fail. For example:

# ...
# ----------------------------------------------------------------------
# Run 3 tests in 0.001s

# OK




if __name__ == '__main__':
    unittest.main()
