from Unit import  Unit
from Formulas import AttackSpeedFormula, DamageFormula

class ASkill(Unit):
    def __init__(self, name):
        super().__init__(name)
        self._element_type = None
    def _attackSpeedIncreasedBy(self):
        return 0
    def element_type(self):
        return self._element_type
    def update_formula(self, formula):
        pass
    def damage(self, hero):
        return (0,  # non-critical min
                0,  # non-critical max
                0,  # critical min
                0,  # critical max
                "Physical"  # element type
                )


class BigBadVoodoo(ASkill):
    def __init__(self, rune):
        super().__init__("Big Bad Voodoo")
        self._runes = ('None', 'Jungle Drums', 'Rain Dance', 'Slam Dance', 'Ghost Trance', 'Boogie Man')
        assert(rune in self._runes)
        self.rune = rune
        self._element_type = "Physical"
    def _attackSpeedIncreasedBy(self):
        '''
Big Bad Voodoo increased attack speed by 20% for all runes.
        '''
        return 20 / 100
    def update_formula(self, formula):
        if isinstance(formula, AttackSpeedFormula):
            formula._otherIAS += self._attackSpeedIncreasedBy()

class FetishArmy(ASkill):
    def __init__(self, rune):
        super().__init__("Fetish Army")
        self._runes = ("None", "Fetish Ambush", "Devoted Following", "Legion of Daggers", "Tiki Torchers", "Head Hunters")
        assert(rune in self._runes)
        self.rune = rune
        if self.rune == "Fetish Ambush":
            self._element_type = "Cold"
        elif self.rune == "Tiki Torchers":
            self._element_type = "Fire"
        elif self.rune == "Head Hunters":
            self._element_type = "Poison"
    def update_formula(self, formula):
        if isinstance(formula, DamageFormula):
            if formula.skill is self:
                formula._skill_tooltip += 180 / 100 * 5
                if self.rune == "Legion of Daggers":
                    formula._skill_tooltip += 180 / 100 * 3
                elif self.rune == "Tiki Torchers":
                    formula._skill_tooltip += 85 / 100 * 2
                elif self.rune == "Head Hunters":
                    formula._skill_tooltip += 130 / 100 * 2

class CorpseSpiders(ASkill):
    def __init__(self, rune):
        super().__init__("Corpe Spiders")
        self._runes = ('None', 'Leaping Spiders', 'Spider Queen', 'Widowmakers', 'Medusa Spiders', 'Blazing Spiders')
        assert(rune in self._runes)
        self.rune = rune
        self._element_type = 'Physical'
        if self.rune in ('Leaping Spiders', 'Spider Queen'):
            self._element_type = 'Poison'
        elif self.rune == 'Medusa Spiders':
            self._element_type = 'Cold'
        elif self.rune == 'Blazing Spiders':
            self._element_type = 'Fire'
    def update_formula(self, formula):
        if isinstance(formula, DamageFormula):
            if formula.skill is self:
                formula._skill_tooltip += 576 / 100
                if self.rune == 'Leaping Spiders':
                    formula._skill_tooltip += (645 - 576) / 100
                elif self.rune == 'Spider Queen':
                    assert(False, "Spider Queen rune is not implemented.")
                elif self.rune == 'Blazing Spiders':
                    formula._skill_tooltip += (700 - 576) / 100

class Piranhas(ASkill):
    def __init__(self, rune):
        super().__init__("Piranhas")
        self._runes = ('None', "Bogdadile", "Zombie Piranhas", "Piranhado", "Wave of Mutilation", "Frozen Piranhas")
        assert(rune in self._runes)
        self.rune = rune
        self._element_type = 'Poison'
        if self.rune == "Bogdadile":
            self._element_type = 'Physical'
        elif self.rune == 'Frozen Piranhas':
            self._element_type = 'Cold'
    def update_formula(self, formula):
        if isinstance(formula, DamageFormula):
            formula._category_D += 15 / 100
            if formula.skill is self:
                if self.rune in ('None', 'Zombie Paranhas', 'Piranhado', 'Frozen Piranhas'):
                    formula._skill_tooltip += 400 / 100
                elif self.rune == "Bogdagile":
                    formula._skill_tooltip += 1100 / 100
                elif self.rune == "Wave of Mutilation":
                    formula._skill_tooltip += 475 / 100

class PierceTheVeil(ASkill):
    def __init__(self):
        super().__init__("Pierce the Veil")
    def update_formula(self, formula):
        if isinstance(formula, DamageFormula):
            formula._category_D += 20 / 100

class Skills(list):
    def __init__(self):
        super().__init__()
    def add(self, skill):
        assert(isinstance(skill, ASkill))
        self.append(skill)
