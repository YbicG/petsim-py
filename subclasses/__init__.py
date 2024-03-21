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

class BattleGoal():
    Quests: dict = {
        "27": "Ice Obby Completions",
        "46": "Catch Fish in Advanced Fishing",
        "34": "Use Tier 4 Potions",
        "38": "Break Comets in Best Area",
        "40": "Make Golden Pets from Best Egg",
        "44": "Break Lucky Blocks in Best Area",
        "21": "Break Breakables in Best Area",
        "39": "Break Mini-Chests in Best Area",
        "7": "Earn Diamonds",
        "37": "Break Coin Jars in Best Area",
        "43": "Break Piñatas in Best Area",
        "42": "Hatch Rare \"??\" Pets",
        "9": "Break Diamond Breakables",
        "41": "Make Rainbow Pets from Best Egg",
        "20": "Hatch Best Eggs",
        "12": "Craft Tier 3 Potions",
        "45": "Find Chests in Advanced Digsite"
    }
    
    def __init__(self, data: dict) -> None:
        self.Type: str = self.Quests.get(str(data["Type"]))
        self.TypeID: int = data["Type"]
        self.Amount: int = data["Amount"]
        self.Stars: int = data["Stars"]
        self.Progress: int = data["Progress"]
        self.Tier: int = data["Tier"]
        self.Contributions: List[BattleMember] = []
        
        for contribution_user in data["Contributions"].keys():
            battle_data: dict = {
                "UserID": int(contribution_user.replace("u", "")),
                "Points": data["Contributions"][contribution_user]
            }
            
            self.Contributions.append(BattleMember(data=battle_data))
        
        
    def __str__(self) -> str:
        return f"""{{
            "Type": {self.Type}, 
            "TypeID": {self.TypeID}, 
            "Amount": {self.Amount}, 
            "Stars": {self.Stars}, 
            "Progress": {self.Progress},
            "Tier": {self.Tier}
        }}"""
    
class Battle():
    def __init__(self, data: dict) -> None:
        self.Name: str = data["Name"]
        self.ProcessedAwards: bool = data["ProcessedAwards"]
        self.AwardUserIDs: list = data["AwardUserIDs"]
        self.BattleID: str = data["BattleID"]
        self.PointsEarned: int = data["PointsEarned"]
        self.EarnedMedal: str = data["EarnedMedal"]
        self.Goals: List[BattleGoal] | None = None
        self.Goal1: BattleGoal | None = None
        self.Goal2: BattleGoal | None = None
        self.Goal3: BattleGoal | None = None
        self.Goal4: BattleGoal | None = None
        
        self.PointContributions: List[BattleMember] = []
        
        for contribution in data["PointContributions"]:
            battle_data: dict = {
                "UserID": contribution["UserID"],
                "Points": contribution["Points"]
            }
            
            self.PointContributions.append(BattleMember(data=battle_data))
        
        if "GoalBattle" in self.BattleID:
            self.Goals: List[BattleGoal] = [BattleGoal(goal) for goal in data["Goals"]]
            self.Goal1: BattleGoal | None = self.Goals[0]
            self.Goal2: BattleGoal | None = self.Goals[1]
            self.Goal3: BattleGoal | None = self.Goals[2]
            self.Goal4: BattleGoal | None = self.Goals[3]

            
            
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