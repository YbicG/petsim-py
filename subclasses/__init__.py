from typing import List, Dict

class PetType():
    Dictionary: dict = {"normal": 0, "golden": 1, "rainbow": 2}
    Golden: int = 1
    Rainbow: int = 2
    Sh: bool = False
    
class SortObject():
    def __init__(self, value: str) -> None:
        self.value: str = value
    
    def __str__(self) -> str:
        return self.value
    
class Sort():
    POINTS: SortObject = SortObject("Points")
    DIAMONDS: SortObject = SortObject("DepositedDiamonds")
    CREATION_DATE: SortObject = SortObject("Created")
    
    ASC: SortObject = SortObject("asc")
    DESC: SortObject = SortObject("desc")

class Member():
    def __init__(self, data: dict) -> None:
        self.UserID: int = data["UserID"]
        self.PermissionLevel: int = data["PermissionLevel"]
        self.JoinTime: int = data["JoinTime"]
        self.Donated: int = data["Donated"]
        self.Points: int = data["Points"]
        
    def __str__(self) -> str:
        return f"""{{
            "Donated": {self.Donated}, 
            "Points": {self.Points}, 
            "UserID": {self.UserID}, 
            "PermissionLevel": {self.PermissionLevel}, 
            "JoinTime": {self.JoinTime}
        }}"""
    
class BattleMember():
    def __init__(self, data: dict) -> None:
        self.UserID: int = data["UserID"]
        self.Points: int = data["Points"]
        
    def __str__(self) -> str:
        return f"""{{
            "UserID": {self.UserID},
            "Points": {self.Points}
        }}"""
        
class Battle():
    def __init__(self, data: dict) -> None:
        self.Name: str = data["Name"]
        self.ProcessedAwards: bool = data["ProcessedAwards"]
        self.AwardUserIDs: list = data["AwardUserIDs"]
        self.BattleID: str = data["BattleID"]
        self.PointsEarned: int = data["PointsEarned"]
        self.EarnedMedal: str = data["EarnedMedal"]
        
        
        self.PointContributions: List[BattleMember] = []
        
        for contribution in data["PointContributions"]:
            battle_data: dict = {
                "UserID": contribution["UserID"],
                "Points": contribution["Points"]
            }
            
            self.PointContributions.append(BattleMember(data=battle_data))
            
    def __str__(self) -> str:
        return f"""{{
            "Name": {self.Name}, 
            "ProcessedAwards": {self.ProcessedAwards}, 
            "AwardUserIDs": {self.AwardUserIDs}, 
            "BattleID": {self.BattleID}, 
            "PointsEarned": {self.PointsEarned}, 
            "PointContributions": {self.PointContributions},
            "EarnedMedal": {self.EarnedMedal}
        }}"""
    
class PetExist():
    def __init__(self, data: dict) -> None:
        self.Category: str = data["Category"]
        self.Id: str = data["ConfigData"]["Id"]
        self.Variation: str = "Normal"
        self.IsShiny: bool = False
        self.ExistCount: int = data["Value"]
        
        if "Pt" in data["ConfigData"]:
            if data["ConfigData"]["Pt"] == PetType.Golden:
                self.Variation: str = "Golden"
            elif data["ConfigData"]["Pt"] == PetType.Rainbow:
                self.Variation: str = "Rainbow"
        
        if "Sh" in data["ConfigData"]:
            if data["ConfigData"]["Sh"] == True:
                self.IsShiny: bool = True
                
    def __str__(self) -> str:
        return f"""{{
            "Category": {self.Category}, 
            "Id": {self.Id}, 
            "Variation": {self.Variation}, 
            "IsShiny": {self.IsShiny}, 
            "ExistCount": {self.ExistCount},
        }}"""
    

class PetRap():
    def __init__(self, data: dict) -> None:
        self.Category: str = data["Category"]
        self.Id: str = data["ConfigData"]["Id"]
        self.Variation: str = "Normal"
        self.IsShiny: bool = False
        self.Rap: int = data["Value"]
        
        if "Pt" in data["ConfigData"]:
            if data["ConfigData"]["Pt"] == PetType.Golden:
                self.Variation: str = "Golden"
            elif data["ConfigData"]["Pt"] == PetType.Rainbow:
                self.Variation: str = "Rainbow"
        
        if "Sh" in data["ConfigData"]:
            if data["ConfigData"]["Sh"] == True:
                self.IsShiny: bool = True     
    
    def __str__(self) -> str:
        return self.Id           

class BronzeReward():
    def __init__(self, data: dict) -> None:
        self.Booth: str = data["Booth"]
        
    def __str__(self) -> str:
        return f"""{{
            "Booth": {self.Booth}
        }}"""

class SilverReward():
    def __init__(self, data: dict) -> None:
        self.Hoverboard: str = data["Hoverboard"]
        self.Booth: str = data["Booth"]
        self.EggCount: int = data["EggCount"]
        self.Egg: str = data["Egg"]
        

    def __str__(self) -> str:
        return f"""{{
            "Booth": {self.Booth}
            "Hoverboard": {self.Hoverboard}, 
            "EggCount": {self.EggCount}, 
            "Egg": {self.Egg},
        }}"""
    
class GoldReward():
    def __init__(self, data: dict) -> None:
        self.Huge: str = data["Huge"]
        self.Hoverboard: str = data["Hoverboard"]
        self.Booth: str = data["Booth"]
        self.EggCount: int = data["EggCount"]
        self.Egg: str = data["Egg"]
        

    def __str__(self) -> str:
        return f"""{{
            "Huge": {self.Huge}, 
            "Booth": {self.Booth},
            "Hoverboard": {self.Hoverboard}, 
            "EggCount": {self.EggCount}, 
            "Egg": {self.Egg},
        }}"""
    
class Rewards():
    def __init__(self, data: dict) -> None:
        self.Bronze: BronzeReward = BronzeReward(data=data["Bronze"])
        self.Silver: SilverReward = SilverReward(data=data["Silver"])
        self.Gold: GoldReward = GoldReward(data=data["Gold"])

    
    def __str__(self) -> str:
        return self.Id