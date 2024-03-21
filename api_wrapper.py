import requests
import json
from requests import Request
from typing import List
from api import APIRequest, APIResponse
from subclasses import Sort, SortObject, Member, Battle, PetExist, PetType, PetRap

BASE_URL: str = "https://biggamesapi.io/api"

# Wrapper Start

class Collections(APIRequest):
    """
    Types of data from Pet Simulator 99's in-game configuration files. Each of these may be queried. These are like tables of a database.
    """
    # Constants
    PETS: str = "Pets"
    ACHIEVEMENTS: str = "Achievements"
    BOOSTS: str = "Boosts"
    BOOTHS: str = "Booths"
    BOXES: str = "Boxes"
    BUFFS: str = "Buffs"
    CHARMS: str = "Charms"
    CURRENCY: str = "Currency"
    EGGS: str = "Eggs"
    ENCHANTS: str = "Enchants"
    FISHINGRODS: str = "FishingRods"
    FRUITS: str = "Fruits"
    GUILDBATTLES: str = "GuildBattles"
    HOVERBOARDS: str = "Hoverboards"
    LOOTBOXES: str = "Lootboxes"
    MASTERY: str = "Mastery"
    MISCITEMS: str = "MiscItems"
    PETS: str = "Pets"
    POTIONS: str = "Potions"
    RANDOMEVENTS: str = "RandomEvents"
    RANKS: str = "Ranks"
    RARITY: str = "Rarity"
    REBIRTHS: str = "Rebirths"
    SECRETROOMS: str = "SecretRooms"
    SEEDS: str = "Seeds"
    SHOVELS: str = "Shovels"
    SPRINKLERS: str = "Sprinklers"
    ULTIMATES: str = "Ultimates"
    UPGRADES: str = "Upgrades"
    WATERINGCANS: str = "WateringCans"
    WORLDS: str = "Worlds"
    ZONEFLAGS: str = "ZoneFlags"
    ZONES: str = "Zones"

    api_url: str = BASE_URL+"/collections"
    
    def __init__(self) -> None:
        """
        Types of data from Pet Simulator 99's in-game configuration files. Each of these may be queried. These are like tables of a database.
        """
        super().__init__()
        
    def get_data(self) -> list:
        """Retrieves the collections data.

        Returns:
            list: The raw list of all collections.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_data()
    
    def get_status(self) -> str:
        """Retrieves the status of the collections api.

        Returns:
            str: Current status.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_status()
    
