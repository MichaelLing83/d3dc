from WitchDoctor import WitchDoctor
from Gems import GemOfEfficaciousToxin, PainEnhancer, FlawlessRoyalTopaz, Enforcer, BaneOfTheTrapped
from nose.tools import ok_, eq_
from random import seed, randint
from Item import Item
from Gear import Gear, Weapon
from Slot import Slot
from Hero import Hero
from PredefinedGears import StrongarmBracers, TaskerAndTheo, Unity, RingOfRoyalGrandeur, MaskOfJeram
from Skills import BigBadVoodoo, FetishArmy, CorpseSpiders, Piranhas, PierceTheVeil

def float_eq_(a, b):
    assert abs(a-b) < 0.001, "{a} != {b}".format(a=a, b=b)
"""
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
"""

"""
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
"""

"""
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
"""

"""
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
        unity = Unity()
        unity.intelligence = 471
        unity.criticalHitChanceIncreasedBy = 4.5 / 100
        unity.increaseDamageAgainstElites = 13 /100
        enforcer = Enforcer(28)
        unity.addSocket()
        unity.sockets[0].insert(enforcer)
        self.wd.ring_one.equip(unity)
        ## Ring Two
        ringOfRoyalGrandeur = RingOfRoyalGrandeur()
        ringOfRoyalGrandeur.intelligence = 461
        ringOfRoyalGrandeur.attackSpeedIncreasedBy = 7 / 100
        ringOfRoyalGrandeur.criticalHitDamageIncreasedBy = 45 / 100
        ringOfRoyalGrandeur.addSocket()
        ringOfRoyalGrandeur.sockets[0].insert(BaneOfTheTrapped(26))
        self.wd.ring_two.equip(ringOfRoyalGrandeur)
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
        doomBringer.intelligence = 695
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
        # Skills
        self.wd.skills.add(BigBadVoodoo('Slam Dance'))
        self.wd.skills.add(FetishArmy("Legion of Daggers"))
        # End of Skills
        print(self.wd)
        print("Critical Hit Chance Increased by {:03.1f}%".format(self.wd._criticalHitChanceIncreasedBy() * 100))
    def tearDown(self):
        pass
    def test_basic_stat(self):
        print()
        wd = WitchDoctor("Intelligence")
        wd.intelligence = 0
        zunimassasMarrow = Gear('Chest Armor', "Zunnimassa's Marrow", 'Set')
        zunimassasMarrow.armor = 688
        zunimassasMarrow.intelligence = 432
        zunimassasMarrow.vitality = 463
        zunimassasMarrow.increaseHauntDamageBy = 15 / 100
        zunimassasMarrow.criticalHitChanceIncreasedBy = 4 / 100
        zunimassasMarrow.addSocket()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.sockets[0].insert(FlawlessRoyalTopaz())
        zunimassasMarrow.sockets[1].insert(FlawlessRoyalTopaz())
        zunimassasMarrow.sockets[2].insert(FlawlessRoyalTopaz())
        wd.torso.equip(zunimassasMarrow)
        print("wd._intelligence() = {}".format(wd._intelligence()))
        assert(wd._intelligence() == 280 * 3 + 432)
        print("Critical Hit Chance Increased by {:03.1f}%".format(wd._criticalHitChanceIncreasedBy() * 100))
    def test_stats_from_gear(self):
        self.wd.intelligence = 0
        eq_(self.wd._intelligence(), 8064)
        eq_(int(self.wd._criticalHitChanceIncreasedBy() * 100), 43)
        eq_(int(self.wd._baseWeaponAps_E7() * 100), int(1.5 * 100))
        eq_(int(self.wd._totalAPS_E8() * 1000), int(1.605 * 1000))
        print("Increased Attack Speed on Gear and Paragon: {:03.1f}%".format(100*self.wd._increasedAttackSpeedOnGearAndParagon()))
        print("Attack Speed is {:06.3f} per Second".format(self.wd.attack_speed()))
        eq_(int(1.905 * 1000), int(self.wd.attack_speed() * 1000))
        print("Critical Hit Damage Increased by {:03.1f}%".format(self.wd._criticalHitDamageIncreasedBy() * 100))
        # basic damage from gears
        print("Damage from gears: {}".format(self.wd._baseDamage()))
        print("Damage with Fetish Army {}".format(self.wd._skillDamage("Fetish Army")))
"""

