"""
Provides testing for the smogon_endpoints module

Classes
-------
TestSmogon_Endpoints(unittest.TestCase)
    Performs a series of different tests on the smogon_endpoints module
"""
import unittest
from fastapi.testclient import TestClient

from smogonapi.main import myApp
from smogonapi.submodules import smogon_endpoints

class TestSmogonEndpoints(unittest.TestCase):
    """
    Performs different types of unit tests on the endpoints handling scraped Smogon data
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

    def test_smoke_get_smogon(self):
        """
        This smoke test ensures the GetSmogonData endpoint
        returns a valid response.
        """
        client = TestClient(myApp)
        response = client.get("/GetSmogonData/ss/Charizard")
        assert response.status_code == 200

        pokemon = response.json()
        assert "languages" in pokemon.keys()
        assert "learnset" in pokemon.keys()
        assert "strategies" in pokemon.keys()

    def test_pokedata_invalid_gen(self):
        """
        This smoke test ensures the GetSmogonData endpoint
        returns a ValueError if the gen is invalid.
        """
        client = TestClient(myApp)
        response = client.get("/GetSmogonData/badGen/Charizard")
        assert response.status_code == 200
        assert response.json()['errorType'] == "ValueError"

    def test_pokedata_invalid_poke(self):
        """
        This smoke test ensures the GetSmogonData endpoint
        returns ValueError if the Pokemon name is invalid.
        """
        client = TestClient(myApp)
        response = client.get("/GetSmogonData/ss/Carizard")
        assert response.status_code == 200
        assert response.json()['errorType'] == "ValueError"
    
    def test_smoke_get_gendata(self):
        """
        This smoke test ensures the GetPokemonByGen endpoint
        returns a valid response.
        """
        client = TestClient(myApp)
        response = client.get("/GetPokemonByGen/rb/")
        assert response.status_code == 200

        pokemon_list = response.json()
        for pokemon in pokemon_list:
            assert "name" in pokemon.keys()
            assert "types" in pokemon.keys()
            assert "abilities" in pokemon.keys()

    def test_gendata_invalid_gen(self):
        """
        This smoke test ensures the GetPokemonByGen endpoint
        returns a ValueError if the gen is invalid.
        """
        client = TestClient(myApp)
        response = client.get("GetPokemonByGen/badGen/")
        assert response.status_code == 200
        assert response.json()['errorType'] == "ValueError"

    def test_smoke_get_tierdata(self):
        """
        This smoke test ensures the GetPokemonByGenAndTier endpoint
        returns a valid response.
        """
        client = TestClient(myApp)
        response = client.get("/GetPokemonByGenAndTier/ss/OU")
        assert response.status_code == 200

        pokemon_list = response.json()
        for pokemon in pokemon_list:
            assert "name" in pokemon.keys()
            assert "types" in pokemon.keys()
            assert "abilities" in pokemon.keys()

    def test_tierdata_invalid_gen(self):
        """
        This smoke test ensures the GetPokemonByGenAndTier endpoint
        returns a ValueError if the gen is invalid.
        """
        client = TestClient(myApp)
        response = client.get("/GetPokemonByGenAndTier/badGen/OU")
        assert response.status_code == 200
        assert response.json()['errorType'] == "ValueError"

    def test_tierdata_invalid_tier(self):
        """
        This smoke test ensures the GetPokemonByGenAndTier endpoint
        returns ValueError if the Pokemon name is invalid.
        """
        client = TestClient(myApp)
        response = client.get("/GetPokemonByGenAndTier/ss/OP")
        assert response.status_code == 200
        assert response.json()['errorType'] == "ValueError"
    
    def test_smoke_get_items(self):
        """
        This smoke test ensures the GetItems endpoint
        returns a valid response.
        """
        client = TestClient(myApp)
        response = client.get("/GetItems/ss/")
        assert response.status_code == 200

        items_list = response.json()
        for item in items_list:
            assert "name" in item.keys()
            assert "description" in item.keys()

    def test_items_invalid_gen(self):
        """
        This smoke test ensures the GetItems endpoint
        returns a ValueError if the gen is invalid.
        """
        client = TestClient(myApp)
        response = client.get("/GetItems/badGen")
        assert response.status_code == 200
        assert response.json()['errorType'] == "ValueError"

if __name__ == '__main__':
    unittest.main()
