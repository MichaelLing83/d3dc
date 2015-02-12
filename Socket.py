from Unit import Unit

class Socket(Unit):
    def __init__(self, owner):
        super().__init__('socket')
        self.slot = None
        self.owner = owner
        if self.owner:
            self.slot = self.owner.slot
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
        self.gem.slot = self.slot
    def remove(self):
        gem = self.gem
        self.gem = None
        return gem
