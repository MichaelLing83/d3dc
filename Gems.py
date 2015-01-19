from Unit import Unit
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
        return super().__str__() + """
Level:  {lvl}""".format(lvl=self.lvl)

class GemOfEfficaciousToxin(LegendaryGem):
    def __init__(self, lvl):
        super().__init__("Gem of Efficacious Toxin", lvl)
    def __str__(self):
        return super().__str__() + """
Properties:
    * Poison all enemies hit for """ + colored("2000%", "blue") + """ damage as Poison over 10 seconds.
        * Upgrade: +50% damage as Poison over 10 seconds (+5% per second) per Rank.
    * Poisoned enemies also take 10% increased damage from all sources (Requires Rank 25)"""

if __name__ == '__main__':
    from colorama import Fore, Back, Style
    import colorama
    colorama.init()
    toxin = GemOfEfficaciousToxin(25)
    print(toxin)