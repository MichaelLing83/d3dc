from Gear import Gear
from ColorScheme import _legendary, _set, improvable_str

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