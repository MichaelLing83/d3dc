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

def property_str(s):
    return colored(s, "blue")

def number_str(s):
    return colored(s, "cyan")

# Gear quality strings
def _normal(s):
    return colored(s, "white")

def _unusual(s):
    return colored(s, "blue")

def _rare(s):
    return colored(s, "yellow")

def _legendary(s):
    return colored(s, "magenta")

def _set(s):
    return colored(s, "green")