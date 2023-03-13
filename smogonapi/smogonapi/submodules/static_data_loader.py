"""File that includes all static data loading functions"""

import os.path
import pandas as pd


def load_pokemon_stats():
    """
    Loads the pokemon 1-8 gen dataset from local repository,
    and return a map that contains pokemon name -> stats
    :return: dict that contains pokemon name -> stats
    """
    pokemon_df = pd.read_csv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/pokemons_gen1-8.csv'))
    pokemon_df = pokemon_df.fillna('')
    pokemon_stats = pokemon_df.to_dict(orient='records')

    return _build_pokemon_to_stats_dict(pokemon_stats)


def _build_pokemon_to_stats_dict(pokemon_stats):
    """
    Builds pokemon name -> pokemon stats map from a list of pokemon stats
    :param pokemon_stats: List of dicts containing pokemon stats.
    It will need to contain a field named 'Pokemon' representing the pokemon name
    :return:  dict containing pokemon name -> pokemon stats
    """
    result = {}
    for pokemon in pokemon_stats:
        pokemon_name = pokemon['Pokemon']
        result[pokemon_name.lower()] = pokemon

    return result
