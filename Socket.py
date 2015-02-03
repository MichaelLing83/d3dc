from Unit import Unit

class Socket(Unit):
    def __init__(self, owner):
        super().__init__('socket')
        self.owner = owner
        self.gem = None
    def __str__(self, prefix=''):
        s = ''
        if self.gem:
            s += self.gem.__str__(self.owner, prefix)
        else:
            s += 'Empty Socket'
        return s
    def insert(self, gem):
        self.gem = gem
    def remove(self):
        gem = self.gem
        self.gem = None
        return gem
    def _get_gem(self):
        return self.gem