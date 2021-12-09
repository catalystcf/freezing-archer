from collections import defaultdict

def convert(line):
    ''' string to numbers '''
    l = line.strip()
    return [int(x) for x in l.split(' ') if x ]

class Board(object):
    def __init__( self, lines ):
        self.rows = [{} for x in range(5)]
        self.cols = [{} for x in range(5)]

        lines = [ convert(x) for x in lines ]

        for r in range(5):
            line = lines[r]
            for c in range(5):
                self.rows[r][line[c]] = False

        
        for c in range(5):
            for r in range(5):
                line = lines[r]
                self.cols[c][line[c]] = False    

    def isWin(self):
        for r in range(5):
            if sum(self.cols[r].values()) == 5:
                return True
            if sum(self.rows[r].values()) == 5:
                 return True
        return False

    def unmarked(self):
        sumT = 0
        for r in range(5):
            sumT += sum([ k for k,v in self.rows[r].items() if not v])
        return sumT

    def call(self, num):
        for r in range(5):
            if num in self.cols[r]:
                self.cols[r][num] = True  
            if num in self.rows[r]:
                self.rows[r][num] = True

    def __repr__(self):
        s = ''
        for r in range(5):
            for k,v in self.rows[r].items():
                if (v):
                    s+= "*"
                else:
                    s+= " "
                if k < 10:
                    s+= " " + str(k)
                else:
                    s+= str(k)
                    
            s += '\n'
        return s

    __str__ = __repr__



if __name__ == '__main__':
    DAY = 4
    file = open('aoc2021/inputs/DATA_%s.py' % DAY, 'r') 
    #file = open('aoc2021/inputs/MOCK_%s.py' % DAY, 'r') 
    calls = file.readline()

    # skip
    line = file.readline()

    boards = []
    while line != '':
        l1 = file.readline().strip()
        l2 = file.readline().strip()
        l3 = file.readline().strip()
        l4 = file.readline().strip()
        l5 = file.readline().strip()

        b =Board([ l1,l2,l3,l4,l5] )

        print( "BOARD = \n" , b)
        boards.append(b )
        line = file.readline()

    for call in calls.split(','):
        call = int(call)
        for board in boards:
            board.call(call)
            if board.isWin():
                unmarked = board.unmarked()
                print(unmarked*call)
                raise AttributeError("WON")
                
        
    



    

  