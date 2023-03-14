"""
This module contains all of the endpoints that
primarily return scraped data from Smogon.com.
"""

# pylint: disable=broad-except
# We deliberately make a broad exception clause to make
# sure the error is delivered to the user as a json message
# rather than crashing the app

import json
from fastapi import APIRouter, Query
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

router = APIRouter()
valid_gens = ["rb", "gs", "rs", "dp", "bw", "xy", "sm", "ss", "sv"]

@router.get("/GetSmogonData/{gen_name}/{pokemon_name}")
def get_smogon_data(gen_name, pokemon_name):
    """
    Parameters
    ----------
    gen_name (str)
        A string representing a generation of Pokemon games. Can be "rb" (for Red/Blue),
        "gs" (for Gold/Sliver), "rb" (for Ruby/Sapphire), "dp" (for Diamond/Pearl),
        "bw" (for Black/White), "xy" (for X/Y), "sm" (for Sun/Moon), "ss" (for Sword/Shield),
        or "sv" (for Scarlet/Violet)

    pokemon_name (str)
        The name of a Pokemon that exists for the specified Gen

    Returns
    -------
    (JSON)
        A JSON object representing the Smogon data for the Pokemon from the specified Generation

    Exceptions
    ----------
    ValueError
        Will be thrown under different conditions:

            When either input is missing

            When either input is invalid

            When no data was retrieved
    """
    try:
        if not pokemon_name or not gen_name:
            raise ValueError("missing inputs")
        valid_gen = gen_name in valid_gens
        if not valid_gen:
            raise ValueError("invalid gen name")
        url = "https://www.smogon.com/dex/" + gen_name + "/pokemon/" + pokemon_name.lower()
        url_page = requests.get(url, timeout=100000)
        soup = bs(url_page.content, 'html.parser')

        script = soup.find_all("script")[1]
        script_insides = script.text
        data = json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs']
        if not data:
            raise ValueError("empty set of data for the given inputs")
        return data[2][1]
    except Exception as err:
        err_msg = str(err)
        if hasattr(err, 'message'):
            err_msg = err.message
        return {"errorType": type(err).__name__, "error": err_msg}

@router.get("/GetSprite/{gen_name}/{pokemon_name}")
def get_sprite(gen_name, pokemon_name):
    """
    docstring
    """
    return {"message": "not implemented yet",
        "gen_name": gen_name,
        "pokemon_name": pokemon_name}

@router.get("/GetPokemonByGenAndTier/{gen_name}/{tier_name}")
def get_tier(gen_name, tier_name):
    """
    Parameters
    ----------
    gen_name (str)
        A string representing a generation of Pokemon games. Can be "rb" (for Red/Blue),
        "gs" (for Gold/Sliver), "rb" (for Ruby/Sapphire), "dp" (for Diamond/Pearl),
        "bw" (for Black/White), "xy" (for X/Y), "sm" (for Sun/Moon), "ss" (for Sword/Shield),
        or "sv" (for Scarlet/Violet)

    tier_name (str)
        The name of a Smogon tier for which to get data.

    Returns
    -------
    (JSON)
        A JSON object representing the Smogon data for the Pokemon from the specified Generation

    Exceptions
    ----------
    ValueError
        Will be thrown under different conditions:

            When either input is missing

            When either input is invalid

            When no data was retrieved
    """
    try:
        if not gen_name or not tier_name:
            raise ValueError("missing inputs")
        valid_gen = gen_name in valid_gens
        if not valid_gen:
            raise ValueError("invalid gen name")
        url = "https://www.smogon.com/dex/" + gen_name + "/formats/" + tier_name
        url_page = requests.get(url, timeout=100000)
        soup = bs(url_page.content, 'html.parser')

        script = soup.find_all("script")[1]
        script_insides = script.text
        data = json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs']
        if not data:
            raise ValueError("empty set of data for the given inputs")
        data= data[1][1]['pokemon']
        filtered_data = []
        for pokemon in data:
            poke_format = pokemon['formats']
            if poke_format:
                if poke_format[0].lower() == tier_name.lower():
                    filtered_data.append(pokemon)
        return filtered_data
    except Exception as err:
        err_msg = str(err)
        if hasattr(err, 'message'):
            err_msg = err.message
        return {"errorType": type(err).__name__, "error": err_msg}