class TestPhoneutria:
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_damage(self):
        print()
        Phoneutria = WitchDoctor('Phoneutria')
        # Gears
        ##  Head
        maskOfJeram = MaskOfJeram(90 / 100)
        maskOfJeram.armor = 696
        maskOfJeram.intelligence = 680
        maskOfJeram.criticalHitChanceIncreasedBy = 5.5 / 100
        maskOfJeram.fireResistance = 146
        Phoneutria.head.equip(maskOfJeram)
        ## Shoulders
        aughildsPower = Gear('Shoulders', "Aughild's Power", "Set")
        aughildsPower.armor = 660
        aughildsPower.intelligence = 604
        aughildsPower.vitality = 647
        aughildsPower.life = 15 / 100
        Phoneutria.shoulders.equip(aughildsPower)
        ## Neck
        theFlavorOfTime = Gear('Amulet', "The Flavor of Time", 'Legendary')
        theFlavorOfTime.poisonSkillsDealMoreDamage += 20 / 100
        theFlavorOfTime.intelligence = 738
        theFlavorOfTime.criticalHitDamageIncreasedBy = 81 / 100
        theFlavorOfTime.addSocket()
        theFlavorOfTime.sockets[0].insert(PainEnhancer(31))
        Phoneutria.amulet.equip(theFlavorOfTime)
        ## Torso
        zunimassasMarrow = Gear('Chest Armor', "Zunnimassa's Marrow", 'Set')
        zunimassasMarrow.armor = 688
        zunimassasMarrow.intelligence = 432
        zunimassasMarrow.vitality = 463
        zunimassasMarrow.increaseHauntDamageBy = 15 / 100
        zunimassasMarrow.lightningResistance = 144
        zunimassasMarrow.addSocket()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.addSocket()
        zunimassasMarrow.sockets[0].insert(FlawlessRoyalTopaz())
        zunimassasMarrow.sockets[1].insert(FlawlessRoyalTopaz())
        zunimassasMarrow.sockets[2].insert(FlawlessRoyalTopaz())
        Phoneutria.torso.equip(zunimassasMarrow)
        ## Hands
        taskerAndTheo = TaskerAndTheo(50/100)
        taskerAndTheo.armor = 549
        taskerAndTheo.intelligence = 708
        taskerAndTheo.vitality = 707
        taskerAndTheo.criticalHitChanceIncreasedBy = 10 / 100
        Phoneutria.hands.equip(taskerAndTheo)
        ## Wrists
        aughildsSearch = Gear("Bracers", "Aughild's Search", "Set")
        aughildsSearch.poisonSkillsDealMoreDamage = 18 / 100
        aughildsSearch.intelligence = 595
        aughildsSearch.armor = 771
        aughildsSearch.criticalHitChanceIncreasedBy = 6 / 100
        aughildsSearch.fireResistance = 199
        Phoneutria.wrists.equip(aughildsSearch)
        ## Waist
        blackthornesNotchedBelt = Gear('Belt', "Blackthorne's Notched Belt", 'Set')
        blackthornesNotchedBelt.armor = 490
        blackthornesNotchedBelt.intelligence = 472
        blackthornesNotchedBelt.vitality = 434
        blackthornesNotchedBelt.resistanceToAllElements = 94
        Phoneutria.waist.equip(blackthornesNotchedBelt)
        ## Ring One
        unity = Unity()
        unity.intelligence = 471
        unity.criticalHitChanceIncreasedBy = 4.5 / 100
        unity.increaseDamageAgainstElites = 13 /100
        unity.addSocket()
        unity.sockets[0].insert(Enforcer(34))
        Phoneutria.ring_one.equip(unity)
        ## Ring Two
        ringOfRoyalGrandeur = RingOfRoyalGrandeur()
        ringOfRoyalGrandeur.intelligence = 461
        ringOfRoyalGrandeur.attackSpeedIncreasedBy = 7 / 100
        ringOfRoyalGrandeur.criticalHitDamageIncreasedBy = 45 / 100
        ringOfRoyalGrandeur.addSocket()
        ringOfRoyalGrandeur.sockets[0].insert(BaneOfTheTrapped(34))
        Phoneutria.ring_two.equip(ringOfRoyalGrandeur)
        ## Legs
        blackthornesJoustingMail = Gear('Pants', "Blackthorne's Jousting Mail", 'Set')
        blackthornesJoustingMail.armor = 1097
        blackthornesJoustingMail.intelligence = 598
        blackthornesJoustingMail.vitality = 622
        blackthornesJoustingMail.addSocket()
        blackthornesJoustingMail.addSocket()
        blackthornesJoustingMail.sockets[0].insert(FlawlessRoyalTopaz())
        blackthornesJoustingMail.sockets[1].insert(FlawlessRoyalTopaz())
        Phoneutria.legs.equip(blackthornesJoustingMail)
        ## Feet
        zunimassasTrail = Gear('Boots', "Zunimassa's Trail", 'Set')
        zunimassasTrail.armor = 905
        zunimassasTrail.intelligence = 495
        zunimassasTrail.resistanceToAllElements = 97
        Phoneutria.feet.equip(zunimassasTrail)
        ## MainHand
        theSpiderQueensGrasp = Weapon('Ceremonial Knife', "the Spider Queen's Grasp", "Legendary")
        theSpiderQueensGrasp.damage = (1608, 2409)
        theSpiderQueensGrasp.attacksPerSecond = 1.4
        theSpiderQueensGrasp.intelligence = 936
        Phoneutria.mainHand.equip(theSpiderQueensGrasp)
        ## OffHand
        zunimassasStringOfSkulls = Gear('Mojo', "Zunimassa's String of Skulls", 'Set')
        zunimassasStringOfSkulls.damage = (366, 446)
        zunimassasStringOfSkulls.intelligence = 728
        zunimassasStringOfSkulls.vitality = 662
        zunimassasStringOfSkulls.criticalHitChanceIncreasedBy = 9.5 / 100
        zunimassasStringOfSkulls.addSocket()
        zunimassasStringOfSkulls.sockets[0].insert(FlawlessRoyalTopaz())
        Phoneutria.offHand.equip(zunimassasStringOfSkulls)
        # End of Gears
        # Skills
        ## Active Skills
        Phoneutria.skills.add(CorpseSpiders('Leaping Spiders'))
        Phoneutria.skills.add(Piranhas("Wave of Mutilation"))
        Phoneutria.skills.add(BigBadVoodoo('Slam Dance'))
        Phoneutria.skills.add(FetishArmy("Head Hunters"))
        ## Passive Skills
        Phoneutria.skills.add(PierceTheVeil())
        # End of Skills

        # Paragon
        Phoneutria.paragon.mainStatPoint = 42
        # End of Paragon
        print(Phoneutria)

        # Checks from game info panel
        eq_(Phoneutria._intelligence(), 10275)
        # End of checks from game info panel

        # Checks from game DETAILS panel
        print()
        print("DETAILS")
        ## Offense
        print("OFFENSE")
        float_eq_(Phoneutria.damageIncreasedByInt(), 10275 / 100)
        print("Damage Increased by Intelligence\t{:,}%".format(Phoneutria.damageIncreasedByInt()*100))
        float_eq_(Phoneutria.damageIncreasedBySkills(), (20+15) / 100)
        # here we deviate from game details as we always count Piranha skill.
        print("Damage Increased by Skills\t{:04.2f}%".format(Phoneutria.damageIncreasedBySkills()*100))
        float_eq_(Phoneutria.bonusDamageToElites(), 38 / 100)
        print("Bonus Damage to Elites\t{:04.2f}%".format(Phoneutria.bonusDamageToElites()*100))
        # End of checks from game DETAILS panel

        print("Critical Hit Chance Increased by {:03.1f}%".format(Phoneutria._criticalHitChanceIncreasedBy() * 100))
        print("Damage from Fetish Army: {}".format(Phoneutria._skillDamage("Fetish Army")))
