import unittest

from band_name_generator.generator import generate_band_name


class GenerateBandNameTests(unittest.TestCase):
    def test_combines_city_and_pet(self):
        self.assertEqual(generate_band_name("Paris", "Rex"), "Paris Rex")

    def test_strips_whitespace(self):
        self.assertEqual(generate_band_name("  Paris ", " Rex\n"), "Paris Rex")

    def test_empty_city_raises(self):
        with self.assertRaises(ValueError):
            generate_band_name("", "Rex")

    def test_blank_pet_raises(self):
        with self.assertRaises(ValueError):
            generate_band_name("Paris", "   ")


if __name__ == "__main__":
    unittest.main()
