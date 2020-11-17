class BigBell:
    f = 0
    def sound(self):
        if not self.f :
            print('ding')
            self.f = 1
        else:
            print('dong')
            self.f = 0


