"""
This submodule contains all of the endpoints that primarily
return data from static datasets.
"""

from fastapi import APIRouter
from .static_data_loader import load_pokemon_stats

router = APIRouter()

@router.get("/getPokemonStatsHistorical/{pokemon}")
def get_pokemon_stats_historical(pokemon: str):
    """
    API handler for retrieving Pokemon stats from static Gen1-8 dataset
    :param pokemon: pokemon name
    :return: stats if found
    """

    pokemon_stats_data = load_pokemon_stats()
    pokemon_stats = pokemon_stats_data[pokemon.lower()]
    print(pokemon_stats)
    response = {}
    if pokemon_stats is None:
        response['status'] = "Failed"
        response['reason'] = "Pokemon not found in Gen 1-8 dataset"
    else:
        response['status'] = "Success"
        response['stats'] = pokemon_stats
    return response

@router.get("/GetInGameData/{gen_name}/{pokemon_name}")
def get_game_data(gen_name, pokemon_name):
    """
    docstring
    """
    return {"message": "not implemented yet",
        "gen_name": gen_name,
        "pokemon_name": pokemon_name}

@router.get("/GetListOfAbilities/{gen_name}")
def get_abilities(gen_name):
    """
    docstring
    """
    return {"message": "not implemented yet",
        "gen_name": gen_name}
