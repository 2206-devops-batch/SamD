import unittest
import my_dice_ver_4

class SimpleTest(unittest.TestCase):

    def test_user_input(self):
        self.assertListEqual(my_dice_ver_4.get_set(6), [])

    def test_some(self):
        pass


if __name__ == '__main__':
    unittest.main()