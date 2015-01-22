from WitchDoctor import WitchDoctor
from Gems import GemOfEfficaciousToxin
from nose.tools import ok_, eq_
from random import seed, randint

class TestLegendaryGem:
    def setUp(self):
        seed()
        lvls = [randint(0, 30) for x in range(3)]
        self.gems = [GemOfEfficaciousToxin(lvl) for lvl in lvls]
    def tearDown(self):
        pass
    def test__str__(self):
        for gem in self.gems:
            print(gem)

class TestWitchDoctor:
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_a(self):
        pass