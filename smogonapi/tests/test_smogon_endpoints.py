"""
Provides testing for the smogon_endpoints module

Classes
-------
TestSmogon_Endpoints(unittest.TestCase)
    Performs a series of different tests on the smogon_endpoints module
"""
import unittest

from smogonapi.submodules import smogon_endpoints

class TestSmogonEndpoints(unittest.TestCase):
    """
    Performs different types of unit tests, imported from the unittest package

    Functions
    ---------
    test_get_top_pokemon_smoke()
        performs a smoke test, which checks whether the function get_top_pokemon() performs
        correctly
    test_get_top_pokemon_stats_is_list()
        An edge test which validates that a ValueError is raised when a list is not passed for the
        stats parameter
    test_get_top_pokemon_stat_is_string()
        An edge test which validates that a ValueError is raised when the stats parameter contains
        non-strings
    test_get_top_pokemon_stat_is_valid()
        An edge test which validates that a ValueError is raised when the stats parameter contains
        invalid strings (i.e. anything that is not a pokemon stat)
    test_get_top_pokemon_gen_is_string()
        An edge test which validates that a ValueError is raised when the gen parameter is not a
        string
    test_get_top_pokemon_gen_is_valid()
        An edge test which validates that a ValueError is raised when the gen parameter is an
        invalid string (i.e. anything that is not a valid pokemon generation)
    """
    # Smoke Test
    def test_get_top_pokemon_smoke(self):
        """
        Checks that get_top_pokemon performs properly
        """
        smogon_endpoints.get_top_pokemon(['atk', 'spd'], 'gs')
        # pylint: disable=redundant-unittest-assert
        self.assertTrue(True)

    # Edge Test
    def test_get_top_pokemon_stats_is_list(self):
        """
        Validates that a ValueError is raised when stats is not a list
        """
        with self.assertRaises(ValueError):
            smogon_endpoints.get_top_pokemon('atk', 'ss')

    # Edge Test
    def test_get_top_pokemon_stat_is_string(self):
        """
        Validates that a ValueError is raised when stats contains non-strings
        """
        with self.assertRaises(ValueError):
            smogon_endpoints.get_top_pokemon(['atk', 78], 'ss')

    # Edge Test
    def test_get_top_pokemon_stat_is_valid(self):
        """
        Validates that a ValueError is raised when stats contains invalid strings
        """
        with self.assertRaises(ValueError):
            smogon_endpoints.get_top_pokemon(['atk', 'sdfa'], 'ss')

    # Edge Test
    def test_get_top_pokemon_gen_is_string(self):
        """
        Validates that a ValueError is raised when gen is not a string
        """
        with self.assertRaises(ValueError):
            smogon_endpoints.get_top_pokemon(['atk', 'spe'], 34)

    # Edge Test
    def test_get_top_pokemon_gen_is_valid(self):
        """
        Validates that a ValueError is raised when gen is an invalid string
        """
        with self.assertRaises(ValueError):
            smogon_endpoints.get_top_pokemon(['atk', 'spe'], 'rby')

if __name__ == '__main__':
    unittest.main()
