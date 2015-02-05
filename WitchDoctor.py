#!/usr/bin/env python3

from Hero import Hero

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

class WitchDoctor(Hero):
    def __init__(self, name):
        super().__init__('Witch Doctor', name)
    def __str__(self, prefix=''):
        return super().__str__(prefix)