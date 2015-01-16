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
    weapon_damage = (2122, 2122)
    weapon_base_APS = 1.4
    IAS_on_weapon = 0 / 100
    IAS_on_gear_and_paragon_points = 35 / 100

class WD:
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
    BotT =