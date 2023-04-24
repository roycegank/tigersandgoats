'''
Huligutta (Goats and Tigers)
file: game.py
Description: GUI of the game using TKinter
'''

__author__ = "Cameron Canda and group"
__status__ = "Dev"

# from functions import positions

class Game:
    def __init__(self):
        self.boardPositions = {
            'b0': None,'a1': None,'a2': None,'a3': None,
            'b1': None,'b2': None,'b3': None,'b4': None,
            'c1': None,'c2': None,'c3': None,'c4': None,
            'd1': None,'d2': None,'d3': None,'d4': None,
            'e1': None,'e2': None,'e3': None,'e4': None,
            'f1': None,'f2': None,'f3': None
            }
        self.goatCount = 20
        self.goatEaten = 0
        self.selectedPiece = None
        
    def getAdjacentPositions(self, position):
        # This function returns a list of positions adjacent to the given position.
        # It checks if each adjacent position is on the board and if it is empty.
        row, col = self.getRowAndCol(position)
        adjacentPositions = []
        if row > 0 and self.boardPositions[self.getPosition(row-1, col)] is None:
            adjacentPositions.append(self.getPosition(row-1, col))
        if row < 4 and self.boardPositions[self.getPosition(row+1, col)] is None:
            adjacentPositions.append(self.getPosition(row+1, col))
        if col > 0 and self.boardPositions[self.getPosition(row, col-1)] is None:
            adjacentPositions.append(self.getPosition(row, col-1))
        if col < 2 and self.boardPositions[self.getPosition(row, col+1)] is None:
            adjacentPositions.append(self.getPosition(row, col+1))
        return adjacentPositions
        
    def getPosition(self, row, col):
        # This function returns the position string for the given row and column.
        return chr(97 + col) + str(row)
    
    def getRowAndCol(self, position):
        # This function returns the row and column for the given position string.
        col = ord(position[0]) - 97
        row = int(position[1])
        return row, col
        
    def allpossiblemovesGoats(self, positions, goatCount):
        M = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]  # the adjacency matrix for the board
        for position, value in positions.items():
            if value == "O":
                row, col = self.getRowAndCol(position)
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if M[i+1][j+1] == 1 and row+i >= 0 and row+i <= 4 and col+j >= 0 and col+j <= 2:
                            adjacentPosition = self.getPosition(row+i, col+j)
                            if self.boardPositions[adjacentPosition] is None:
                                print(position + ' to ' + adjacentPosition)

    def allpossiblemovesTigers(self, positions, tigerCount):
        for position, value in positions.items():
            if value == "X":
                print(position)

def valueOfPosition(self, boardPositions-given, goatCount, goatEaten, *args):
        if self.goatCount == 0:
            return
        global noGoat_noTiger
        global noGoat_oneTiger
        global noGoat_twoTiger
        global oneGoat_noTiger
        global oneGoat_oneTiger
        global twoGoat_noTiger
        if args:
            if args[0] == "default":
                print("DEBUG: randomized values")
                noGoat_noTiger = random.randint(0,10)
                noGoat_oneTiger = random.randint(-10,0)
                noGoat_twoTiger = random.randint(0,10)
                oneGoat_noTiger = random.randint(0,10)
                oneGoat_oneTiger = random.randint(0,10)
                twoGoat_noTiger = random.randint(0,10)
        else:
            print("DEBUG: set values")
            noGoat_noTiger = 1
            noGoat_oneTiger = -1
            noGoat_twoTiger = 1
            oneGoat_noTiger = 1
            oneGoat_oneTiger = 1
            twoGoat_noTiger = 1
        # Mobility Value
        tigerPos = tigerPositions(boardPositions-given)
        mobilityval = 0
        for tiger in tigerPos:
            print("Tiger [",tiger,"]: mobilityval = ",len(Piece(tiger).possibleMoves()))
            mobilityval = mobilityval + len(Piece(tiger).possibleMoves())
        # Safety Value (WIP)
        goatPos = goatPositions(boardPositions-given)
        safetyval = 0
        for goat in goatPos:
                print("Goat [",goat,"]")
            #if random.randint(0,1) == 0:
            #    print("SKIP GOAT")
            #    continue
            #else:
                # Horizontal Check
                goatCount = 0
                tigerCount = 0
                for neighbors in Position(goat[0],goat[1]).get_horizontal_neighbors():
                    if Position(neighbors[0],neighbors[1]).content() == 'O':
                        goatCount = goatCount + 1
                    elif Position(neighbors[0],neighbors[1]).content() == 'X':
                        tigerCount = tigerCount + 1
                print("   Horizontal-Check: ", end = '')
                print("goatCount = ",goatCount,"tigerCount = ",tigerCount, end = '')
                safetyval = safetyval + self.checkValue(goatCount,tigerCount)
                # Vertical Check
                goatCount = 0
                tigerCount = 0
                for neighbors in Position(goat[0],goat[1]).get_vertical_neighbors():
                    if Position(neighbors[0],neighbors[1]).content() == 'O':
                        goatCount = goatCount + 1
                    elif Position(neighbors[0],neighbors[1]).content() == 'X':
                        tigerCount = tigerCount + 1
                print("   Vertical-Check  : ", end = '')
                print("goatCount = ",goatCount,"tigerCount = ",tigerCount, end = '')
                safetyval = safetyval + self.checkValue(goatCount,tigerCount)
        weight = 0.5 #random.uniform(0,1)
        maxmobilityval = 4
        maxsafetyval = 2*max(noGoat_noTiger, noGoat_oneTiger, noGoat_twoTiger, oneGoat_noTiger, oneGoat_oneTiger, twoGoat_noTiger)
        avgsafetyval = safetyval/self.goatCount
        avgmobilityval = mobilityval/3
        if self.goatEaten == 5:
            winprob = 0
        elif len(Piece(tiger).possibleMoves()) == 0:
            winprob = 1
        else:
            winprob = (weight)*(avgsafetyval/maxsafetyval)+(1-weight)*(1-(avgmobilityval/maxmobilityval))
        print("DEBUG: weight = ", weight)
        print("DEBUG: mobilityval = ", mobilityval)
        print("DEBUG: safetyval = ", safetyval)
        print("DEBUG: avgmobilityval = ", avgmobilityval)
        print("DEBUG: avgsafetyval = ", avgsafetyval)
        print("DEBUG: maxmobilityval = ", maxmobilityval)
        print("DEBUG: maxsafetyval = ", maxsafetyval)
        print("DEBUG: winprob = ", winprob)
        
    def checkValue(self,goatCount,tigerCount): # Does not include impossibles
        print(" checkValue: ", end = '')
        if goatCount == 0 and tigerCount == 0:
            print(noGoat_noTiger)
            return noGoat_noTiger
        elif goatCount == 0 and tigerCount == 1:
            print(noGoat_oneTiger)
            return noGoat_oneTiger
        elif goatCount == 0 and tigerCount == 2:
            print(noGoat_twoTiger)
            return noGoat_twoTiger
        elif goatCount == 1 and tigerCount == 0:
            print(oneGoat_noTiger)
            return oneGoat_noTiger
        elif goatCount == 1 and tigerCount == 1:
            print(oneGoat_oneTiger)
            return oneGoat_oneTiger
        elif goatCount == 2 and tigerCount == 0:
            print(twoGoat_noTiger)
            return twoGoat_noTiger
            
