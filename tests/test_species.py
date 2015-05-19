from unittest import TestCase
import unittest
from butterflies.species import get_species_from_html


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