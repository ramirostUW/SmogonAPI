"""
Provides testing for the kaggle_data_endpoints module

Classes
-------
TestSmogon_Endpoints(unittest.TestCase)
    Performs a series of different tests on the kaggle_data_endpoints module
"""
import unittest
from fastapi.testclient import TestClient

from smogonapi.main import myApp
from smogonapi.submodules import kaggle_data_endpoints

class TestSmogonEndpoints(unittest.TestCase):
    """
    Performs different types of unit tests on the endpoints handling kaggle data
    """
    # Smoke Test
    def test_get_historic_pokemon_smoke(self):
        """
        Checks that endpoint gets correct Pokemon
        """
        client = TestClient(myApp)
        pokemon_name = "Pikachu"
        response = client.get("/getPokemonStatsHistorical/" + pokemon_name)
        assert response.status_code == 200

        pokemon_historic = response.json()
        assert pokemon_historic['status'] == "Success"

        pokemon_stats = pokemon_historic['stats']
        assert pokemon_stats['Pokemon Name'] == pokemon_name

    #Edge test
    def test_get_historic_pokemon_bad_name(self):
        """
        Checks that endpoint returns a failed status
        without crashing when given a bad name
        """
        client = TestClient(myApp)
        pokemon_name = "notAPokemon"
        response = client.get("/getPokemonStatsHistorical/" + pokemon_name)
        assert response.status_code == 200

        pokemon_historic = response.json()
        assert pokemon_historic['status'] == "Failed"

    def test_abilities(self):
        """
        Checks that endpoint returns ability list
        in correct format
        """
        client = TestClient(myApp)
        response = client.get("/GetListOfAbilities/")
        assert response.status_code == 200

        ability_list = response.json()
        for ability in ability_list:
            assert "name" in ability.keys()
            assert "description" in ability.keys()
            assert len(ability.keys()) == 2


if __name__ == '__main__':
    unittest.main()
