from Item import Item
from Gear import Gear
from ColorScheme import warn_str

class Slot(Item):
    def __init__(self, slot_type):
        assert(slot_type in Item.SLOT_TYPES)
        super().__init__(slot_type)
        self.slot_type = slot_type
        self.gear = None
    def __str__(self, prefix=''):
        s = "{prefix}{slot_type}".format(prefix=prefix, slot_type=self.slot_type)
        if self.gear:
            s += ' equiped:\n' + self.gear.__str__(prefix + '  ')
        else:
            s += ' ' + warn_str('(Empty)')
        return s
    def equip(self, gear):
        assert(isinstance(gear, Gear))
        assert(gear.gear_type in Slot.SLOT_GEAR[self.slot_type])
        self.gear = gear
        self.gear.slot = self
    def _gear(self):
        return self.gear
