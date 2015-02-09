
class Formula:
    def __init__(self):
        pass

class ResistanceFormula(Formula):
    '''
    Calculate resistance to one element.
    '''
    def __init__(self):
        self._all_resistance = 0
        self._fire_resistance = 0
        self._cold_resistance = 0
        self._lightning_resistance = 0
        self._poison_resistance = 0
        self._physical_resistance = 0
class AttackSpeedFormula(Formula):
    '''
    player's attack speed = Weapon_attack_speed * (1 + IAS_on_weapon) * (1 + IAS_from_all_other_sources)
    '''
    def __init__(self):
        self._weaponAttackSpeed = 0
        self._weaponIAS = 0
        self._otherIAS = 0
    def calc(self):
        return self._weaponAttackSpeed * (1 + self._weaponIAS) * (1 + self._otherIAS)

class DamageFormula(Formula):
    '''
    Formula to calculate single hit damage (critical or non-critical) for one skill
    '''
    def __init__(self, hero, skill):
        '''
        [ Weapon Damage ]
        x [ 1 + (Intel/100) ]
        x [ APS ]
        x [ Tooltip ]
        x [ Pet Buff + %Element ]   # category A
        x [ % Skill ]   # category B
        x [ % Elite ]   # category C
        x [ Character Buff + Monster Debuff ]   # category D
        x [ Bane Trapped ]  # category E
        x [ Zei's Stone ]   # category F
        '''
        self.hero = hero
        self.skill = skill
        self._element_type = skill.element_type()
        self._base_damage = hero._baseDamage()
        self._skill_tooltip = 1
        self._category_A = 1
        self._category_B = 1
        self._category_C = 1
        self._category_D = 1
        self._category_E = 1
        self._category_F = 1
        self._category_G = 1
    def calc(self):
        def scale(x):
            return x * (1 + self.hero._intelligence() / 100) * self._skill_tooltip * self._category_A * self._category_B * self._category_C * self._category_D * self._category_E * self._category_F * self._category_G
        damage_min, damage_max = tuple(map(scale, self._base_damage))
        critical_min = damage_min * (1 + self.hero._criticalHitDamageIncreasedBy())
        critical_max = damage_max * (1 + self.hero._criticalHitDamageIncreasedBy())
        return (damage_min, damage_max, critical_min, critical_max, self._element_type)
