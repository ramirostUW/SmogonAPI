<h1 align="center"> Functional Specification </h1>

## Background
Pokémon is one of the most successful multimedia franchises. According to [its producer](https://corporate.Pokemon.co.jp/en/aboutus/figures/), more than 440 million sets of Pokémon-related software and more than 43 billion Pokémon cards have been sold over the world. Such popularity creates huge demands of Pokémon-related websites and applications.

[Smogon](https://smogon.com) is an online platform for competitive Pokémon battling with over 450,000 members. Smogon also offers detailed data related to the competitive viability of each Pokémon, including information on the stats of each Pokémon, what "tier" of competition each Pokémon appears in and is legal for, as well as other information like the list of moves the Pokémon has access to. The data is publicly available through [Smogon's website](https://smogon.com) but changes quickly as new trends emerge, and is not available in a form that is easy to process in an application.

The goal of the project is to create an API that scrapes Smogon Data on the fly and packages it for use in third party applications. The application should be able to allow the user to query for a particular Smogon page like any other API endpoint, and receive the data packaged in JSON or CSV format.

## Data Sources
### Main Source
- https://smogon.com
### Supplemental static dataset
- https://www.kaggle.com/datasets/mrdew25/pokemon-database

The static dataset is used to provide static data for supplemental queries like the evolutionary requirements of a Pokemon, which is not available directly on Smogon but is useful regardless.

## User Profiles
### User A
User A is a competitive Pokémon player who wants to know what strategies would best suit the Pokémon she has. She wants to use the Smogon API to retrieve the StrategyDex for a given Pokémon, and a particular generation. She does not have any particular technical skills, but wants to be able to query for the best available strategies using a simple user interface.

### User B
User B is a casual Pokémon player who wants to know the in-game locations of different items he needs to complete his game. He wants to be able to query the item, as well as the game. He does not have any particular technical knowledge.

### User C
User C is a data scientist. She wants to create a dashboard that visualizes information that she is able to pull from the Smogon API. For instance, she wants to show the stat distribution of different Pokémon across generations. She also wants to highlight how different Pokémon have changed competitive format tiers across time. She has skills in visualizing data from CSV and JSON files.

### User D
User D is a mobile app developer who is interested in creating a tool that translates Pokémon data into an Arabic Pokémon Encyclopedia. He is able to know how to pull data from the API, and create a translator tool that can translate the information. He also has experience with creating websites and web design.

## Use Cases
### Check StrategyDex
**Objective:** The user is preparing for a Pokémon battle. In order to refer to Pokémon strategies during the battle, she wants to have access to Pokémon strategies without having to visit Smogon and look for her Pokémon in the browser. This use case is pratical for competitive Pokémon players such as user A.

**Expected Interactions:** The user specifies the name of a Pokémon or item and the generation ti belongs to. The API pulls the Strategy Dex Page for the Pokémon or item from Smogon.


### Get In-Game Items
**Objective:** The user is stuck while playing a Pokémon series game. He cannot find a powerful item in the game, and he wants some instructions about the in-game location of the item. As the latest generation of Pokémon series games has been released recently, this use case can be common among casual Pokémon players.

**Expected Interactions:** The user selects the game he is playing and specifies the name of the item. The API returns the in-game location of the given item that the user specifies.

### Query Pokémon Data
**Objective:** The user wants to query a list of Pokémons or items in a form that is easy to process in an application, such as a CSV file. This use case is common for Pokémon content creators such as user C and D.

**Expected Interactions:** The user inputs a list of Pokémons or items and the generations they belong to. The API returns a CSV file of different Pokémon statistics, based on the inputs that the user provides.