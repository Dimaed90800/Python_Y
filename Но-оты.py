class Note:
    
    def __init__(self, highs, *lenght):
        self.high = highs
        self.is_long = False
        if lenght:
            self.is_long = lenght[0]
        self.long = ['до-о', 'ре-э', 'ми-и', 'фа-а', 'со-оль', 'ля-а', 'си-и']
        self.short = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
        
    def __str__(self):
        if self.is_long:
            return self.long[self.short.index(self.high)]
        return self.high

