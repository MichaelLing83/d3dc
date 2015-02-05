from Formulas import AttackSpeedFormula

class Paragon:
    def __init__(self, hero):
        self.hero = hero
        # core tab
        self.mainStatPoint = 0
        self.vitalityPoint = 0
        self.movementSpeedPoint = 0
        self.maximumResourcePoint = 0
        # offense tab
        self.attackSpeedPoint = 0
        self.cooldownReductionPoint = 0
        self.criticalHitChancePoint = 0
        self.criticalHitDamagePoint = 0
        # defense tab
        self.lifePoint = 0
        self.armorPoint = 0
        self.allResistancePoint = 0
        self.lifeRegenerationPoint = 0
        # utility tab
        self.areaDamagePoint = 0
        self.resourceCostReductionPoint = 0
        self.lifeOnHitPoint = 0
        self.goldFindPoint = 0
    def _intelligence(self):
        intelligence = 0
        if self.hero.hero_class in ("WITCH DOCTOR", "WIZARD"):
            intelligence = self.mainStatPoint * 5
        return intelligence
    def _strength(self):
        strength = 0
        if self.hero.hero_class in ("CRUSADER", "BARBARIAN"):
            strength = self.mainStatPoint * 5
        return strength
    def _vitality(self):
        return self.vitalityPoint * 5
    def _movementSpeed(self):
        return 0.5 / 100 * self.movementSpeedPoint
    def _attackSpeed(self):
        return 0.2 / 100 * self.attackSpeedPoint
    def _cooldownReduction(self):
        return 2 / 100 * self.cooldownReductionPoint
    def _criticalHitChance(self):
        return 0.1 / 100 * self.criticalHitChancePoint
    def _criticalHitDamage(self):
        return 1 / 100 * self.criticalHitDamagePoint
    def _lifeIncreasedBy(self):
        return 0.5 / 100 * self.lifePoint
    def _armorIncreasedBy(self):
        return 0.5 / 100 * self.armorPoint
    def _allResistance(self):
        return 5 * self.allResistancePoint
    def _lifeRegeneration(self):
        return 165.1 * self.lifeRegenerationPoint
    def _areaDamageIncreasedBy(self):
        return 1 / 100 * self.areaDamagePoint
    def _lifeOnHit(self):
        return 82.5 * self.lifeOnHitPoint
    def update_formula(self, formula):
        if isinstance(formula, AttackSpeedFormula):
            formula._otherIAS += self._attackSpeed()