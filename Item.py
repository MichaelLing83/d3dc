from Unit import Unit
from ColorScheme import _normal, _unusual, _rare, _legendary, _set

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
    def __str__(self, prefix=''):
        s = prefix + self._color[self.quality]("{}".format(self.name)) + '\n'
        s += prefix + self._color[self.quality](self.quality)
        return s
    def update_formula(self, formular):
        pass