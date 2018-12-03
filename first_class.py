class Lift:
    """ Lift Class: """
    max_weight = 120
    status = 'closed'
    def __init__(self, f, s):
        self.floor = f
        #self.status = s
    
    def open(self):
        self.status = 'open'
        print("Opening Lift.")
    
    def close(self):
        self.status = 'closed'
        print(self.status)


class ClosedLift:
    """ Default value of 'closed' """
    def __init__(self, f, l, s='closed'):
        self.floor = f
        self.status = s
        self.locked = l
    
    def open(self):
        self.status = 'open'
    
    def close(self):
        self.status = 'closed'

class ToggleLift:
    """ Default value of 'closed' """
    max_weight = 120    
    def __init__(self, f, l, s='closed'):
        self.floor = f
        self.status = s
        self.locked = l
    
    def open(self):
        self.status = 'open'
        print(self.status)
    
    def close(self):
        self.status = 'closed'
        print(self.status)

    def toggle(self):
        # if self.status == 'open'
        #     self.status = 'closed'
        # else:
        #     self.status = 'open'
        if self.status == 'open':
            self.close()
        else:
            self.open()
        print(self.status)
        print("updated!")

class SecurityLift(Lift):
    def __init__(self, f, s, l=False):
        super().__init__(f, s)
        self.locked = l
        
    def open(self):
        print("Locked:", self.locked)
        if not self.locked:
            print("security check...")
            super().open()
        else:
            print("Lift is locked!")

    def close(self, l=False):
        super().close()
        self.locked = l
        print("Locked =", self.locked)
        
    def close_and_lock(self):
        self.close(l=True)
