import unittest

class TestDog(unittest.TestCase):
    def test_human_age(self):
        dog = Dog(4)
        self.assertEqual(dog.human_age(), 28)

if __name__ == '__main__':
    unittest.main()
