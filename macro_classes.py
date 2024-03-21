import time
import random
import pytesseract
import pyautogui
import keyboard
import time
import random
import autoit
from PIL import Image, ImageGrab
from collections.abc import Callable, Iterable, Sequence
from typing import Final, NamedTuple, SupportsIndex, SupportsInt, TypeVar

class Ocr():
    def getTextFromRect():
        return
    
class Keybind():
    @staticmethod
    def add(keybind, callback, args=(), suppress=False, timeout=1, trigger_on_release=False):
        keyboard.add_hotkey(keybind, callback, args, suppress, timeout, trigger_on_release)
    
    @staticmethod   
    def remove(keybind):
        keyboard.remove_hotkey(keybind)
        
class Input():
    @staticmethod
    def click(cords=(None, None), button="left", clicks=1, speed=-1) -> None:
        autoit.mouse_click(button, cords[0], cords[1], clicks, speed)
    
    @staticmethod
    def press(
        keys: str | Iterable[str],
        presses: SupportsIndex = 1,
        interval: float = 0.0,
        logScreenshot: bool | None = None,
        _pause: bool = True,
    ) -> None:
        pyautogui.press(keys, presses, interval, logScreenshot, _pause)
        
    @staticmethod   
    def scroll(clicks, x=None, y=None, logScreenshot=None, _pause=True):
        pyautogui.scroll(clicks, x, y, logScreenshot, _pause)
        
class HomeUICordinates():
    InventoryCords = (1286, 1292)
    AutoFarmCords = (219, 647)
    AutoHatchCords = (81, 636)
    AutoTapCords = (347, 645)
    HoverboardCords = (341, 506)
    TeleportCords = (215, 515)
    FreeGiftCords = (80, 501)
    RewardsCords = (2374, 996)
    SpecialAbilityCords = (772, 1290)
    EscapeCords = None

class BottomBarInventoryCords():
    PetCords = (857, 1292)
    ExclusiveShopCords = (999, 1289)
    AchievementCords = (1145, 1288)
    TradingCords = (1283, 1288)
    ClanCords = (1430, 1291)
    MasteryCords = (1583, 1302)
    SettingCords = (1716, 1291)

class SideBarInventoryCords():
    pass

class MainInventoryCords():
    SeachBarCords = None
    FirstItemCords = None
    
