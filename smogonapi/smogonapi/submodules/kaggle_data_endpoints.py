"""
This submodule contains all of the endpoints that primarily
return data from static datasets.
"""

from fastapi import APIRouter
from .static_data_loader import load_pokemon_stats, load_pokemon_abilities

router = APIRouter()

@router.get("/getPokemonStatsHistorical/{pokemon}")
def get_pokemon_stats_historical(pokemon: str):
    """
    Parameters
    ----------
    pokemon (str)
        The name of a Pokemon

    Returns
    -------
    (JSON)
        A JSON object representing the in-game historical data for the Pokemon
    """

    pokemon_stats_data = load_pokemon_stats()
    pokemon_stats = None
    if pokemon.lower() in pokemon_stats_data.keys():
        pokemon_stats = pokemon_stats_data[pokemon.lower()]
    response = {}
    if pokemon_stats is None:
        response['status'] = "Failed"
        response['reason'] = "Pokemon not found in Gen 1-9 dataset"
    else:
        response['status'] = "Success"
        response['stats'] = pokemon_stats
    return response

@router.get("/GetListOfAbilities")
def get_abilities():
    """
    Parameters
    ----------
    None

    Returns
    -------
    (JSON)
        A JSON object with the name of every ability in the games,
        as well as their descriptions
    """
    abilities = load_pokemon_abilities()
    abilities_array = []
    for ability_name, ability_desc in abilities.items():
        abilities_array.append({
            "name" : ability_name,
            "description": ability_desc
        })
    return abilities_array
