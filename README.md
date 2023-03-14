# SmogonAPI
![Build/Test Workflow](https://github.com/ramirostUW/smogonAPI/actions/workflows/build_test.yml/badge.svg)[![Coverage Status](https://coveralls.io/repos/github/ramirostUW/SmogonAPI/badge.svg?branch=deployment)](https://coveralls.io/github/ramirostUW/SmogonAPI?branch=deployment)

Jason Wang, Marques J Chacon, Ramiro Steinmann Petrasso, Yangyang Yao

## Project Type
This project consists of a tool that solves a common problem for users: the inability to programmatically access Smogon data. 

## Background

Pokémon is one of the most successful multimedia franchises. According to [its producer](https://corporate.Pokemon.co.jp/en/aboutus/figures/), more than 440 million sets of Pokémon-related software and more than 43 billion Pokémon cards have been sold over the world. Such popularity creates huge demands of Pokémon-related websites and applications.

[Smogon](https://smogon.com) is an online platform for competitive Pokémon battling with over 450,000 members. Smogon also offers detailed data related to the competitive viability of each Pokémon, including information on the stats of each Pokémon, what "tier" of competition each Pokémon appears in and is legal for, as well as other information like the list of moves the Pokémon has access to. The data is publicly available through [Smogon's website](https://smogon.com) but changes quickly as new trends emerge, and is not available in a form that is easy to process in an application.

The goal of the project is to create an API that scrapes Smogon Data on the fly and packages it for use in third party applications. The application should be able to allow the user to query for a particular Smogon page like any other API endpoint, and receive the data packaged in JSON or CSV format.

## Goal for the Project
The goal of the project is to create an API that scrapes Smogon Data on the fly and packages it for use in third party applications. The application should be able to allow the user to query for a particular Smogon page like any other API endpoint, and receive the data packaged in JSON or CSV format.

## How to use:
First, make sure your Python version is either 3.8, 3.9, or 3.10

Then, run `pip install .`  . This will install of the necessary requirements for you. 

After you do so, you can run the API locally by running `uvicorn smogonapi.smogonapi.main:myApp --reload` .

## Questions of Interest
This project does not center around any particular question, but questions of minor interest include what type of data users will query most (I.E. tier data, individual Pokemon data, etc.), and if there's any supplemental data sources that could be scraped and joined with data from Smogon to supplement queries (I.E. Bulbapedia data)

## Data Sources Used:

(The static dataset is used to provide static data for supplemental queries like the evolutionary requirements of a Pokemon, which is not available directly on Smogon but is useful regardless). 


- https://smogon.com
- https://www.kaggle.com/datasets/mrdew25/pokemon-database