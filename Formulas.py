
class Formula:
    def __init__(self):
        pass

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