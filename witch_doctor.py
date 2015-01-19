#!/usr/bin/env python3

'''
Abbreviations:
    BotT:   Bane of the Trapped
    CHC:    Critical Hit Chance
    CHD:    Critical Hit Damage
    FA:     Fetish Army
    IAS:    Increased Attack Speed
    Intel:  Intelligence
    MoJ:    Mask of Jeram
    SZD:    Summon Zombie Dogs
'''

class SheetStat:
    intel = 9400
    CHC = 50.5 / 100
    CHD = 403 / 100
    weapon_damage = 2122
    weapon_base_APS = 1.4
    IAS_on_weapon = 0 / 100
    IAS_on_gear_and_paragon_points = 35 / 100

class WitchDoctor:
    # Input gear
    mask = ("Mask of Jeram", "Carnevil", "Other")[0]
    MoJ_increase_pet_damage_rate = 79 / 100
    cold_damage_increase_rate = 0 / 100
    physical_damage_increase_rate = 0 / 100
    fire_damage_increase_rate = 0 / 100
    poison_damage_increase_rate = 0 / 100
    FA_damage_increase_rate = 0 / 100
    SZD_damage_increase_rate = 0 / 100
    Gargantuan_damage_increase_rate = 0 / 100
    damage_increase_against_elites = 0 / 100
    # Legendary gems
    Enforcer = 22.5 / 100
    BotT = 0 / 100
    use_Gem_of_Efficacious_Toxin_lvl_25 = True
    use_Tall_Mans_Finger = False
    use_Tasker_and_Theo = True
    Tasker_and_Theo_speed_increase = 50 / 100
    Fetish_Army_rune = "Dagger"
    Summon_Zombie_Dogs_rune = "Physical"
    Gargantuan_rune = "Restless Giant"
    use_BBV_Slam_Dance = True
    use_PTV_passive = True
    use_Piranhas = True
    use_Midnight_Feast_passive = True

    @staticmethod
    def base_weapon_APS():
        return (1 + SheetStat.IAS_on_weapon) * SheetStat.weapon_base_APS

    @staticmethod
    def total_APS():
        return (1 + SheetStat.IAS_on_gear_and_paragon_points) * base_weapon_APS()

    @staticmethod
    def buffed_APS():
        """
        =IF(B45="Yes";(1+B8+E46)*E7;E8)
        """
        if WitchDoctor.use_BBV_Slam_Dance:
            return (1 + SheetStat.IAS_on_gear_and_paragon_points + 0.2) * SheetStat.weapon_base_APS
        else:
            return WitchDoctor.total_APS()

    @staticmethod
    def damage_increase_physical_skills():
        """
        =IF(B$11="Mask of Jeram";(C$12+(C$15-1)+(C$23-1));C$15+(C$23-1))
        """
        if WitchDoctor.mask == "Mask of Jeram":
            return (1 + WitchDoctor.MoJ_increase_pet_damage_rate) + (WitchDoctor.physical_damage_increase_rate - 1) + WitchDoctor.Enforcer
        else:
            return WitchDoctor.physical_damage_increase_rate + WitchDoctor.Enforcer

    @staticmethod
    def calculate_FA():
        """=IF(C$36="Cold";
            (B$5+(B$5*C$2/100))*E$9*1,8*D$14*C$18*C$31*C$57*C$24;
            IF(C$36="Physical";
            (B$5+(B$5*C$2/100))*E$9*1,8*D$15*C$18*C$31*C$57*C$24;
            IF(C$36="Fire";
            (B$5+(B$5*C$2/100))*E$9*1,8*D$16*C$18*C$31*C$57*C$24;
            IF(C$36="Poison";
            (B$5+(B$5*C$2/100))*E$9*1,8*D$17*C$18*C$31*C$57*C$24))))"""
        if WitchDoctor.Fetish_Army_rune == "Dagger":
            return (SheetStat.weapon_damage + SheetStat.weapon_damage * SheetStat.intel / 100) * WitchDoctor.buffed_APS() * 1.8 * WitchDoctor.damage_increase_physical_skills() * (1 + WitchDoctor.FA_damage_increase_rate) * 1 * 1.8 * (1 + WitchDoctor.BotT)

if __name__ == '__main__':
    print(WitchDoctor.calculate_FA())
