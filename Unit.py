class Unit:
    '''
    '''
    id_count = 0
    def __init__(self, name):
        self.name = name
        self.id = Unit.id_count
        Unit.id_count += 1
    def __str__(self):
        return """Name: {name}""".format(name=self.name)