
class Formula:
    def __init__(self):
        pass
    def calc(self):
        pass

class AttributeFormula(Formula):
    '''
    Calculate resistance to one element.
    '''
    def __init__(self):
        ## From game details panel
        # offensive attributes
        self.damageIncreasedByInt = 0
        self.damageIncreasedBySkills = 0
        self.bonusDamageToElites = 0
        self.attacksPerSecond = 0
        self.attackSpeedIncrease = 0
        self.criticalHitChance = 0
        self.criticalHitDamage = 0
        self.areaDamage = 0
        self.cooldownReduction = 0
        self.physicalDamageIncrease = 0
        self.coldDamageIncrease = 0
        self.fireDamageIncrease = 0
        self.lightningDamageIncrease = 0
        self.poisonDamageIncrease = 0
        self.arcaneDamageIncrease = 0
        self.holyDamageIncrease = 0
        self.hauntDamageIncrease = 0
        self.fetishArmyDamageIncrease = 0
        # defensive attributes
        self.armor = 0
        self.blockAmount = [0, 0]
        self.blockChance = 0
        self.dodgeChance = 0
        self.physicalResistance = 0
        self.coldResistance = 0
        self.fireResistance = 0
        self.lightningResistance = 0
        self.poisonResistance = 0
        self.arcaneHolyResistance = 0
        self.crowdControlReduction = 0
        self.missileDamageReduction = 0
        self.meleeDamageReduction = 0
        self.eliteDamageReduction = 0
        self.thorns = 0
        # life
        self.maximumLife = 0
        self.totalLifeBonus = 0
        self.lifePerSecond = 0
        self.lifePerHit = 0
        self.lifePerKill = 0
        self.lifeSteal = 0
        self.healthGlobeHealingBonus = 0
        self.bonusToGoldGlobeRadius = 0
        # resource
        self.maximumMana = 0
        self.manaGenerationPerSecond = 0
        self.manaCostReduction = 0
        # adventure
        self.movementSpeed = 0
        self.goldFind = 0
        self.magicFind = 0
        self.bonusExperience = 0
        self.bonusExperiencePerKill = 0
        ## End of game details panel

        ## Basic attributes
        self.intelligence = 0
        self.strength = 0
        self.vitality = 0
        ## End of basic attributes
    def calc(self):
        self.damageIncreasedByInt = self.intelligence / 100
    def __str__(self):
        def align(s1, s2):
            return "{:<30s}{:>10s}\n".format(s1, s2)
        s = ""
        s += "{:>20s}\n".format("DETAILS")
        s += "OFFENSE\n"
        s += align("Damage Increased by Int", "{:,}%".format(int(self.damageIncreasedByInt*100)))
        s += align("Damage Increased by Skills", "{:04.2f}%".format(self.damageIncreasedBySkills))
        s += align("Bonus Damage to Elites", "{:04.2f}%".format(self.bonusDamageToElites))
        s += align("Attacks per Second", "{:03.2f}".format(self.attacksPerSecond))
        s += align("Attack Speed Increase", "{:04.2f}%".format(self.attackSpeedIncrease))
        s += align("Critical Hit Chance", "{:04.2f}%".format(self.criticalHitChance))
        s += align("Critical Hit Damage", "+{:05.2f}%".format(self.criticalHitDamage))
        s += align("Area Damage", "{:04.2f}%".format(self.areaDamage))
        s += align("Cooldown Reduction", "{:04.2f}%".format(self.cooldownReduction))
        s += align("Poison Damage Increase", "{:04.2f}%".format(self.poisonDamageIncrease))
        s += align("Haunt Damage Increase", "{:04.2f}%".format(self.hauntDamageIncrease))
        s += align("Fetish Army Damage Increase", "{:04.2f}%".format(self.fetishArmyDamageIncrease))
        return s

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
