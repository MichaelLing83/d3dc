from Item import Item
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
from Skills import ASkill, Skills
from Formulas import AttackSpeedFormula, DamageFormula
from PredefinedGears import SetBonus

class Hero(Item):
    CLASSES = ('Witch Doctor', 'Crusader', 'Babarian', 'Demon Hunter', 'Wizard')
    def __init__(self, hero_class, name):
        assert(hero_class in Hero.CLASSES)
        super().__init__(name)
        self.hero_class = hero_class
        self.lvl = 70
        self.name = name
        self.paragon = Paragon(self)
        self.intelligence = 7 + 3 * self.lvl
        self.vitality = 7 + 2 * self.lvl
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
        self.slots = (self.head, self.shoulders, self.amulet, self.torso, self.hands, self.wrists,
                        self.waist, self.ring_one, self.ring_two, self.legs, self.feet, self.mainHand,
                        self.offHand)
        self.skills = Skills()
    def _intelligence(self):
        intelligence = self.intelligence
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                intelligence += gear._intelligence()
        # check Paragon points
        intelligence += self.paragon._intelligence()
        # check set bonuses
        intelligence += SetBonus(self)._intelligence()
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
        # check Paragon points
        criticalHitChanceIncreasedBy += self.paragon._criticalHitChance()
        # check Set bonus
        criticalHitChanceIncreasedBy += SetBonus._attackSpeedIncreasedBy()
        return criticalHitChanceIncreasedBy
    def _criticalHitDamageIncreasedBy(self):
        criticalHitDamageIncreasedBy = 0
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                criticalHitDamageIncreasedBy += gear._criticalHitDamageIncreasedBy()
        criticalHitDamageIncreasedBy += self.paragon._criticalHitDamage()
        return criticalHitDamageIncreasedBy
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
    def attackPerSecond(self):
        return self.attack_speed()
    def attackSpeedIncrease(self):
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
        return formula._otherIAS + formula._weaponIAS
    def _baseDamage(self):
        '''
        Weapon damage plus any +damage from gears
        '''
        damage = [0, 0]
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                damage[0] += gear.damage[0]
                damage[1] += gear.damage[1]
        return damage
    def _skillDamage(self, skill_name):
        '''
        Get damage info for one equipped skill.
        '''
        skill = None
        for sk in self.skills:
            if sk.name == skill_name:
                skill = sk
        assert(skill != None, "Skill {} is not equipped for this hero.".format(skill_name))
        damageFormula = DamageFormula(self, skill)
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                gear.update_formula(damageFormula)
        return damageFormula.calc()
    def damageIncreasedBySkills(self):
        damageFormula = DamageFormula(self, ASkill("None"))
        for skill in self.skills:
            skill.update_formula(damageFormula)
        return damageFormula._category_D - 1
    def bonusDamageToElites(self):
        bonusDamageToElites = 0
        for slot in self.slots:
            gear = slot._gear()
            if gear:
                bonusDamageToElites += gear._increaseDamageAgainstElites()
        # check set bonuses
        bonusDamageToElites += SetBonus(self)._increaseDamageAgainstElitesBy()
        return bonusDamageToElites

