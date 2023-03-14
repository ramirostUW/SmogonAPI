"""
This module contains all of the endpoints that
primarily return scraped data from Smogon.com.
"""

import json
from fastapi import APIRouter, Query
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

router = APIRouter()

@router.get("/charizard")
def get_charizard():
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text, "html.parser")
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

@router.get("/firstOverview")
def get_first_overview(pokemon_name):
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemon_name.lower()
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = bs(script.text)
    smogon_html = script_insides.find("p").text
    first_overview = smogon_html.split("<\\/p>")[0].replace("<\\/a>", "")
    return {"overview": first_overview}

@router.get("/getJSONGen7")
def get_json(pokemon_name):
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/" + pokemon_name.lower()
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][2][1]

@router.get("/getJSONGen8")
def get_json_g8(pokemon_name):
    """
    docstring
    """
    url = "https://www.smogon.com/dex/ss/pokemon/" + pokemon_name.lower()
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][2][1]

@router.get("/getGen7Data")
def get_pokemon_data():
    """
    docstring
    """
    url = "https://www.smogon.com/dex/sm/pokemon/charizard"
    url_page = requests.get(url, timeout=100000)
    soup = bs(url_page.content, 'html.parser')

    script = soup.find_all("script")[1]
    script_insides = script.text
    return json.loads(script_insides.replace("dexSettings = ", "").strip())['injectRpcs'][1][1]

@router.get("/getTopPokemon")
# pylint: disable=unsubscriptable-object
def get_top_pokemon(stats: list[str] | None = Query(), gen: str = Query()):
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
