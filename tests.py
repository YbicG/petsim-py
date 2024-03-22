import unittest
from api_wrapper import Collections, Collection, Clans, Clan, Exists, Rap, APIRequest, APIResponse
from api_wrapper.subclasses import Sort, SortObject, Member, Battle, PetExist, PetType, PetRap, BattleMember

class TestCollections(unittest.TestCase):
    def test_get_data(self):
        collections = Collections()
        data = collections.get_data()
        self.assertIsInstance(data, list)

    def test_get_status(self):
        collections = Collections()
        status = collections.get_status()
        self.assertIsInstance(status, str)

class TestCollection(unittest.TestCase):
    def test_get_data(self):
        collection = Collection("Pets")
        data = collection.get_data()
        self.assertIsInstance(data, list)

    def test_get_info_by_name(self):
        collection = Collection("Pets")
        pet_info = collection.get_info_by_name("Flamingo")
        self.assertIsNotNone(pet_info)

    def test_get_status(self):
        collection = Collection("Pets")
        status = collection.get_status()
        self.assertIsInstance(status, str)

class TestClans(unittest.TestCase):
    def test_get_clans(self):
        clans = Clans()
        clan_list = clans.get_clans()
        self.assertIsInstance(clan_list, list)
        self.assertIsInstance(clan_list[0], Clan)

    def test_get_data(self):
        clans = Clans()
        data = clans.get_data()
        self.assertIsInstance(data, list)

    def test_get_status(self):
        clans = Clans()
        status = clans.get_status()
        self.assertIsInstance(status, str)

class TestClan(unittest.TestCase):
    def test_get_data(self):
        clan = Clan("EXP")
        data = clan.get_data()
        self.assertIsInstance(data, dict)

    def test_get_status(self):
        clan = Clan("EXP")
        status = clan.get_status()
        self.assertIsInstance(status, str)

class TestExists(unittest.TestCase):
    def test_get_data(self):
        exists = Exists()
        data = exists.get_data()
        self.assertIsInstance(data, list)

    def test_search_for_pet(self):
        exists = Exists()
        pet_info = exists.search_for_pet("Huge Happy Rock")
        self.assertIsNotNone(pet_info)

    def test_get_status(self):
        exists = Exists()
        status = exists.get_status()
        self.assertIsInstance(status, str)

class TestRap(unittest.TestCase):
    def test_get_data(self):
        rap = Rap()
        data = rap.get_data()
        self.assertIsInstance(data, list)

    def test_search_for_pet(self):
        rap = Rap()
        pet_info = rap.search_for_pet("Huge Happy Rock")
        self.assertIsNotNone(pet_info)

    def test_get_status(self):
        rap = Rap()
        status = rap.get_status()
        self.assertIsInstance(status, str)

class TestSubclasses(unittest.TestCase):
    def test_sort_object(self):
        sort_obj = SortObject("Points")
        self.assertEqual(str(sort_obj), "Points")

    def test_member(self):
        member_data = {"Donated": 100, "Points": 50, "UserID": 123, "PermissionLevel": 2, "JoinTime": 1679012345}
        member = Member(member_data)
        self.assertEqual(member.Donated, 100)
        self.assertEqual(member.Points, 50)

    def test_battle(self):
        battle_data = {
            "Name": "DecemberActiveHugePets", 
            "ProcessedAwards": True, 
            "AwardUserIDs": [1331231231, 1231313], 
            "BattleID": "DecemberActiveHugePets", 
            "PointsEarned": 231313, 
            "PointContributions": [{"UserID": 2313123, "Points": 2313123}],
            "EarnedMedal": None
        }
        
        battle = Battle(battle_data)
        self.assertEqual(battle.Name, "DecemberActiveHugePets")

    def test_pet_exist(self):
        pet_exist_data = {
            "Category": "Pet",
            "ConfigData": {
                "Id": "Huge Happy Rock", 
                "Pt": None,
                "Sh": True
            },
            "Value": 999
        }
        pet_exist = PetExist(pet_exist_data)
        self.assertEqual(pet_exist.Category, "Pet")
        self.assertEqual(pet_exist.IsShiny, True)
        self.assertEqual(pet_exist.Variation, "Normal")
        self.assertEqual(pet_exist.ExistCount, 999)

    def test_pet_rap(self):
        pet_rap_data = {
            "Category": "Pet",
            "ConfigData": {
                "Id": "Huge Happy Rock", 
                "Pt": 1,
                "Sh": True
            },
            "Value": 1234
        }
        pet_rap = PetRap(pet_rap_data)
        self.assertEqual(pet_rap.Category, "Pet")
        self.assertEqual(pet_rap.IsShiny, True)
        self.assertEqual(pet_rap.Variation, "Golden")
        self.assertEqual(pet_rap.Rap, 1234)

class TestSearchFunctions(unittest.TestCase):
    def test_collection_get_info_by_name(self):
        collection = Collection("Pets")
        pet_info = collection.get_info_by_name("Huge Happy Rock")
        self.assertIsNotNone(pet_info)

    def test_exists_search_for_pet(self):
        exists = Exists()
        pet_info = exists.search_for_pet("Huge Happy Rock")
        self.assertIsNotNone(pet_info)
        self.assertEqual(pet_info.Id, "Huge Happy Rock")

    def test_rap_search_for_pet(self):
        rap = Rap()
        pet_info = rap.search_for_pet("Huge Happy Rock")
        self.assertIsNotNone(pet_info)
        self.assertEqual(pet_info.Id, "Huge Happy Rock")
          
if __name__ == "__main__":
    unittest.main()
    
