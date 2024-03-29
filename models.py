class K:
    def __init__(self, label=None, **kwargs):
        assert(len(kwargs) == 1)
        for k, v in kwargs.items():
            self.id = k
            self.v = v
        self.label = label or self.id

class Konstants:
    def __init__(self, *args):
        self.klist = args
        for k in self.klist:
            setattr(self, k.id, k.v)

    def choices(self):
        return [(k.v, k.label) for k in self.klist]
    
    def active_choices(self):
        return [(k.v, k.label) for k in self.klist if k.v > -1 ]
    
    def keysandlabels(self):
        return [(k.v, k.id) for k in self.klist]
    
    def labels(self):
        return [k.label for k in self.klist]

    def display(self, k):
        for ks in self.klist:
            if k==ks.v: return ks.label
        return ""

    def __getitem__(self,k):
        return self.display(k)
    
    def __call__(self, l):
        for ks in self.klist:
            if l==ks.label: return ks.v
        return -1

