import Image
from pytesseract import image_to_string
from unittest import TestCase
import unittest
from butterflies.params import root_dir


def get_image_as_string():
    return image_to_string(Image.open('%s/data/test.png' % root_dir))


class TestTess(TestCase):
    def test_starts_correctly(self):
        text = get_image_as_string()
        expected = "A third subfamily, the Heteropterinae, is weakly differentiated from the other"
        self.assertEquals(text[0:50], expected[0:50])


if __name__ == "__main__":
    unittest.main()