# TODO: Add wrappers for each individual collection. Such as Pets, Achievements, etc.
class Collection(APIRequest):
    """
    The details from the specified collection. This contains a list of configuration data from the game configuration files. These are like rows of a database.
    """
    
    api_url: str = BASE_URL+"/collection/"
    
    def __init__(self, collection_name: str) -> None:
        """
        The details from the specified collection. This contains a list of configuration data from the game configuration files. These are like rows of a database.
        """
        super().__init__()
        self.api_url += collection_name
        
        self.Name = collection_name
        
    def get_data(self) -> list:
        """Retrieves the list from the collection.

        Returns:
            list: The raw list of data in a collection.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_data()
    
    def get_info_by_name(self, search_by: str) -> list | dict:
        """Queries the collection by name and returns matching results.

        Args:
            search_by (str): The name of the item to search by. This could be a pet, achievement, quest, hoverboard, loot item, rebirth, etc.

        Returns:
            list | dict: This returns either a dictionary with 1 search result, or a list with dictionaries of all of the matching search results.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        
        response_list: list = []
        
        for response in api_response.get_data():
            if search_by.lower() in response["configName"].lower():
                response_list.append(response)
        
        if len(response_list) == 0:
            return None
        
        response_list: list = response_list if len(response_list) > 1 else response_list[0]
        
        return response_list
             
    
    def get_status(self) -> str:
        """Retrieves the status of the collection api.

        Returns:
            str: Current status.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_status()
    
    def __str__(self) -> str:
        return self.Name

class Clans(APIRequest):
    """
    An overview of all the clans. All query params are required but the default ones are set.
        - Options for sort: Sort.DIAMONDS, Sort.POINTS, and Sort.CREATION_DATE
        - Options for sortOrder: Sort.ASC, Sort.DESC
    """
    
    api_url: str = BASE_URL+"/clans"
    
    def __init__(self, page: int = 1, page_size: int = 10, sort: SortObject | str = Sort.POINTS, sort_order: SortObject | str = Sort.DESC) -> None:
        """
        An overview of all the clans. All query params are required but the default ones are set.
            - Options for sort: Sort.DIAMONDS, Sort.POINTS, and Sort.CREATION_DATE
            - Options for sortOrder: Sort.ASC, Sort.DESC
        """
        super().__init__()
        self.parameters: dict = {
            "page": page, 
            "pageSize": page_size, 
            "sort": sort, 
            "sortOrder": sort_order
        }
    
    def get_clans(self) -> list:
        """Retrieves the clan list formateted as Clan classes.

        Returns:
            list: The raw list of all Clan classes sorted by what is specified.
        """
        raw_data: list = self.get_data()
        
        response_data: List[Clan] = []
        
        for clan in raw_data:
            name: str = clan["Name"]
            clan: Clan = Clan(clan_name=name)
            response_data.append(clan)
            
        return response_data
            
    def get_data(self) -> list:
        """Retrieves the clan list.

        Returns:
            list: The raw list of all clans sorted by what is specified.
        """
        
        api_response: APIResponse = self.http_get(self.api_url, parameters=self.parameters)
        return api_response.get_data()
             
    def get_status(self) -> str:
        """Retrieves the status of the clans api.

        Returns:
            str: Current status.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_status()

class Clan(APIRequest):
    """
    The details of a specific clan.
    """
    api_url: str = BASE_URL+"/clan/"
    
    def __init__(self, clan_name: str) -> None:
        """
        The details of a specific clan.
        """
        super().__init__()
        self.api_url += clan_name
    
        data: dict = self.get_data()
        
        # Attributes
        self.Created: int = data["Created"]
        self.Owner: int = data["Owner"]
        self.Name: str = data["Name"]
        self.Icon: str  = data["Icon"]
        self.Desc: str = data["Desc"]
        self.CountryCode: str = data["CountryCode"]
        self.MemberCapacity: int = data["MemberCapacity"]
        self.OfficerCapacity: int = data["OfficerCapacity"]
        self.GuildLevel:int  = data["GuildLevel"]
        self.LastKickTimestamp: int = data["LastKickTimestamp"] 
        self.Members: List[Member] = []
        self.MemberCount: int = 0
        self.DepositedDiamonds: int = data["DepositedDiamonds"]
        self.Status: str = data["Status"] if "Status" in data else None
        self.StatusTimestamp: int = data["StatusTimestamp"] if "StatusTimestamp" in data else None
        self.StatusUsername: str = data["StatusUsername"] if "StatusUsername" in data else None
        self.Battles: List[Battle] = []
        self.Points: int = 0
        
        
        most_recent_clan_battle: dict = data["Battles"][list(data["Battles"].keys())[-1]]
        
        for member in data["Members"]:
            donated: int = 0
            points: int = 0
            
            for contribution in data["DiamondContributions"]["AllTime"]["Data"]:
                if contribution["UserID"] == member["UserID"]:
                    donated: int = contribution["Diamonds"]
            
            for contribution in most_recent_clan_battle["PointContributions"]:
                if contribution["UserID"] == member["UserID"]:
                    points: int = contribution["Points"]
            
            member_data: dict = {
                "Donated": donated, 
                "Points": points, 
                "UserID": member["UserID"], 
                "PermissionLevel": member["PermissionLevel"], 
                "JoinTime": member["JoinTime"]
            }
            
            self.Members.append(Member(data=member_data))
           
        for battle_key in data["Battles"].keys():
            battle: dict = data["Battles"][battle_key]
            
            battle_data: dict = {
                "Name": battle_key,
                "ProcessedAwards": battle["ProcessedAwards"], 
                "AwardUserIDs": battle["AwardUserIDs"], 
                "BattleID": battle["BattleID"], 
                "PointsEarned": battle["Points"], 
                "PointContributions": battle["PointContributions"],
                "EarnedMedal": battle["EarnedMedal"] if "EarnedMedal" in battle else None,
            }
            
            self.Battles.append(Battle(data=battle_data))      
        
        self.MemberCount: int = len(self.Members)
        self.Points: int = most_recent_clan_battle["Points"]
        
    def get_data(self) -> list:
        """Retrieves the clan data.

        Returns:
            list: The raw list of data in a clan.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_data() 
             
    def get_status(self) -> str:
        """Retrieves the status of the clan api.

        Returns:
            str: Current status.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_status()
    
    def __str__(self) -> str:
        return self.Name

