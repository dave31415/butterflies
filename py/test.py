import Image
from pytesseract import image_to_string
from unittest import TestCase
import unittest
from params import root_dir
from species import get_species_from_html


def get_image_as_string():
    return image_to_string(Image.open('%s/data/test.png' % root_dir))


class TestTess(TestCase):
    def test_starts_correctly(self):
        text = get_image_as_string()
        expected = "A third subfamily, the Heteropterinae, is weakly differentiated from the other"
        self.assertEquals(text[0:50], expected[0:50])


class TestGetSpecies(TestCase):
    def setUp(self):
        self.sp = get_species_from_html()

    def test_length_species(self):
        self.assertEquals(len(self.sp['species']), 7822)

    def test_length_genus(self):
        self.assertEquals(len(self.sp['genus']), 958)

    def test_length_tribe(self):
        self.assertEquals(len(self.sp['tribe']), 54)

    def test_length_subfamily(self):
        self.assertEquals(len(self.sp['subfamily']), 26)

    def test_length_family(self):
        self.assertEquals(len(self.sp['family']), 6)



if __name__ == "__main__":
    unittest.main()