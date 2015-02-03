from Item import Item
from ColorScheme import *
from termcolor import colored

class Gem(Item):
    def __init__(self, name, quality = 'Normal'):
        super().__init__(name, quality)
    def __str__(self, prefix):
        return super().__str__(prefix)
    def _intelligence(self):
        return 0

class FlawlessRoyalTopaz(Gem):
    def __init__(self):
        super().__init__("Flawless Royal Topaz", 'Normal')
        self.helm = "41% Better Chance of Finding Magical Items"
        self.weapon = "Ranged and melee attackers take 4975 damage per hit"
        self.other = "+280 Intelligence"
    def __str__(self, owner, prefix = ''):
        s = prefix + self.name
        if owner == None:
            s += '\n' + '  ' + prefix + "Can be inserted into equipment with sockets."
            s += '\n' + '  ' + prefix + "Helm: " + self.helm
            s += '\n' + '  ' + prefix + "Weapon: " + self.weapon
            s += '\n' + '  ' + prefix + "other: " + self.other
        else:
            slot_type = Item.to_slot_type(owner.gear_type)
            if slot_type == 'Head':
                s += ':  ' + self.helm
            elif slot_type == 'Main Hand':
                s += ':  ' + self.weapon
            else:
                s += ':  ' + self.other
        return s


class LegendaryGem(Gem):
    def __init__(self, name, lvl, quality = 'Legendary'):
        super().__init__(name, quality)
        self.lvl = lvl
    def apply(self):
        pass
    def __str__(self, owner, prefix):
        s = super().__str__(prefix) + '\n'
        s += prefix + colored("Level:  {lvl}".format(lvl=self.lvl), active_legendary_c)
        return s

class Enforcer(LegendaryGem):
    def __init__(self, lvl):
        super().__init__("Enforcer", lvl)
        self.petDamageIncrease = 15 + 0.3 * self.lvl
    def __str__(self, owner = None, prefix = ''):
        result = super().__str__(owner, prefix) + '\n'
        result += prefix + active_legendary_str("Properties:\n")
        result += prefix + active_legendary_str("  * Increases the damage of your pets by ")
        result += improvable_str("{:03.1f}%".format(self.petDamageIncrease))
        result += active_legendary_str(".\n")
        result += prefix + active_legendary_str("    * Upgrade: +0.3% damage per Rank.\n")
        if self.lvl >= 25:
            tmp_str = active_legendary_str
            tmp_lvl_str = active_legendary_str
        else:
            tmp_str = deactive_str
            tmp_lvl_str = warn_str
        result += prefix + tmp_str("  * Your pets take 25% less damage (")
        result += tmp_lvl_str("Requires Rank 25") + tmp_str(")")
        return result

class PainEnhancer(LegendaryGem):
    def __init__(self, lvl):
        super().__init__("Pain Enhancer", lvl)
        self.bleed = 1200 + 30 * self.lvl
    def __str__(self, owner = None, prefix = ''):
        result = super().__str__(owner, prefix) + '\n'
        result += prefix + active_legendary_str("Properties:\n")
        result += prefix + active_legendary_str("  * Critical hits cause the enemy to bleed for ")
        result += improvable_str("{}%".format(self.bleed))
        result += active_legendary_str(" damage as Physical over 3 seconds.\n")
        result += prefix + active_legendary_str("    * Upgrade: +30% damage as Physical over 3 seconds (+10% per second) per Rank.\n")
        if self.lvl >= 25:
            tmp_str = active_legendary_str
            tmp_lvl_str = active_legendary_str
        else:
            tmp_str = deactive_str
            tmp_lvl_str = warn_str
        result += prefix + tmp_str("  * Gain Blood Frenzy, granting 3% increased Attack Speed for each bleeding enemy within 20 yards (")
        result += tmp_lvl_str("Requires Rank 25") + tmp_str(")")
        return result

class GemOfEfficaciousToxin(LegendaryGem):
    def __init__(self, lvl):
        super().__init__("Gem of Efficacious Toxin", lvl)
        self.poison = 2000 + 50 * self.lvl
    def __str__(self, owner = None, prefix = ''):
        result = super().__str__(owner, prefix) + '\n'
        result += prefix + active_legendary_str("Properties:\n")
        result += prefix + active_legendary_str("  * Poison all enemies hit for ")
        result += improvable_str("{}%".format(self.poison))
        result += active_legendary_str(" damage as Poison over 10 seconds.\n")
        result += prefix + active_legendary_str("    * Upgrade: +50% damage as Poison over 10 seconds (+5% per second) per Rank.\n")
        if self.lvl >= 25:
            tmp_str = active_legendary_str
            tmp_lvl_str = active_legendary_str
        else:
            tmp_str = deactive_str
            tmp_lvl_str = warn_str
        result += prefix + tmp_str("  * Poisoned enemies also take 10% increased damage from all sources (")
        result += tmp_lvl_str("Requires Rank 25") + tmp_str(")")
        return result

if __name__ == '__main__':
    from colorama import Fore, Back, Style
    import colorama
    colorama.init()
    toxin = GemOfEfficaciousToxin(25)
    print(toxin)