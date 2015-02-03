from WitchDoctor import WitchDoctor
from Gems import GemOfEfficaciousToxin, PainEnhancer, FlawlessRoyalTopaz, Enforcer
from nose.tools import ok_, eq_
from random import seed, randint
from Item import Item
from Gear import Gear, Weapon
from Slot import Slot
from Hero import Hero
from PredefinedGears import StrongarmBracers, TaskerAndTheo, Unity

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
class TestHeadEtc:
    def setUp(self):
        print()
    def tearDown(self):
        pass
    def test_create(self):
        from Head import Head
        from Shoulders import Shoulders
        head = Head()
        shoulders = Shoulders()
        print(head)
        print(shoulders)
class TestGear:
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_create(self):
        gear = Gear('Helm', "LEORIC'S CROWN")

class TestSlot:
    def setUp(self):
        self.gear = Gear('Helm', "LEORIC'S CROWN")
    def tearDown(self):
        pass
    def test_create(self):
        for slot_type in Item.SLOT_TYPES:
            print(Slot(slot_type))
        slot = Slot('Head')
        slot.equip(self.gear)
        print(slot)

class TestHero:
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_create(self):
        hero = Hero('Witch Doctor', 'Nefarious')
        axe = Gear('Axe', 'Hand Axe')
        hero.mainHand.equip(axe)
        print(hero)
        #print(hero._slot_Head)


class TestWitchDoctor:
    def setUp(self):
        print()
        self.wd = WitchDoctor('Nefarious')
        # Gears
        ##  Head
        maskOfJeram = Gear('Helm', "Mask of Jeram", "Legendary")
        maskOfJeram.armor = 1318
        maskOfJeram.intelligence = 730
        maskOfJeram.criticalHitChanceIncreasedBy = 4.5 / 100
        self.wd.head.equip(maskOfJeram)
        ## Shoulders
        aughildsPower = Gear('Shoulders', "Aughild's Power", "Set")
        aughildsPower.armor = 660
        aughildsPower.intelligence = 604
        aughildsPower.vitality = 647
        self.wd.shoulders.equip(aughildsPower)
        ## Neck
        painEnhancer = PainEnhancer(27)
        theFlavorOfTime = Gear('Amulet', "The Flavor of Time", 'Legendary')
        theFlavorOfTime.physicalSkillsDealMoreDamage = 15 / 100
        theFlavorOfTime.resistanceToAllElements = 128
        theFlavorOfTime.criticalHitChanceIncreasedBy = 8.5 / 100
        theFlavorOfTime.movementSpeed = 12 / 100
        theFlavorOfTime.addSocket()
        theFlavorOfTime.sockets[0].insert(painEnhancer)
        self.wd.amulet.equip(theFlavorOfTime)
        ## Torso
        zunimassasMarrow = Gear('Chest Armor', "Zunnimassa's Marrow", 'Set')
        zunimassasMarrow.armor = 688
        zunimassasMarrow.intelligence = 432
        zunimassasMarrow.vitality = 463
        zunimassasMarrow.increaseHauntDamageBy = 15 / 100
        flawlessRoyalTopaz = FlawlessRoyalTopaz()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.sockets[0].insert(flawlessRoyalTopaz)
        zunimassasMarrow.sockets[1].insert(flawlessRoyalTopaz)
        zunimassasMarrow.sockets[2].insert(flawlessRoyalTopaz)
        self.wd.torso.equip(zunimassasMarrow)
        ## Ring One
        gemOfEfficaciousToxin = GemOfEfficaciousToxin(27)
        theTallMansFinger = Gear('Ring', "The Tall Man's Finger", 'Legendary')
        theTallMansFinger.addSocket()
        theTallMansFinger.sockets[0].insert(gemOfEfficaciousToxin)
        self.wd.ring_one.equip(theTallMansFinger)
        ## Ring Two
        unity = Unity()
        unity.intelligence = 471
        unity.criticalHitChanceIncreasedBy = 4.5 / 100
        unity.increaseDamageAgainstElites = 13 /100
        enforcer = Enforcer(28)
        unity.addSocket()
        unity.sockets[0].insert(enforcer)
        self.wd.ring_two.equip(unity)
        ## Waist
        blackthornesNotchedBelt = Gear('Belt', "Blackthorne's Notched Belt", 'Set')
        blackthornesNotchedBelt.armor = 490
        blackthornesNotchedBelt.intelligence = 472
        blackthornesNotchedBelt.vitality = 434
        blackthornesNotchedBelt.resistanceToAllElements = 94
        self.wd.waist.equip(blackthornesNotchedBelt)
        ## Legs
        blackthornesJoustingMail = Gear('Pants', "Blackthorne's Jousting Mail", 'Set')
        blackthornesJoustingMail.armor = 1097
        blackthornesJoustingMail.intelligence = 598
        blackthornesJoustingMail.vitality = 622
        blackthornesJoustingMail.addSocket()
        blackthornesJoustingMail.addSocket()
        blackthornesJoustingMail.sockets[0].insert(flawlessRoyalTopaz)
        blackthornesJoustingMail.sockets[1].insert(flawlessRoyalTopaz)
        self.wd.legs.equip(blackthornesJoustingMail)
        ## Wrists
        strongarmBracers = StrongarmBracers(30/100)
        strongarmBracers.armor = 409
        strongarmBracers.physicalSkillsDealMoreDamage = 19 / 100
        strongarmBracers.vitality = 428
        strongarmBracers.criticalHitChanceIncreasedBy = 6 / 100
        strongarmBracers.lifePerHit = 8962
        self.wd.wrists.equip(strongarmBracers)
        ## Hands
        taskerAndTheo = TaskerAndTheo(50/100)
        taskerAndTheo.armor = 549
        taskerAndTheo.intelligence = 708
        taskerAndTheo.vitality = 707
        taskerAndTheo.criticalHitChanceIncreasedBy = 10 / 100
        self.wd.hands.equip(taskerAndTheo)
        ## Feet
        zunimassasTrail = Gear('Boots', "Zunimassa's Trail", 'Set')
        zunimassasTrail.armor = 556
        zunimassasTrail.intelligence = 485
        zunimassasTrail.vitality = 468
        zunimassasTrail.resistanceToAllElements = 91
        zunimassasTrail.movementSpeed = 11 / 100
        self.wd.feet.equip(zunimassasTrail)
        ## MainHand
        doomBringer = Weapon('Sword', 'Doombringer', 'Legendary')
        doomBringer.damage = (1344, 1800)
        doomBringer.attacksPerSecond = 1.5
        self.wd.mainHand.equip(doomBringer)
        ## OffHand
        zunimassasStringOfSkulls = Gear('Mojo', "Zunimassa's String of Skulls", 'Set')
        zunimassasStringOfSkulls.damage = (366, 446)
        zunimassasStringOfSkulls.intelligence = 728
        zunimassasStringOfSkulls.vitality = 662
        zunimassasStringOfSkulls.criticalHitChanceIncreasedBy = 9.5 / 100
        zunimassasStringOfSkulls.addSocket()
        zunimassasStringOfSkulls.sockets[0].insert(flawlessRoyalTopaz)
        self.wd.offHand.equip(zunimassasStringOfSkulls)
        # End of Gears
        print(self.wd)
    def tearDown(self):
        pass
    def test_basic_stat(self):
        ok_(self.wd.intelligence > 0)