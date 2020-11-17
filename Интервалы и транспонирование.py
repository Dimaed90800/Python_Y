PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта",
             "секста", "септима"]
N = 7


class Note:

    def __init__(self, high, *lenght):
        self.high = PITCHES.index(high)
        self.long = False
        if lenght:
            self.long = lenght[0]

    def __rshift__(self, num):
        return Note(PITCHES[(self.high + num) % N], self.long)

    def __lshift__(self, num):
        return Note(PITCHES[(self.high - num) % N], self.long)

    def get_interval(self, note):
        return INTERVALS[max([self.high - note.high, note.high - self.high])]

    def __str__(self):
        if self.long:
            return LONG_PITCHES[self.high]
        else:
            return PITCHES[self.high]

    def __lt__(self, note):
        return self.high < note.high

    def __le__(self, note):
        return self.high <= note.high

    def __eq__(self, note):
        return self.high == note.high

    def __ne__(self, note):
        return self.high != note.high

    def __gt__(self, note):
        return self.high > note.high

    def __ge__(self, note):
        return self.high >= note.high
