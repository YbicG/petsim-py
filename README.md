# Pet Simulator 99 API Wrapper Documentation

This document provides detailed information about the Pet Simulator 99 API Wrapper and its functionalities.

## Introduction

The Pet Simulator 99 API Wrapper is a Python library that allows you to easily access and interact with various data points from the Pet Simulator 99 game through the Big Games API. This wrapper simplifies the process of retrieving information about collections, clans, exist counts, RAP values, and active clan battles.

## Installation

You can install this package with:
```bash
pip install petsim-py
```

Example import:
```py
import petsim_api

print(petsim_api.ActiveClanBattle())
```

## Classes

The wrapper provides several classes, each representing a specific data category:

### Collections

This class allows you to retrieve a list of all available collections in the game, such as "Pets", "Achievements", "Boosts", etc.

- Use the `get_data()` method to retrieve the list of collections.
- Use the `get_status()` method to check the API status.

### Collection

This class represents a specific collection and allows you to access its data.

- Initialize the class with the desired collection name (e.g., `Collection("Pets")`).
- Use the `get_data()` method to retrieve a list of all items in the collection.
- Use the `get_info_by_name(search_by)` method to search for specific items by name within the collection.
- Use the `get_status()` method to check the API status for this collection.

### Clans

This class allows you to retrieve information about clans.

- You can specify sorting criteria using `Sort` and `SortObject` subclasses (e.g., `Clans(sort=Sort.POINTS, sort_order=Sort.DESC)`).
- Use the `get_clans()` method to retrieve a list of `Clan` objects for all clans.
- Use the `get_data()` method to retrieve the raw clan data as a list.
- Use the `get_status()` method to check the API status.

### Clan

This class represents a specific clan and provides access to its details.

- Initialize the class with the clan name (e.g., `Clan("EXP")`).
- Access various attributes like Name, Created, Owner, Members, Points, Battles, etc.
- Use the `get_data()` method to retrieve the raw clan data as a dictionary.
- Use the `get_status()` method to check the API status for this clan.

### Exists

This class allows you to retrieve exist data for all items and pets in the game.

- Use the `get_data()` method to retrieve the raw exist data as a list.
- Use the `search_for_pet(search_by, variation, shiny)` method to search for specific pets by name, variation (normal, golden, rainbow), and shiny status.
- Use the `get_status()` method to check the API status.

### RAP

This class allows you to retrieve RAP (Recent Average Price) data for all items and pets in the game.

- Use the `get_data()` method to retrieve the raw RAP data as a list.
- Use the `search_for_pet(search_by, variation, shiny)` method to search for specific pets by name, variation, and shiny status.
- Use the `get_status()` method to check the API status.

### ActiveClanBattle

This class provides details about the latest clan battle.

- Access attributes like Name, StartTime, FinishTime, Rewards, etc.
- Use the `get_data()` method to retrieve the raw active clan battle data as a dictionary.
- Use the `get_status()` method to check the API status.

## Subclasses

The wrapper also includes several subclasses that provide additional functionality and data structures:

- `Sort`: Provides options for sorting clan lists (e.g., `Sort.POINTS`, `Sort.DIAMONDS`).
- `SortObject`: Represents a specific sorting option (e.g., `Sort.ASC`, `Sort.DESC`).
- `Member`: Represents a clan member and their stats (Donated, Points, etc.).
- `BattleMember`: Represents a member's contribution to a clan battle.
- `BattleGoal`: Represents a specific goal within a clan battle.
- `Battle`: Represents a clan battle and its details (Name, PointsEarned, etc.).
- `PetExist`: Represents the exist data for a specific pet.
- `PetType`: Defines different pet variations (normal, golden, rainbow).
- `PetRap`: Represents the RAP data for a specific pet.
- `BronzeReward`, `SilverReward`, `GoldReward`: Represent different reward tiers in clan battles.
- `Rewards`: Represents all reward tiers for a clan battle.

## Usage Examples

Here are some examples of how to use the Pet Simulator 99 API Wrapper:

```python
from api_wrapper import Collections, Clan, Exists, Rap, ActiveClanBattle

# Get a list of all collections
collections = Collections()
print(collections.get_data())

# Get details about the "Pets" collection
pets_collection = Collection("Pets")
print(pets_collection.get_data())

# Search for "Huge Happy Rock" pet in the "Pets" collection
pet_info = pets_collection.get_info_by_name("Huge Happy Rock")
print(pet_info)

# Get details about the "EXP" clan
clan = Clan("EXP")
print(clan.get_data())

# Get exist data for "Huge Happy Rock" pet
exists = Exists()
pet_exist_data = exists.search_for_pet("Huge Happy Rock")
print(pet_exist_data)

# Get RAP data for "Huge Happy Rock" pet
rap = Rap()
pet_rap_data = rap.search_for_pet("Huge Happy Rock", variation="golden", shiny=True)
print(pet_rap_data)

# Get information about the latest clan battle
active_battle = ActiveClanBattle()
print(active_battle.get_data())
```

These examples demonstrate some basic functionalities of the wrapper. You can explore the various classes and methods to access more specific data points and customize your interactions with the Pet Simulator 99 API.

## Additional Notes

- This documentation provides a general overview of the wrapper's capabilities. For more detailed information about each class and method, please refer to the source code and comments.
- The Big Games API and the Pet Simulator 99 game are subject to change. This wrapper may need to be updated to reflect any changes in the API or game data structure.
- Please use this wrapper responsibly and adhere to the Big Games API terms of service.

I hope this documentation helps you effectively use the Pet Simulator 99 API Wrapper!
