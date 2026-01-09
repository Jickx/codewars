def is_ends_with(s: str, e: str) -> bool:
    e_l = len(e)
    return s[-e_l:] == e


import unittest

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs")
)


class TestIsEndsWith(unittest.TestCase):
    def test_true_cases(self):
        """Test cases that should return True"""
        for text, ending in fixed_tests_True:
            with self.subTest(text=text, ending=ending):
                self.assertTrue(is_ends_with(text, ending),
                                f"'{text}' should end with '{ending}'")

    def test_false_cases(self):
        """Test cases that should return False"""
        for text, ending in fixed_tests_False:
            with self.subTest(text=text, ending=ending):
                self.assertFalse(is_ends_with(text, ending),
                                 f"'{text}' should not end with '{ending}'")

    def test_empty_string(self):
        """Empty string with empty ending should return True"""
        self.assertTrue(is_ends_with("", ""))

    def test_single_character(self):
        """Test single character strings"""
        self.assertTrue(is_ends_with("a", "a"))
        self.assertFalse(is_ends_with("a", "b"))


if __name__ == '__main__':
    unittest.main()
