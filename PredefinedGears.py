from Gear import Gear
from ColorScheme import _legendary, _set, improvable_str
from Formulas import AttributeFormula

StrongarmBracers = Gear('Bracers', 'Strongarm Bracers', 'Legendary')
StrongarmBracers.armor = 409
StrongarmBracers.physicalSkillsDealMoreDamage = 19 / 100
StrongarmBracers.vitality = 428
StrongarmBracers.criticalHitChanceIncreasedBy = 6 / 100
StrongarmBracers.lifePerHit = 8962

class StrongarmBracers(Gear):
    def __init__(self, moreDamagePercentage):
        super().__init__('Bracers', 'Strongarm Bracers', 'Legendary')
        self.moreDamagePercentage = moreDamagePercentage
    def __str__(self, prefix=''):
        s = super().__str__(prefix)
        s += _legendary("\n{prefix}Enemies hit by knockbacks suffer ".format(prefix=prefix))
        s += improvable_str("{:02.0f}%".format(self.moreDamagePercentage * 100))
        s += _legendary(" more damage for 5 seconds when they land.")
        return s

class TaskerAndTheo(Gear):
    def __init__(self, speedIncrease):
        super().__init__('Gloves', 'Tasker and Theo', 'Legendary')
        self.speedIncrease = speedIncrease
    def __str__(self, prefix=''):
        s = super().__str__(prefix)
        s += _legendary("\n{prefix}Increase attack speed of your pets by ".format(prefix=prefix))
        s += improvable_str("{:02.0f}%".format(self.speedIncrease * 100))
        s += _legendary(".")
        return s


class Unity(Gear):
    def __init__(self):
        super().__init__('Ring', 'Unity', 'Legendary')
    def __str__(self, prefix=''):
        s = super().__str__(prefix)
        s += _legendary("\n{prefix}All damage taken is split between wearers of this item.".format(prefix=prefix))
        return s

class RingOfRoyalGrandeur(Gear):
    def __init__(self):
        super().__init__('Ring', 'Ring of Royal Grandeur', 'Legendary')
    def __str__(self, prefix=''):
        s = super().__str__(prefix)
        s += _legendary("\n{prefix}Reduces the number of items needed for set bonuses by 1 (to a minimum of 2).".format(prefix=prefix))
        return s

class MaskOfJeram(Gear):
    def __init__(self, moreDamagePercent):
        super().__init__("Helm", "Mask of Jeram", "Legendary")
        self._more_damage = moreDamagePercent
    def __str__(self, prefix=''):
        s = super().__str__(prefix)
        s += _legendary("\n{}Pets deal {:03.1f}% more damage.".format(prefix, self._more_damage * 100))
        return s

class SetBonus:
    '''
    Should never be equipped, only used to calculate set bonus.
    '''
    def __init__(self, hero):
        self._hero = hero
    def _set_count(self, key_name):
        set_count = 0
        for slot in self._hero.slots:
            gear = slot._gear()
            if gear and key_name in gear.name:
                set_count += 1
        # check if we have the ring
        for slot in self._hero.slots:
            gear = slot._gear()
            if gear and isinstance(gear, RingOfRoyalGrandeur) and set_count >= 2:
                set_count += 1
        return set_count
    def _intelligence(self):
        intelligence = 0
        # Zunimassa Set
        set_count = self._set_count("Zunimassa")
        if set_count >= 2:
            intelligence = 250
        return intelligence
    def _resistanceToAllElements(self):
        resistanceToAllElements = 0
        # Zunimassa Set
        set_count = self._set_count("Zunimassa")
        if set_count >= 3:
            resistanceToAllElements = 75
        return resistanceToAllElements
    def _increaseDamageAgainstElitesBy(self):
        increaseDamageAgainstElitesBy = 0
        set_count = self._set_count("Aughild")
        if set_count >= 3:
            increaseDamageAgainstElitesBy += 15 / 100
        set_count = self._set_count("Blackthorne")
        if set_count >= 3:
            increaseDamageAgainstElitesBy += 10 / 100
        return increaseDamageAgainstElitesBy
    def _criticalHitChanceIncreasedBy(self):
        criticalHitChanceIncreasedBy = 0
        return criticalHitChanceIncreasedBy
    def update_formula(self, formula):
        if isinstance(formula, AttributeFormula):
            # Zunimassa Set
            set_count = self._set_count("Zunimassa")
            if set_count >= 2:
                formula.intelligence += 250
