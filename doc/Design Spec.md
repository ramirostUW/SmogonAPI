<h1 align="center"> Design Specification </h1>

## Overview
The Smogon API system consist of the following components
* User facing API interface
* Service request handler
* Smogon webpage URL generator
* Smogon webpage crawler

## Software Components Specifications

### Component 1 - User facing API interface
* Name: User facing API interface
* What it does: Defines the API interface for the Smogon API, including input/output data schemas and the function signatures.
* Inputs: N/A since this is an interface
* Outputs: N/A since this is an interface
* Assumptions: Users will be able to directly submit requests to the Smogon API through this interface without any additional setup.

### Component 2 - Service request handler
* Name: Smogon API service request handler
* What it does: Server side code that handles the request to response process, including authentication, throttling, and error handling methods such as auto-retry and error message communication.
* Inputs: Smogon API get Pokémon information request
* Outputs: Smogon API get Pokémon information response
* Assumptions: The application logic can be deployed as a service without additional configurations

### Component 3 - Smogon webpage URL generator
* Name: Smogon webpage URL generator
* What it does: Generates Smogon webpage URL link with given Pokémon name
* Inputs: Pokémon name
* Outputs: Smogon webpage link of the given Pokémon
* Assumptions: The logic of generating Smogon webpage link from Pokémon name is deterministic.

### Component 4 - Smogon webpage crawler
* Name: Smogon webpage crawler
* What it does: Crawls the Smogon webpage and parses the body to extract the Pokémon information that is required to construct the API response
* Inputs: Smogon webpage URL
* Outputs: Detailed Pokémon information with specific format
* Assumptions: The Smogon website is always available and will not throttle

## Interactions

The following diagram depicts the interaction between the listed components

![](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgU21vZ29uIEFQSQoKVXNlci0-QVBJIFNlcnZlcjogUG9rZW1vbiBpbmZvcm1hdGlvbiByZXF1ZXN0CgAeCi0-AD8HVVJMIEdlbmVyYXRvcjogUgAkBgA9CXdlYnBhZ2UgVVJMCgAeFABuDlJldHVybgAoFQBvDFdlYiBjcmF3bGVyOiBTdWJtaXQgdwAKCgCBJwggd2l0aAB1BQAmCwCBMAlXZWJzaXRlOiBBY2Nlc3MAgg4IAIEqBwCBJQgAHwcAZBAAHw0gYm9keQBWDgCCORggcGFyc2VkIGZyb20AYgkAgkoMVXMAgXsNAIJ6Ego&s=default)

### Check Best Pokémons

*User:* Goes to "getTopPokemon" endpoint

*User:* Adds "stats=atk" for the attack stat

*User:* Appends "&gen=sv" for the Scarlet & Violet generation

*API:* Returns a JSON object that contains a list of five Pokémons with highest attack stat in the Scarlet & Violet generation. If the generation or stat is not found, it returns an error page.

*User:* Appends "&stats=spd" to take the speed into consideration

*API:* Returns a JSON object that contains a list of five Pokémons with highest average stat of attack and speed. If the generation or stat is not found, it returns an error page.

### Get Generation Items

*User:* Goes to "GetItems" endpoint

*User:* Adds "/ss" for the Sword & Shield generation

*API:* Returns a JSON object that contains a list of items available in the Sword & Shield generation. If the generation is not found, it returns an error page.

### Query Pokémon Data

*User:* Goes to "GetPokemonByGen" endpoint

*User:* Adds "/sv" for the Scarlet & Violet generation

*API:* Returns a JSON object that contains a list of Pokémons in the Scarlet & Violet generation. If the generation is not found, it returns an error page.

## Preliminary Plan

**Week 6**
- Determine the goal and scope of the project
- Create README.md and LICENSE file

**Week 7**
- Explore the structure and format of the html pages of Smogon
- Finish user stories and use cases of the API

**Week 8**
- Confirm Python packages to implement the web crawler and deploy the API
- Figure out how to deploy the API
- Prepare for technology review presentation and demo

**Week 9**
- Refine endpoints for FastAPI
- Extract Pokémon gen 1-8 and gen 9 dataset from supplemental data sources
- Add environment and dependency files of the API

**Week 10-11**
- Implement setup.py file
- Create unit tests for the API
- Add documentation of codes and improve code style with pylint
- Finalize design and functional documentation
- Prepare for final project presentation