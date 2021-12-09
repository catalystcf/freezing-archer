import numpy as np

class Field(object):
    def __init__(self):
        self.F = np.zeros((1000,1000))

    def addVent(self, x1,y1,x2,y2):
        if x1 == x2:
            self.addVerticalVent(x1, y1, y2)
        elif y1 == y2:
            self.addHorizontalVent(x1, x2, y1)
        else:
            raise ValueError( "NOT a line")

    def addVerticalVent(self, x1,y1,y2):
        if y2 < y1:
            t = y1
            y1 = y2
            y2 = t

        for y in range(y1,y2+1):
            self.F[x1, y] += 1

    def addHorizontalVent(self, x1,x2,y1):
        if x2 < x1:
            t = x1
            x1 = x2
            x2 = t
        for x in range(x1,x2+1):
            self.F[x, y1] += 1
    
    def  __repr__(self):
        return str(self.F)

    __str__ = __repr__

if __name__ == '__main__':
    DAY = 5
    file = open('aoc2021/inputs/DATA_%s.py' % DAY, 'r') 
    #file = open('aoc2021/inputs/MOCK_%s.py' % DAY, 'r') 
    
    field = Field()
    vents = file.readlines()
    for vent in vents:
        if not vent:
            continue

        (start, arrow, end)  = vent.split(' ')
        (x1,y1) = [int(x) for x in start.split(',')]
        (x2,y2) = [int(x) for x in end.split(',')]

        if x1 == x2 or y1 == y2:
            field.addVent(x1,y1,x2,y2)

    print(sum(sum(field.F>1)))
