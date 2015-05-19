from butterflies import images
import unittest
from unittest import TestCase


class TestImages(TestCase):
    def setUp(self):
        self.string2 = images.get_image_as_string(num=2)
        self.string1 = images.get_image_as_string(num=1)

    def test_string_2_starts_correctly(self):
        expected = 'Frame 50 (reads vertically)'
        self.assertEquals(self.string2[0:27], expected)

    def test_string_1_starts_correctly(self):
        expected = 'Row 1'
        self.assertEquals(self.string1[0:5], expected)

if __name__ == '__main__':
    unittest.main()
