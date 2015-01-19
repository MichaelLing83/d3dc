from Unit import Unit
from ColorScheme import *
from termcolor import colored

class Gem(Unit):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return super().__str__()

class LegendaryGem(Gem):
    def __init__(self, name, lvl):
        super().__init__(name)
        self.lvl = lvl
    def apply(self):
        pass
    def __str__(self):
        return super().__str__() + colored("""
Level:  {lvl}""".format(lvl=self.lvl), active_legendary_c)

class GemOfEfficaciousToxin(LegendaryGem):
    def __init__(self, lvl):
        super().__init__("Gem of Efficacious Toxin", lvl)
        self.poison = 2000 + 50 * self.lvl
    def __str__(self):
        result = super().__str__()
        result += active_legendary_str("""
Properties:
    * Poison all enemies hit for """)
        result += improvable_str("{}%".format(self.poison))
        result += active_legendary_str(""" damage as Poison over 10 seconds.
        * Upgrade: +50% damage as Poison over 10 seconds (+5% per second) per Rank.""")
        if self.lvl >= 25:
            tmp_str = active_legendary_str
            tmp_lvl_str = active_legendary_str
        else:
            tmp_str = deactive_str
            tmp_lvl_str = warn_str
        result += tmp_str("""
    * Poisoned enemies also take 10% increased damage from all sources (""")
        result += tmp_lvl_str("Requires Rank 25") + tmp_str(")")
        return result

if __name__ == '__main__':
    from colorama import Fore, Back, Style
    import colorama
    colorama.init()
    toxin = GemOfEfficaciousToxin(25)
    print(toxin)