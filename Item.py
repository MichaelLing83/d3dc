from Unit import Unit
from ColorScheme import _normal, _unusual, _rare, _legendary, _set
from Socket import Socket

class Item(Unit):
    ITEM_TYPES = (
    # Weapon
    'Axe', 'Dagger', 'Mace', 'Spear', 'Sword', 'Ceremonial Knife', 'Fist Weapon', 'Flail', 'Mighty Weapon',
    # Head
    'Helm', 'Spirit Stone', 'Voodoo Mask', 'Wizard Hat',
    # Shoulders
    'Shoulders',
    # Torso
    'Chest Armor', 'Cloak',
    # Wrists
    'Bracers',
    # Hands
    'Gloves',
    # Waist
    'Belt', 'Mighty Belt',
    # Legs
    'Pants',
    # Feet
    'Boots',
    # Jewelry
    'Amulet', 'Ring',
    # Off-hand
    'Shield', 'Crusader Shield', 'Mojo', 'Orb', 'Quiver',
    # Follower Special
    'Enchantress Focus', 'Templar Relic', 'Scoundrel Token')
    SLOT_TYPES = ('Head', 'Shoulders', 'Torso', 'Wrists', 'Hands', 'MainHand', 'OffHand', 'Waist', 'Legs',
                'Feet', 'Amulet', 'Ring', 'Follower Special')
    SLOT_GEAR = {
        'Head': ('Helm', 'Spirit Stone', 'Voodoo Mask', 'Wizard Hat'),
        'Shoulders': ('Shoulders',),
        'Torso': ('Chest Armor', 'Cloak'),
        'Wrists': ('Bracers',),
        'Hands': ('Gloves',),
        'Waist': ('Belt', 'Mighty Belt',),
        'Legs': ('Pants',),
        'Feet': ('Boots',),
        'Amulet': ('Amulet',),
        'Ring': ('Ring',),
        'MainHand': ('Axe', 'Dagger', 'Mace', 'Spear', 'Sword', 'Ceremonial Knife', 'Fist Weapon',
                        'Flail', 'Mighty Weapon',),
        'OffHand': ('Shield', 'Crusader Shield', 'Mojo', 'Orb', 'Quiver',),
        'Follower Special': ('Enchantress Focus', 'Templar Relic', 'Scoundrel Token')
    }
    @staticmethod
    def to_slot_type(gear):
        if isinstance(gear, str):
            for slot_type in Item.SLOT_GEAR.keys():
                if gear in Item.SLOT_GEAR[slot_type]:
                    return slot_type
        assert(False)
    def __init__(self, name, quality = 'Normal'):
        super().__init__(name)
        self._QUALITY = ('Normal', 'Unusual', 'Rare', 'Legendary', 'Set')
        self._color = { 'Normal': _normal,
                        'Unusual': _unusual,
                        'Rare': _rare,
                        'Legendary': _legendary,
                        'Set': _set }
        assert(quality in self._QUALITY)
        self.quality = quality
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
    def __str__(self, prefix=''):
        s = prefix + self._color[self.quality]("{}".format(self.name)) + '\n'
        s += prefix + self._color[self.quality](self.quality)
        return s
    def addSocket(self):
        self.sockets.append(Socket(self))
    def update_formula(self, formular):
        pass
    def _resistanceToAllElements(self, owner=None):
        return self.resistanceToAllElements
    def _attackSpeedIncreasedBy(self, owner=None):
        return self.attackSpeedIncreasedBy
    def _criticalHitChanceIncreasedBy(self, owner=None):
        return self.criticalHitChanceIncreasedBy
    def _criticalHitDamageIncreasedBy(self, owner=None):
        criticalHitDamageIncreasedBy = self.criticalHitDamageIncreasedBy
        for socket in self.sockets:
            gem = socket._get_gem()
            if gem:
                criticalHitDamageIncreasedBy += gem._criticalHitDamageIncreasedBy(self)
        return criticalHitDamageIncreasedBy
    def _increaseDamageAgainstElites(self, owner=None):
        return self.increaseDamageAgainstElites
    def _intelligence(self, owner=None):
        intelligence = self.intelligence
        for socket in self.sockets:
            gem = socket._get_gem()
            if gem:
                intelligence += gem._intelligence(self)
        return intelligence
