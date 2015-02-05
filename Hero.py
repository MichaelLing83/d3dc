from Unit import Unit
from Head import Head
from Shoulders import Shoulders
from Amulet import Amulet
from Torso import Torso
from Waist import Waist
from Wrists import Wrists
from Ring import Ring
from MainHand import MainHand
from OffHand import OffHand
from Legs import Legs
from Feet import Feet
from Hands import Hands
from Paragon import Paragon
from Skills import BigBadVoodoo, Skills
from Formulas import AttackSpeedFormula

class Hero(Unit):
    CLASSES = ('Witch Doctor', 'Crusader', 'Babarian', 'Demon Hunter', 'Wizard')
    def __init__(self, hero_class, name):
        assert(hero_class in Hero.CLASSES)
        super().__init__(name)
        self.hero_class = hero_class
        self.lvl = 70
        self.name = name
        self.paragon = Paragon(self)
        self.intelligence = 10 + 3 * self.lvl
        self.head = Head()
        self.shoulders = Shoulders()
        self.torso = Torso()
        self.amulet = Amulet()
        self.wrists = Wrists()
        self.waist = Waist()
        self.legs = Legs()
        self.hands = Hands()
        self.feet = Feet()
        self.ring_one = Ring()
        self.ring_two = Ring()
        self.mainHand = MainHand()
        self.offHand = OffHand()
        self.slots = (self.head, self.shoulders, self.torso, self.amulet, self.wrists, self.hands,
                        self.waist, self.legs, self.feet, self.ring_one, self.ring_two, self.mainHand,
                        self.offHand)
        self.skills = Skills()
    def _intelligence(self):
        intelligence = self.intelligence
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                intelligence += gear._intelligence()
        intelligence += self.paragon._intelligence()
        return intelligence
    def __str__(self, prefix=''):
        s = super().__str__()
        s += """
Class:  {}
Lvl:    {}
Intel:  {}
""".format(self.hero_class, self.lvl, self._intelligence())
        for slot in self.slots:
            s += str(slot) + "\n"
        return s
    def _criticalHitChanceIncreasedBy(self):
        criticalHitChanceIncreasedBy = 0
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                criticalHitChanceIncreasedBy += gear._criticalHitChanceIncreasedBy()
        return criticalHitChanceIncreasedBy
    def _baseWeaponAps_E7(self):
        aps = 0
        weapon = self.mainHand._gear()
        aps = (1 + weapon.attackSpeedIncreasedBy) * weapon.attacksPerSecond
        return aps
    def _totalAPS_E8(self):
        return (1 + self._increasedAttackSpeedOnGearAndParagon()) * self._baseWeaponAps_E7()
    def _increasedAttackSpeedOnGearAndParagon(self):
        ias = self.paragon._attackSpeed()
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                ias += gear._attackSpeedIncreasedBy()
        return ias
    def attack_speed(self):
        formula = AttackSpeedFormula()
        # update from all gears
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                gear.update_formula(formula)
        # update from paragon points
        self.paragon.update_formula(formula)
        # update from skills
        for skill in self.skills:
            skill.update_formula(formula)
        return formula.calc()