class Exists(APIRequest):
    """
    Exists data for each item and pet in the game.
    """
    
    api_url: str = BASE_URL+"/exists"
    
    def __init__(self) -> None:
        super().__init__()
        
    def get_data(self) -> list:
        """Retrieves the exist count of all of the pets in a list.

        Returns:
            list: The raw list of data in the exist count list.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_data()
    
    def search_for_pet(self, search_by: str, variation: str = "normal", shiny: bool = False) -> PetExist | List[PetExist]:
        """Queries the exists by name and returns matching results.

        Args:
            search_by (str): The name of the pet to search for.
            variation (str): Which variation pet to look for, options "rainbow", "golden", or "normal".
            shiny (bool): Whether to filter by shiny or not.

        Returns:
            list | dict: This returns either a dictionary with 1 search result, or a list with dictionaries of all of the matching search results.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        
        response_list: list = []
        
        for response in api_response.get_data():
            if search_by.lower() in response["configData"]["id"].lower():
                if variation == "normal" and not shiny:
                    if "pt" not in response["configData"] and "sh" not in response["configData"]:
                        pet_data: dict = {
                            "Category": response["category"],
                            "ConfigData": {
                                "Id": response["configData"]["id"], 
                                "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                },
                            "Value": response["value"]
                        }
                        
                        pet: PetExist = PetExist(data=pet_data)

                        response_list.append(pet)   
                    
                elif variation != "normal" and not shiny:
                    if "pt" in response["configData"]:
                        if response["configData"]["pt"] == PetType.Dictionary[variation] and "sh" not in response["configData"]:
                            pet_data: dict = {
                                "Category": response["category"],
                                "ConfigData": {
                                    "Id": response["configData"]["id"], 
                                    "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                    "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                    },
                                "Value": response["value"]
                            }
                    
                            pet: PetExist = PetExist(data=pet_data)

                            response_list.append(pet)
                elif variation != "normal" and  shiny:
                    if "pt" in response["configData"] and "sh" in response["configData"]:
                        if response["configData"]["pt"] == PetType.Dictionary[variation]:
                            if response["configData"]["sh"] == shiny:
                                pet_data: dict = {
                                    "Category": response["category"],
                                    "ConfigData": {
                                        "Id": response["configData"]["id"], 
                                        "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                        "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                        },
                                    "Value": response["value"]
                                }
                    
                                pet: PetExist = PetExist(data=pet_data)

                                response_list.append(pet)
                                
                elif variation == "normal" and shiny:
                    if "sh" in response["configData"]:
                        if response["configData"]["sh"] == shiny and "pt" not in response["configData"]:
                            pet_data: dict = {
                                "Category": response["category"],
                                "ConfigData": {
                                    "Id": response["configData"]["id"], 
                                    "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                    "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                    },
                                "Value": response["value"]
                            }
                    
                            pet: PetExist = PetExist(data=pet_data)

                            response_list.append(pet)
        
        if len(response_list) == 0:
            return None
        
        response_list: list = response_list if len(response_list) > 1 else response_list[0]
        
        return response_list
             
    
    def get_status(self) -> str:
        """Retrieves the status of the exists api.

        Returns:
            str: Current status.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_status()

class Rap(APIRequest):
    """
    RAP data for each item and pet in the game.
    """
    
    api_url: str = BASE_URL+"/rap"
    
    def __init__(self) -> None:
        super().__init__()
        
    def get_data(self) -> list:
        """Retrieves the rap count of all of the pets in a big list.

        Returns:
            list: The raw list of data in the raps count list.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_data()
    
    def search_for_pet(self, search_by: str, variation: str = "normal", shiny: bool = False) -> PetRap | List[PetRap]:
        """Queries the exists by name and returns matching results.

        Args:
            search_by (str): The name of the pet to search for.
            variation (str): Which variation pet to look for, options "rainbow", "golden", or "normal".
            shiny (bool): Whether to filter by shiny or not.

        Returns:
            list | dict: This returns either a dictionary with 1 search result, or a list with dictionaries of all of the matching search results.
        """
        
        api_response: APIResponse = self.http_get(self.api_url)
        
        response_list: list = []
        
        for response in api_response.get_data():
            if search_by.lower() in response["configData"]["id"].lower():
                if variation == "normal" and not shiny:
                    if "pt" not in response["configData"] and "sh" not in response["configData"]:
                        pet_data: dict = {
                            "Category": response["category"],
                            "ConfigData": {
                                "Id": response["configData"]["id"], 
                                "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                },
                            "Value": response["value"]
                        }
                        
                        pet: PetRap = PetRap(data=pet_data)

                        response_list.append(pet)
                    
                elif variation != "normal" and not shiny:
                    if "pt" in response["configData"]:
                        if response["configData"]["pt"] == PetType.Dictionary[variation] and "sh" not in response["configData"]:
                            pet_data: dict = {
                                "Category": response["category"],
                                "ConfigData": {
                                    "Id": response["configData"]["id"], 
                                    "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                    "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                    },
                                "Value": response["value"]
                            }
                    
                            pet: PetRap = PetRap(data=pet_data)

                            response_list.append(pet)
                elif variation != "normal" and  shiny:
                    if "pt" in response["configData"] and "sh" in response["configData"]:
                        if response["configData"]["pt"] == PetType.Dictionary[variation]:
                            if response["configData"]["sh"] == shiny:
                                pet_data: dict = {
                                    "Category": response["category"],
                                    "ConfigData": {
                                        "Id": response["configData"]["id"], 
                                        "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                        "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                        },
                                    "Value": response["value"]
                                }
                    
                                pet: PetRap = PetRap(data=pet_data)

                                response_list.append(pet)
                                
                elif variation == "normal" and shiny:
                    if "sh" in response["configData"]:
                        if response["configData"]["sh"] == shiny and "pt" not in response["configData"]:
                            pet_data: dict = {
                                "Category": response["category"],
                                "ConfigData": {
                                    "Id": response["configData"]["id"], 
                                    "Pt": response["configData"]["pt"] if "pt" in response["configData"] else None,
                                    "Sh": response["configData"]["sh"] if "sh" in response["configData"] else None
                                    },
                                "Value": response["value"]
                            }
                    
                            pet: PetRap = PetRap(data=pet_data)

                            response_list.append(pet)
        
        if len(response_list) == 0:
            return None
        
        response_list: list = response_list if len(response_list) > 1 else response_list[0]
        
        return response_list
             
    
    def get_status(self) -> str:
        """Retrieves the status of the exists api.

        Returns:
            str: Current status.
        """
        api_response: APIResponse = self.http_get(self.api_url)
        return api_response.get_status()
    
# End Wrappers