@router.get("/GetItems/{gen_name}")
def get_items(gen_name):
    """
    Parameters
    ----------
    gen_name (str)
        A string representing a generation of Pokemon games. Can be "rb" (for Red/Blue),
        "gs" (for Gold/Sliver), "rb" (for Ruby/Sapphire), "dp" (for Diamond/Pearl),
        "bw" (for Black/White), "xy" (for X/Y), "sm" (for Sun/Moon), "ss" (for Sword/Shield),
        or "sv" (for Scarlet/Violet)

    Returns
    -------
    (JSON)
        A JSON object representing the Smogon data for the Pokemon from the specified Generation

    Exceptions
    ----------
    ValueError
        Will be thrown under different conditions:

            When the input is missing

            When the input is invalid

            When no data was retrieved
    """
    try:
        if not gen_name:
            raise ValueError("missing input")
        valid_gen = gen_name in valid_gens
        if not valid_gen:
            raise ValueError("invalid gen name")
        url = "https://www.smogon.com/dex/" + gen_name + "/items/"
        url_page = requests.get(url, timeout=100000)
        soup = bs(url_page.content, 'html.parser')

        script = soup.find_all("script")[1]
        script_insides = script.text
        data = json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs']
        if not data:
            raise ValueError("empty set of data for the given inputs")
        data= data[1][1]['items']
        filtered_data = []
        for item in data:
            if item['name'] != "No Item" and item['isNonstandard']=="Standard":
                filtered_data.append(item)
        return filtered_data
    except Exception as err:
        err_msg = str(err)
        if hasattr(err, 'message'):
            err_msg = err.message
        return {"errorType": type(err).__name__, "error": err_msg}

@router.get("/getTopPokemon")
def get_top_pokemon(stats: list = Query(), gen: str = Query()):
    """
    Scrapes the HTML from the Smogon Dex for the given generation. Particularly, it scrapes all
    eligible pokemon in the generation (along with their stats), compacts it into dataframe object,
    then manipulates it to get the top 5 pokemon with the highest average in the given stats, for
    each battle format.

    Parameters
    ----------
    stats (list)
        A list of strings, where each string represents a different stat (Atk, Sp. Atk, Spe, etc.)
            HP --> "hp"
            Attack --> "atk"
            Defense --> "def"
            Special Attack --> "spa"
            Special Defense --> "spd"
            Speed --> "spe"
    gen (str)
        A shorthand string representing the generation
            Red/Blue --> "rb"
            Gold/Silver --> "gs"
            Ruby/Sapphire --> "rs"
            Diamond/Pearl --> "dp"
            Black/White --> "bw"
            X/Y --> "xy"
            Sun/Moon --> "sm"
            Sword/Shield --> "ss"
            Scarlet/Violet --> "sv"

    Returns
    -------
    (JSON)
        A JSON object representing the top 5 pokemon with the highest average in the given stats,
        for each battle format in the given generation

    Exceptions
    ----------
    ValueError
        Will be thrown under different conditions:
            When stats is not a list
            When stats contains non-string items
            When stats contains invalid strings
            When gen is not a string
            When gen is an invalid string
    """
    eligible_stats = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
    eligible_gens = ['rb', 'gs', 'rs', 'dp', 'bw', 'xy', 'sm', 'ss', 'sv']
    # pylint: disable=no-else-raise
    if not isinstance(stats, list):
        raise ValueError('Stats must be a list')
    else:
        pass
    for stat in stats:
        if not isinstance(stat, str):
            raise ValueError('Stat list contains non-strings')
        else:
            pass
        if stat.lower() not in eligible_stats:
            raise ValueError('Stat list contains invalid stats')
        else:
            pass
    if not isinstance(gen, str):
        raise ValueError('Generation must be a string')
    else:
        pass
    if gen.lower() not in eligible_gens:
        raise ValueError('Not a valid generation')

    url = "https://www.smogon.com/dex/" + gen + "/pokemon/"
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')
    script = soup.find_all("script")[1]
    script_insides = script.text

    dataframe = pd.DataFrame(json.loads(script_insides.replace("dexSettings = ", "")
    .strip())['injectRpcs'][1][1]['pokemon'])
    dataframe['average'] = dataframe[stats].mean(axis=1)
    str1 = ' '
    dataframe['formats'] = dataframe['formats'].apply(str1.join)

    top_pokemon = dataframe.groupby('formats').apply(
        lambda x: x.nlargest(5, 'average')
        ).set_index('formats')
    return json.loads(json.dumps(top_pokemon.filter(
        items=['name'] + stats + ['types', 'abilities', 'average']).reset_index()
        .to_dict('records')))
