from Item import Item
from Gems import Gem
from Socket import Socket
from ColorScheme import property_str, number_str
from Formulas import AttackSpeedFormula, DamageFormula, ResistanceFormula

class Gear(Item):
    def __init__(self, gear_type, name, quality = 'Normal'):
        assert(gear_type in Item.ITEM_TYPES)
        super().__init__(name, quality)
        self.gear_type = gear_type
        self.sockets = list()
        self.armor = 0
        self.intelligence = 0
        self.vitality = 0
        self.attackSpeedIncreasedBy = 0
        self.criticalHitChanceIncreasedBy = 0
        self.criticalHitDamageIncreasedBy = 0
        self.increaseGargantuanDamageBy = 0
        self.increaseHauntDamageBy = 0
        self.increaseDamageAgainstElites = 0
        self.physicalSkillsDealMoreDamage = 0
        self.poisonSkillsDealMoreDamage = 0
        self.resistanceToAllElements = 0
        self.fireResistance = 0
        self.coldResistance = 0
        self.lightningResistance = 0
        self.poisonResistance = 0
        self.physicalResistance = 0
        self.lifePerHit = 0
        self.life = 0   # increase life by x percentage
        self.movementSpeed = 0
        self.damage = (0, 0)
        self.attacksPerSecond = 0
    def _intelligence(self):
        intelligence = self.intelligence
        for socket in self.sockets:
            gem = socket._get_gem()
            if gem:
                intelligence += gem._intelligence(self)
        return intelligence
    def _resistanceToAllElements(self):
        return self.resistanceToAllElements
    def _attackSpeedIncreasedBy(self):
        return self.attackSpeedIncreasedBy
    def _criticalHitChanceIncreasedBy(self):
        return self.criticalHitChanceIncreasedBy
    def _criticalHitDamageIncreasedBy(self):
        return self.criticalHitDamageIncreasedBy
    def _increaseDamageAgainstElites(self):
        return self.increaseDamageAgainstElites
    def __str__(self, prefix='', is_weapon=False):
        s = super().__str__(prefix)
        s += " " + self._color[self.quality](self.gear_type)
        if self.damage != (0, 0):
            if is_weapon:
                s += ''.join(("\n",
                            prefix,
                            "{}-{} Damage".format(self.damage[0], self.damage[1])))
            else:
                s += ''.join(("\n",
                            prefix,
                            number_str("+{}".format(self.damage[0])),
                            property_str("-"),
                            number_str("{}".format(self.damage[1])),
                            property_str(" Damage")))
        if is_weapon and self.attacksPerSecond:
            s += ''.join(("\n",
                        prefix,
                        "{:03.2f} Attacks per Second".format(self.attacksPerSecond)))
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
        if self.life:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{:02.0f}% ".format(self.life * 100)),
                        property_str("Life")))
        if self.physicalSkillsDealMoreDamage:
            s += ''.join(("\n",
                        prefix, property_str("Physical skills deal "),
                        number_str("{:03.1f}%".format(self.physicalSkillsDealMoreDamage * 100)),
                        property_str(" more damage.")))
        if self.poisonSkillsDealMoreDamage:
            s += ''.join(("\n",
                        prefix, property_str("Physical skills deal "),
                        number_str("{:03.1f}%".format(self.poisonSkillsDealMoreDamage * 100)),
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
                        property_str("Resistance to all elements")))
        if self.fireResistance:
            s += ''.join(("\n",
                        prefix,
                        number_str("+{} ".format(self.fireResistance)),
                        property_str("Fire Resistance")))
        if self.attackSpeedIncreasedBy:
            s += ''.join(("\n",
                        prefix, property_str("Attack Speed Increased by "),
                        number_str("{:03.1f}%".format(self.attackSpeedIncreasedBy * 100))))
        if self.criticalHitChanceIncreasedBy:
            s += ''.join(("\n",
                        prefix, property_str("Critical Hit Chance Increased by "),
                        number_str("{:03.1f}%".format(self.criticalHitChanceIncreasedBy * 100))))
        if self.criticalHitDamageIncreasedBy:
            s += ''.join(("\n",
                        prefix, property_str("Critical Hit Damage Increased by "),
                        number_str("{:03.1f}%".format(self.criticalHitDamageIncreasedBy * 100))))
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
    def update_formula(self, formula):
        if isinstance(formula, AttackSpeedFormula):
            formula._otherIAS += self.attackSpeedIncreasedBy
        elif isinstance(formula, DamageFormula):
            if formula._element_type == "Physical":
                formula._category_A += self.physicalSkillsDealMoreDamage
            elif formula._element_type == "Poison":
                formula._category_A += self.poisonSkillsDealMoreDamage
        elif isinstance(formula, ResistanceFormula):
            formula._all_resistance += self.resistanceToAllElements
            formula._fire_resistance += self.fireResistance
            formula._cold_resistance += self.coldResistance
            formula._lightning_resistance += self.lightningResistance
            formula._poison_resistance += self.poisonResistance
            formula._physical_resistance += self.physicalResistance

class Weapon(Gear):
    def __init__(self, gear_type, name, quality = 'Normal'):
        super().__init__(gear_type, name, quality)
        self.attacksPerSecond = 0
    def __str__(self, prefix=''):
        return super().__str__(prefix, is_weapon=True)
    def update_formula(self, formula):
        if isinstance(formula, AttackSpeedFormula):
            formula._weaponAttackSpeed = self.attacksPerSecond
            formula._weaponIAS = self.attackSpeedIncreasedBy
