import Square
from TicTacToeAction import TicTacToeAction

class TicTacToeState:
    def updateUtility(self):
        if ((self.field[0]==self.field[1] and self.field[1]==self.field[2] and self.field[0]!=Square.EMPTY)) or (self.field[3]==(self.field[4]) and self.field[4]==self.field[5] and self.field[3]!=(Square.EMPTY)) or (self.field[6]==self.field[7] and self.field[7]==self.field[8] and self.field[6]!=Square.EMPTY):
            if self.playerToMove==(Square.X):
                self.utility=-1
            else:
                self.utility=1
        elif ((self.field[0]==self.field[3] and self.field[3]==self.field[6] and self.field[0]!=(Square.EMPTY)) or (self.field[1]==(self.field[4]) and self.field[4]==(self.field[7]) and self.field[1]!=(Square.EMPTY)) or (self.field[2]==(self.field[5]) and self.field[5]==(self.field[8]) and self.field[2]!=(Square.EMPTY))):
            if (self.playerToMove==(Square.X)):
                self.utility=-1
            else:
                self.utility=1
        elif ((self.field[0]==(self.field[4]) and self.field[4]==(self.field[8]) and self.field[0]!=(Square.EMPTY)) or (self.field[2]==(self.field[4]) and self.field[4]==(self.field[6]) and self.field[2]!=(Square.EMPTY))):
            if (self.playerToMove==(Square.X)):
                self.utility=-1
            else:
                self.utility=1
        else:
            self.utility=0

    def __init__(self):
        self.field = []
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X
        self.playerToMove = Square.X
        self.utility = 0


    def getActions(self):
        list=[]
        for i in range(9):
            if (self.field[i]==(Square.EMPTY)):
                list.append(TicTacToeAction(Square.X, i))
        return list


    def getActions1(self):
        list = []
        for i in range(9):
            if (self.field[i] == (Square.EMPTY)):
                list.append(TicTacToeAction(Square.O, i))
        return list

    def getUtility(self):
        return self.utility

    def getResult(self,action):
        state = TicTacToeState()
        for i in range(9):
            if (i == action.getPosition()):
                state.field[i]=action.getPlayer()
            else:
                state.field[i]=self.field[i]
        if (action.getPlayer()==(Square.X)):
            state.playerToMove = Square.O
        else:
            state.playerToMove = Square.X
        state.updateUtility()
        return state

    def  isTerminal(self):
        if (self.utility == 1):
            return True
        if (self.utility == -1):
            return True
        num = 0
        for i in range(9):
            if (self.field[i]==(Square.EMPTY)):
                num+=1
        if (num == 0):
            return True
        return False

    def print(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)