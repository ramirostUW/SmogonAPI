<h1 align="center"> Functional Specification </h1>

## Background
Pokémon is one of the most successful multimedia franchises. According to [its producer](https://corporate.Pokemon.co.jp/en/aboutus/figures/), more than 440 million sets of Pokémon-related software and more than 43 billion Pokémon cards have been sold over the world. Such popularity creates huge demands of Pokémon-related websites and applications.

[Smogon](https://smogon.com) is an online platform for competitive Pokémon battling with over 450,000 members. Smogon also offers detailed data related to the competitive viability of each Pokémon, including information on the stats of each Pokémon, what "tier" of competition each Pokémon appears in and is legal for, as well as other information like the list of moves the Pokémon has access to. The data is publicly available through [Smogon's website](https://smogon.com) but changes quickly as new trends emerge, and is not available in a form that is easy to process in an application.

The goal of the project is to create an API that scrapes Smogon Data on the fly and packages it for use in third party applications. The application should be able to allow the user to query for a particular Smogon page like any other API endpoint, and receive the data packaged in JSON or CSV format.

## Data Sources
### Main Source
- https://smogon.com
### Supplemental static datasets
- https://www.kaggle.com/datasets/notlucasp/Pokemon-gen-18-dataset
- https://www.kaggle.com/datasets/timbuck/Pokemon-generation-9-scarlet-violet-datasets

The two static datasets will be used to provide static data for basic queries like listing Pokémon in a gen, to avoid making unnecessary scrapes. We have a separate dataset for gens 1-8 and gen 9 because we could not find a complete dataset that went past gen 8, due to the recent release of gen 9.

## User Profiles
### User Alpha
User Alpha wants to practice his web development skills. They decide to make a reproduction of Smogon.com, because they are passionate about competitive Pokémon and want to make something they are interested in. In order to do so, they will need a way to access the Smogon data.

### User Brown
User Brown is a data science student. They are taking a data visualization course and have been assigned a project where they must display a dataset of their choice. They decide to to make a bar graph showing how the average attack stat for a Pokémon has changed across Pokémon generations. To do so, they need to find data on Pokémon by gen so they can aggregate Attack Stat values.

### User Charlie
User Charlie is a competitive Pokémon player and amateur coder. They would like a faster way to build teams than to scroll through each Pokémon's Smogon page and check which one has sample sets. They decide to write a program to find the sample sets ror Pokémon with high values in a certain stat.

## Use Cases
### Check Best Pokémons
**Objective:** User Charlie is preparing for a Pokémon battle. They want to have a quick look at best Pokémons on certain stats, such as Attack and Speed. They also want to find Pokémons with top stats on average.

**Expected Interactions:** User Charlie inputs the generation of the Pokémon and the stat they are looking for. They input a certain stat, and the API returns top 5 Pokémons that are at peak for this stat. To find Pokémons with top stats on average, they input a list of stats, and the API returns 5 Pokémons with highest average stats.

### Get Generation Items
**Objective:** User Alpha is adding descriptions to items in a generation for a reproduction of Smogon.com. They want to extract item descriptions from Smogon, but they don't want to parse the whole page that contains a lot of unnecessary information and look for texts they want.

**Expected Interactions:** User Alpha turns to the GetItems endpoint and inputs the generation they look for. The API returns a JSON that contains all items in that generation, including "description" attribute that contains item descriptions.

### Query Pokémon Data
**Objective:** User Brown is working on a bar graph showing how the average attack stat for a Pokémon has changed across Pokémon generations. They want to query Attack Stat values of a Pokémon name Pikachu in a list of generations, and they want the data in a form that is easy to process for data visualization, such as a JSON object.

**Expected Interactions:** At endpoint GetPokemonByGen, User Brown inputs the generation they want to query. The API returns a JSON object of all Pokémon data in that generation. User Brown filters the JSON object with "name" attribute and finds the data of Pikachu.