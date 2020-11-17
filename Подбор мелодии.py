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


class Melody:

    def __init__(self, arr=[]):
        if arr:
            self.arr = arr
        else:
            self.arr = []

    def __str__(self):
        ans = ', '.join([str(i) for i in self.arr])
        if not self.arr:
            return ''
        return ans[0].upper() + ans[1:]

    def append(self, item):
        self.arr.append(item)

    def replace_last(self, nt):
        self.arr[-1] = nt

    def remove_last(self):
        self.arr = self.arr[:-1]

    def clear(self):
        self.arr = []

    def __len__(self):
        return len(self.arr)

    def __rshift__(self, num):
        L = []
        for i in self.arr:
            if (i.high + num) // 7 != 0:
                return self.arr
            L.append(i >> num)
        return Melody(L)

    def __lshift__(self, num):
        L = []
        for i in self.arr:
            a = (i.high - num)
            if (i.high - num) < 0:
                a = ((- i.high) + num)
            if a // 7 != 0:
                return self.arr
            L.append(i << num)
        return Melody(L)
