from Item import Item
from Gems import Gem
from Socket import Socket
from ColorScheme import property_str, number_str

class Gear(Item):
    def __init__(self, gear_type, name, quality = 'Normal'):
        assert(gear_type in Item.ITEM_TYPES)
        super().__init__(name, quality)
        self.gear_type = gear_type
        self.sockets = list()
        self.armor = 0
        self.intelligence = 0
        self.vitality = 0
        self.criticalHitChanceIncreasedBy = 0
        self.increaseGargantuanDamageBy = 0
        self.increaseHauntDamageBy = 0
        self.physicalSkillsDealMoreDamage = 0
        self.resistanceToAllElements = 0
        self.lifePerHit = 0
        self.movementSpeed = 0
    def __str__(self, prefix=''):
        s = super().__str__(prefix)
        s += " " + self._color[self.quality](self.gear_type)
        if self.armor:
            s += ''.join(("\n", prefix, "Armor: {}".format(self.armor)))
        if self.intelligence:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{} ".format(self.intelligence)),
                        property_str("Intelligence")))
        if self.vitality:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{} ".format(self.vitality)),
                        property_str("Vitality")))
        if self.physicalSkillsDealMoreDamage:
            s += ''.join(("\n",
                        prefix, property_str("Physical skills deal "),
                        number_str("{:03.1f}%".format(self.physicalSkillsDealMoreDamage * 100)),
                        property_str(" more damage.")))
        if self.increaseGargantuanDamageBy:
            s += ''.join(("\n",
                        prefix,
                        property_str("Increase "),
                        number_str("Gargantuan "),
                        property_str("damage by "),
                        number_str("{:03.1f}%".format(self.increaseGargantuanDamageBy * 100)),
                        property_str(" (Witch Doctor Only)")))
        if self.increaseHauntDamageBy:
            s += ''.join(("\n",
                        prefix,
                        property_str("Increase "),
                        number_str("Haunt "),
                        property_str("damage by "),
                        number_str("{:03.1f}%".format(self.increaseHauntDamageBy * 100)),
                        property_str(" (Witch Doctor Only)")))
        if self.resistanceToAllElements:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{} ".format(self.resistanceToAllElements)),
                        property_str("Resistance to all elements.")))
        if self.criticalHitChanceIncreasedBy:
            s += ''.join(("\n",
                        prefix, property_str("critical hit chance increased by "),
                        number_str("{:03.1f}%".format(self.criticalHitChanceIncreasedBy * 100))))
        if self.lifePerHit:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{} ".format(self.lifePerHit)),
                        property_str("Life per Hit")))
        if self.movementSpeed:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{:03.1f}% ".format(self.movementSpeed * 100)),
                        property_str("Movement Speed")))
        if self.sockets:
            for socket in self.sockets:
                s += '\n' + socket.__str__(prefix + '  ')
        return s
    def addSocket(self):
        self.sockets.append(Socket(self))
