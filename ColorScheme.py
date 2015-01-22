from termcolor import colored

active_c = "cyan"
active_legendary_c = "magenta"
deactive_c = "white"
warn_c = "red"
improvable_c = "blue"

def active_str(s):
    return colored(s, active_c)

def active_legendary_str(s):
    return colored(s, active_legendary_c)

def deactive_str(s):
    return colored(s, deactive_c)

def warn_str(s):
    return colored(s, warn_c)

def improvable_str(s):
    return colored(s, improvable_c)