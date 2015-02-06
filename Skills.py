from Unit import  Unit
from Formulas import AttackSpeedFormula

class ASkill(Unit):
    def __init__(self, name):
        super().__init__(name)
    def _attackSpeedIncreasedBy(self):
        return 0
    def update_formula(self, formula):
        pass


class BigBadVoodoo(ASkill):
    def __init__(self, rune):
        super().__init__("Big Bad Voodoo")
        self._runes = ('None', 'Jungle Drums', 'Rain Dance', 'Slam Dance', 'Ghost Trance', 'Boogie Man')
        assert(rune in self._runes)
        self.rune = rune
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

class Skills(list):
    def __init__(self):
        super().__init__()
    def add(self, skill):
        assert(isinstance(skill, ASkill))
        self.append(skill)
