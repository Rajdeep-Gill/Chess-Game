import os

class Pawn:
    def __init__(self, color, pos, hasMoved=False):
        self.pos = pos
        self.color = color
        self.hasMoved = hasMoved

        if self.color == 'white':
            self.icon = '♙'
        else:
            self.icon = '♟︎'

    def __str__(self):
        return self.icon

    def getMoves(self):
        if self.color == 'white':
            moves = [[self.pos[0] - 1, self.pos[1]]] # up 1
            if self.hasMoved == False:
                moves.append([self.pos[0] - 2, self.pos[1]]) # up 1 and up 2

            #check the piece top left
            if (self.pos[0] - 1 >= BOARD_MIN and self.pos[1] - 1 >= BOARD_MIN):
                topLeft = board.getPiece(self.pos[0] - 1, self.pos[1] - 1)
                if(topLeft != "" and topLeft.color != self.color):
                    moves.append([self.pos[0] - 1, self.pos[1] - 1])

            #check the piece top right
            if(self.pos[0] - 1 >= BOARD_MIN and self.pos[1] + 1 <= BOARD_MAX):
                topRight = board.getPiece(self.pos[0] - 1, self.pos[1] + 1)
                if(topRight != "" and topRight.color != self.color):
                    moves.append([self.pos[0] - 1, self.pos[1] + 1])

        else:
            moves = [[self.pos[0] + 1, self.pos[1]]]
            if self.hasMoved == False:
                moves.append([self.pos[0] + 2, self.pos[1]])

            #check the piece bottom left
            if (self.pos[0] + 1 <= BOARD_MAX and self.pos[1] - 1 >= BOARD_MIN):
                bottomLeft = board.getPiece(self.pos[0] + 1, self.pos[1] - 1)
                if(bottomLeft != "" and bottomLeft.color != self.color):
                    moves.append([self.pos[0] + 1, self.pos[1] - 1])

            #check the piece bottom right
            if (self.pos[0] + 1 <= BOARD_MAX and self.pos[1] + 1 <= BOARD_MAX):
                bottomRight = board.getPiece(self.pos[0] + 1, self.pos[1] + 1)
                if(bottomRight != "" and bottomRight.color != self.color):
                    moves.append([self.pos[0] + 1, self.pos[1] + 1])

        for i in range(len(moves) -1, -1, -1):
            # checks if the move is out of bounds
            if moves[i][0] > BOARD_MAX or moves[i][0] < BOARD_MIN or moves[i][1] > BOARD_MAX or moves[i][1] < BOARD_MIN:
                moves.remove(moves[i])

        return moves

    def promotePawn(self):
        pass
        print('1. Queen')
        print('2. Rook')
        print('3. Bishop')
        print('4. Knight')

        promotedPiece = int(input("Promote pawn to: "))

        if promotedPiece == 1:
            board.board[self.pos[0]][self.pos[1]] = Queen(self.color, self.pos)
        elif promotedPiece == 2:
            board.board[self.pos[0]][self.pos[1]] = Rook(self.color, self.pos)
        elif promotedPiece == 3:
            board.board[self.pos[0]][self.pos[1]] = Bishop(self.color, self.pos)
        elif promotedPiece == 4:
            board.board[self.pos[0]][self.pos[1]] = Knight(self.color, self.pos)

    def checkEnPassant(self, oldBoard):
        # checks if the pawn is next to another pawn
        if self.color == 'white':
            if self.pos[1] + 1 <= BOARD_MAX:
                rightPiece = board.getPiece(self.pos[0], self.pos[1] + 1)
                if isinstance(rightPiece, Pawn) and rightPiece.color != self.color and rightPiece.pos[0] == self.pos[0]: # checks if the piece is a pawn and is the opposite color and is on the same row
                    if oldBoard[rightPiece.pos[0] - 1][rightPiece.pos[1]] == "" and board.getPiece(rightPiece.pos[0] - 1, rightPiece.pos[1]) == "": # checks if the pawn moved 2 spaces
                        return [rightPiece.pos[0] - 1, rightPiece.pos[1]]

            if self.pos[1] - 1 >= BOARD_MIN:
                leftPiece = board.getPiece(self.pos[0], self.pos[1] - 1)
                if isinstance(leftPiece, Pawn) and leftPiece.color != self.color and leftPiece.pos[0] == self.pos[0]: # checks if the piece is a pawn and is the opposite color and is on the same row
                    if oldBoard[leftPiece.pos[0] - 1][leftPiece.pos[1]] == "" and board.getPiece(leftPiece.pos[0] - 1, leftPiece.pos[1]) == "": # checks if the pawn moved 2 spaces
                        return [leftPiece.pos[0] - 1, leftPiece.pos[1]]
        else:
            if self.pos[1] + 1 <= BOARD_MAX:
                rightPiece = board.getPiece(self.pos[0], self.pos[1] + 1)
                if isinstance(rightPiece, Pawn) and rightPiece.color != self.color and rightPiece.pos[0] == self.pos[0]:
                    if oldBoard[rightPiece.pos[0] + 1][rightPiece.pos[1]] == "" and board.getPiece(rightPiece.pos[0] + 1, rightPiece.pos[1]) == "":
                        return [rightPiece.pos[0] + 1, rightPiece.pos[1]]

            if self.pos[1] - 1 >= BOARD_MIN:
                leftPiece = board.getPiece(self.pos[0], self.pos[1] - 1)
                if isinstance(leftPiece, Pawn) and leftPiece.color != self.color and leftPiece.pos[0] == self.pos[0]:
                    if oldBoard[leftPiece.pos[0] + 1][leftPiece.pos[1]] == "" and board.getPiece(leftPiece.pos[0] + 1, leftPiece.pos[1]) == "":
                        return [leftPiece.pos[0] + 1, leftPiece.pos[1]]

        return False

class Knight:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color

        if self.color == 'white':
            self.icon = '♘'
        else:
            self.icon = '♞'

    def __str__(self):
        return self.icon

    def getMoves(self):
        moves = [[self.pos[0] + 2, self.pos[1] + 1], [self.pos[0] + 2, self.pos[1] - 1], # up 2, left 1 and right 1
                 [self.pos[0] - 2, self.pos[1] + 1], [self.pos[0] - 2, self.pos[1] - 1], # down 2, left 1 and right 1
                 [self.pos[0] + 1, self.pos[1] + 2], [self.pos[0] - 1, self.pos[1] + 2], # right 2, up 1 and down 1
                 [self.pos[0] + 1, self.pos[1] - 2], [self.pos[0] - 1, self.pos[1] - 2]] # left 2, up 1 and down 1

        for i in range(len(moves) -1, -1, -1):
            # checks if the move is out of bounds
            if moves[i][0] > BOARD_MAX or moves[i][0] < BOARD_MIN or moves[i][1] > BOARD_MAX or moves[i][1] < BOARD_MIN:
                moves.remove(moves[i])

        for i in range(len(moves) -1, -1, -1):
            piece = board.getPiece(moves[i][0], moves[i][0]) 
            if piece != '':
                if piece.color == self.color:
                    moves.remove(moves[i])

        return moves

class Bishop:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color

        if self.color == 'white':
            self.icon = '♗'
        else:
            self.icon = '♝'

    def __str__(self):
        return self.icon

    def getMoves(self):
        moves = []
        capturePieces = []

        for i in range(1,8): # checks all spaces top right diagonal
            if self.pos[0] + i <= BOARD_MAX and self.pos[1] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0] + i, self.pos[1] + i) == "":
                    moves.append([self.pos[0] + i, self.pos[1] + i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] + i, self.pos[1] + i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces bottom right diagonal
            if self.pos[0] - i >= BOARD_MIN and self.pos[1] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0] - i, self.pos[1] + i) == "":
                    moves.append([self.pos[0] - i, self.pos[1] + i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] - i, self.pos[1] + i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces top left diagonal
            if self.pos[0] + i <= BOARD_MAX and self.pos[1] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] + i, self.pos[1] - i) == "":
                    moves.append([self.pos[0] + i, self.pos[1] - i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] + i, self.pos[1] - i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces bottom left diagonal
            if self.pos[0] - i >= BOARD_MIN and self.pos[1] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] - i, self.pos[1] - i) == "":
                    moves.append([self.pos[0] - i, self.pos[1] - i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] - i, self.pos[1] - i))
                    break
            else:
                break

        # checks all capture pieces to see if they are the same color and removes them from the list
        for piece in capturePieces:
            if piece != "" and piece != "■":
                if piece.color != self.color:
                    moves.append(piece.pos)

        return moves

class Rook:
    def __init__(self, color, pos, hasMoved=False):
        self.pos = pos
        self.color = color
        self.hasMoved = hasMoved

        if self.color == 'white':
            self.icon = '♖'
        else:
            self.icon = '♜'

    def __str__(self):
        return self.icon

    def getMoves(self):
        moves = []
        capturePieces = []

        for i in range(1,8): # checks all spaces above the rook
            if self.pos[0] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0] + i, self.pos[1]) == "":
                    moves.append([self.pos[0] + i, self.pos[1]])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] + i, self.pos[1]))
                    break
            else:
                break

        for i in range(1, 8): # checks all spaces below the rook
            if self.pos[0] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] - i, self.pos[1]) == "":
                    moves.append([self.pos[0] - i, self.pos[1]])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] - i, self.pos[1]))
                    break
            else:
                break

        for i in range(1, 8): # checks all spaces to the right of the rook
            if self.pos[1] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0], self.pos[1] + i) == "":
                    moves.append([self.pos[0], self.pos[1] + i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0], self.pos[1] + i))
                    break
            else:
                break

        for i in range(1, 8): # checks all spaces to the left of the rook
            if self.pos[1] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] , self.pos[1] - i) == "":
                    moves.append([self.pos[0], self.pos[1] - i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0], self.pos[1] - i))
                    break
            else:
                break

        # checks all capture pieces to see if they are the same color and removes them from the list
        for piece in capturePieces:
            if piece != "" and piece != "■":
                if piece.color != self.color:
                    moves.append(piece.pos)

        return moves

class Queen:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color

        if self.color == 'white':
            self.icon = '♕'
        else:
            self.icon = '♛'

    def __str__(self):
        return self.icon

    def getMoves(self):
        moves = []
        capturePieces = []

        for i in range(1,8): # checks all spaces below the queen
            if self.pos[0] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0] + i, self.pos[1]) == "":
                    moves.append([self.pos[0] + i, self.pos[1]])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] + i, self.pos[1]))
                    break
            else:
                break

        for i in range(1, 8): # checks all spaces above the queen
            if self.pos[0] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] - i, self.pos[1]) == "":
                    moves.append([self.pos[0] - i, self.pos[1]])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] - i, self.pos[1]))
                    break
            else:
                break

        for i in range(1, 8): # checks all spaces to the right of the queen
            if self.pos[1] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0], self.pos[1] + i) == "":
                    moves.append([self.pos[0], self.pos[1] + i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0], self.pos[1] + i))
                    break
            else:
                break

        for i in range(1, 8): # checks all spaces to the left of the queen
            if self.pos[1] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0], self.pos[1] - i) == "":
                    moves.append([self.pos[0], self.pos[1] - i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0], self.pos[1] - i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces bottom right diagonal
            if self.pos[0] + i <= BOARD_MAX and self.pos[1] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0] + i, self.pos[1] + i) == "":
                    moves.append([self.pos[0] + i, self.pos[1] + i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] + i, self.pos[1] + i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces top right diagonal
            if self.pos[0] - i >= BOARD_MIN and self.pos[1] + i <= BOARD_MAX:
                if board.getPiece(self.pos[0] - i, self.pos[1] + i) == "":
                    moves.append([self.pos[0] - i, self.pos[1] + i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] - i, self.pos[1] + i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces bottom left diagonal
            if self.pos[0] + i <= BOARD_MAX and self.pos[1] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] + i, self.pos[1] - i) == "":
                    moves.append([self.pos[0] + i, self.pos[1] - i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] + i, self.pos[1] - i))
                    break
            else:
                break

        for i in range(1,8): # checks all spaces top left diagonal
            if self.pos[0] - i >= BOARD_MIN and self.pos[1] - i >= BOARD_MIN:
                if board.getPiece(self.pos[0] - i, self.pos[1] - i) == "":
                    moves.append([self.pos[0] - i, self.pos[1] - i])
                else:
                    capturePieces.append(board.getPiece(self.pos[0] - i, self.pos[1] - i))
                    break
            else:
                break

        # checks all capture pieces to see if they are the same color and removes them from the list
        for piece in capturePieces:
            if piece != "" and piece != "■":
                if piece.color != self.color:
                    moves.append(piece.pos)

        for i in range(len(moves) -1, -1, -1):
            # checks if the move is out of bounds
            if moves[i][0] > BOARD_MAX or moves[i][0] < BOARD_MIN or moves[i][1] > BOARD_MAX or moves[i][1] < BOARD_MIN:
                moves.remove(moves[i])

        return moves

class King:
    def __init__(self, color, pos, hasMoved=False):
        self.pos = pos
        self.color = color
        self.hasMoved = hasMoved

        if self.color == 'white':
            self.icon = '♔'
        else:
            self.icon = '♚'

    def __str__(self):
        return self.icon

    def getMoves(self):
        moves = [[self.pos[0] + 1, self.pos[1]], [self.pos[0] + 1, self.pos[1] + 1], [self.pos[0] + 1, self.pos[1] - 1], # up, up right, up left
                 [self.pos[0] - 1, self.pos[1]], [self.pos[0] - 1, self.pos[1] + 1], [self.pos[0] - 1, self.pos[1] - 1], # down, down right, down left
                 [self.pos[0], self.pos[1] + 1], [self.pos[0], self.pos[1] - 1]] # right, left

        for i in range(len(moves) -1, -1, -1):
            # checks if the move is out of bounds
            if moves[i][0] > BOARD_MAX or moves[i][0] < BOARD_MIN or moves[i][1] > BOARD_MAX or moves[i][1] < BOARD_MIN:
                moves.remove(moves[i])

        for i in range(1, 4): # checks the king side castle
            if self.pos[1] + i <= BOARD_MAX:
                selectedPiece = board.getPiece(self.pos[0], self.pos[1] + i)
                if selectedPiece != "" and selectedPiece != "■":
                    if isinstance(selectedPiece, Rook) and selectedPiece.color == self.color and selectedPiece.hasMoved == False and self.hasMoved == False:
                        moves.append([self.pos[0], self.pos[1] + 2])
                        break
                    else:
                        break

        for i in range(1,5): # checks the queen side castle
            if self.pos[1] - i >= BOARD_MIN:
                selectedPiece = board.getPiece(self.pos[0], self.pos[1] - i)
                if selectedPiece != "" and selectedPiece != "■":
                    if isinstance(selectedPiece, Rook) and selectedPiece.color == self.color and selectedPiece.hasMoved == False and self.hasMoved == False:
                        moves.append([self.pos[0], self.pos[1] - 2])
                        break
                    else:
                        break

        return moves

class Board:
    def __init__(self):

        self.board = []
        self.board.append([Rook('black', [0, 0]), Knight('black', [0, 1]), Bishop('black', [0, 2]), Queen('black', [0, 3]), King('black', [0, 4]), Bishop('black', [0, 5]), Knight('black', [0, 6]), Rook('black', [0, 7])])
        self.board.append([Pawn('black', [1, 0]), Pawn('black', [1, 1]), Pawn('black', [1, 2]), Pawn('black', [1, 3]), Pawn('black', [1, 4]), Pawn('black', [1, 5]), Pawn('black', [1, 6]), Pawn('black', [1, 7])])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append([Pawn('white', [6, 0]), Pawn('white', [6, 1]), Pawn('white', [6, 2]), Pawn('white', [6, 3]), Pawn('white', [6, 4]), Pawn('white', [6, 5]), Pawn('white', [6, 6]), Pawn('white', [6, 7])])
        self.board.append([Rook('white', [7, 0]), Knight('white', [7, 1]), Bishop('white', [7, 2]), Queen('white', [7, 3]), King('white', [7, 4]), Bishop('white', [7, 5]), Knight('white', [7, 6]), Rook('white', [7, 7])])
        '''

        # test board

        self.board = []
        self.board.append(["", "", "", "", King('black', [0, 4]), "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", Queen('black', [3,1]), "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", ""])
        self.board.append(["", Pawn('white', [6, 1]), "", "", "", "", "", ""])
        self.board.append([King('white', [7, 0]), "", "", "","", "", "", ""])
        '''
    def validateMoves(self, moves, piece):
        # loops through all the moves and sees if they are legal

        for i in range(len(moves) - 1, -1, -1):


            if self.isLegalMove(moves[i], piece) == False:
                moves.remove(moves[i])


        return moves

    def isLegalMove(self, move, piece):
        # simulates the move

        # gets old position and piece
        oldPos = piece.pos
        oldPiece = self.getPiece(move[0], move[1]) # either "" or a possible capture piece object

        # changes the position of the piece and the board
        piece.pos = move
        self.board[move[0]][move[1]] = piece
        self.board[oldPos[0]][oldPos[1]] = ""

        # sees if the king is in check
        isInCheck = self.kingInCheck(piece.color)

        # resets the board and the piece
        piece.pos = oldPos # resets the piece position
        self.board[move[0]][move[1]] = oldPiece # resets the new position of the piece to the old piece which is either "" or a piece
        self.board[oldPos[0]][oldPos[1]] = piece # resets the original piece in the move position to its original position

        # If the king is in check (True), then return False because its not a legal move
        # If the king is not in check (False), then return True because its a legal move
        return not isInCheck

    def kingInCheck(self, color):  
        #Find the king
        king = self.findKing(color)

        #Get all the pieces of the opposite color
        otherColor = 'white' if color == 'black' else 'black'
        pieces = self.getTeamPieces(otherColor)

        for piece in pieces:
            moves = piece.getMoves()
            for move in moves:
                if move == king.pos:
                    return True

        return False

    def kingInCheckMate(self, color):
        # Find own team pieces
        pieces = self.getTeamPieces(color)
        moves = []
        validMoves = []

        # Get all the moves of the pieces
        for piece in pieces:
            moves = piece.getMoves()            
            # Check if the move is a legal move
            for move in moves:
                tryMove = self.isLegalMove(move, piece) # checks if the move is legal (castling is not allowed to evade check)
                if tryMove is not False:
                    validMoves.append(tryMove) # adds the move to the list of valid moves

        if validMoves == [] and self.kingInCheck(color):
            return True # checkmate

        return False

    def checkStalemate(self, color):
        # if any peice doesnt have any valid moves and the king isnt in check its stalemate
        # if its impossible to checkmate with ur current pieces

        otherColor = 'white' if color == 'black' else 'black'
        teamPieces = self.getTeamPieces(color)
        otherTeamPieces = self.getTeamPieces(otherColor)

        tempMoves = []
        teamMoves = []
        otherTeamMoves = []

        for piece in teamPieces:
            tempMoves = piece.getMoves()
            teamMoves.append(self.validateMoves(tempMoves, piece))

        for piece in otherTeamPieces:
            tempMoves = piece.getMoves()
            otherTeamMoves.append(self.validateMoves(tempMoves, piece))

        if teamMoves == [] or otherTeamMoves == []:
            print('no moves stalemate')
            return True

        if len(teamPieces) <= 1 and len(otherTeamPieces) <= 1:
            print('only kings stalemate')
            return True

        if len(teamPieces) == 2:
            for piece in teamPieces:
                if isinstance(piece, Bishop):
                    print('cant checkamte bish')
                    return True
                if isinstance(piece, Knight):
                    print('cant checkamte knight')
                    return True

        if len(otherTeamPieces) == 2:
            for piece in otherTeamPieces:
                if isinstance(piece, Bishop):
                    print('cant checkamte bish')
                    return True
                if isinstance(piece, Knight):
                    print('cant checkamte knight')
                    return True

        return False

    def findKing(self, color):
        for row in self.board:
            for piece in row:
                if piece != "" and piece != "■" and piece.color == color and isinstance(piece, King):
                    king = piece
                    return king

    def getTeamPieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != "" and piece != "■" and piece.color == color:
                    pieces.append(piece)

        return pieces

    def printBoard(self):
        print("\n  a b c d e f g h")
        count = 8
        for row in self.board:
            print(count, end=" ")
            count -= 1
            for piece in row:
                if piece == "": # checks if its a piece or not
                    print(" ", end=" ")
                else:
                    print(piece, end=" ")
            print() # prints a new line

    def getPiece(self, row, col):
        return self.board[row][col]

    def highlight(self, move):
        if board.getPiece(move[0], move[1]) == "":
            self.board[move[0]][move[1]] = '■'

    def unHighlight(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '■':
                    self.board[row][col] = ""                



def convertNotation(letter, number):
    number = 8 - int(number)
    letter = ord(letter) - ord('a')
    if number > 7 or letter > 7:
        return False
    return [number, letter]

def convertNotationBack(move):
    letter = chr(move[1] + ord('a'))
    number = 8 - move[0]
    return [letter, number]

def printValidMoves(valid_moves):
    valid_moves = [convertNotationBack(move) for move in valid_moves]

    for move in valid_moves:
        print(move[0] + str(move[1]), end=" ")

def getInput(typeOfMove):
    possibleMoves = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                     'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                     'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                     'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                     'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                     'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                     'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    userInput = input(' ')
    if typeOfMove == 'getPiece':
        while userInput not in possibleMoves:
            print('\nSelect a piece' , end= '')
            userInput = input('')
            print('userinput: ', repr(userInput))
            userInput = userInput.lower()
            print(userInput in possibleMoves)
            
    else:
        while userInput not in possibleMoves:
            print('Select a move:' , end= '')
            userInput = input(' ')
            userInput = userInput.lower()

    return userInput
def movePiece():
    global color

    # save a copy of the board
    oldBoard = []
    for row in board.board:
        oldBoard.append(row.copy())

    board.printBoard()

    print('\nSelect a piece' , end= '')
    userMove = getInput('getPiece')
    userMove = userMove.lower()
    userMove = convertNotation(userMove[0], userMove[1])

    # gets the piece the user wants to move
    selectedPiece = board.getPiece(userMove[0], userMove[1])

    # checks if they are allowed to move that piece
    if selectedPiece == "" or selectedPiece == "■":
        print("No piece")
        movePiece()

    if selectedPiece.color != color:
        print("Not your piece")
        movePiece()

    moves = selectedPiece.getMoves()
    moves = board.validateMoves(moves, selectedPiece)
    enPassantPossible = False
    if isinstance(selectedPiece, Pawn):
            if selectedPiece.color == 'white':
                if selectedPiece.pos[0] == 3:
                    enPassant = selectedPiece.checkEnPassant(oldBoard)
                    if enPassant != False:
                        enPassantPossible = True
                        moves.append(enPassant)

            elif selectedPiece.color == 'black':
                if selectedPiece.pos[0] == 4:
                    enPassant = selectedPiece.checkEnPassant(oldBoard)
                    if enPassant != False:
                        enPassantPossible = True
                        moves.append(enPassant)

    # highlights the valid moves
    for move in moves:
        board.highlight(move)

    board.printBoard()
    board.unHighlight()
    print('selected piece: ', selectedPiece)
    printValidMoves(moves)

    if moves == []:
        print("No valid moves")
        movePiece()

    # gets the desired move from the user
    print("\nSelect a move: ")
    newUserMove = getInput('getMove')
    newUserMove = newUserMove.lower()
    newUserMove = convertNotation(newUserMove[0], newUserMove[1])

    if newUserMove in moves:
        if isinstance(selectedPiece, King): # checks if the move is a castling move
            if selectedPiece.color == 'white':
                if newUserMove == [7, 6]:
                    board.board[7][7] = ""
                    board.board[7][5] = Rook('white', [7, 5], True)
                elif newUserMove == [7, 2]:
                    board.board[7][0] = ""
                    board.board[7][3] = Rook('white', [7, 3], True)
            else:
                if newUserMove == [0, 6]:
                    board.board[0][7] = ""
                    board.board[0][5] = Rook('black', [0, 5], True)
                elif newUserMove == [0, 2]:
                    board.board[0][0] = ""
                    board.board[0][3] = Rook('black', [0, 3], True)

        if enPassantPossible == True:    
            if newUserMove == enPassant:
                if selectedPiece.color == 'white':
                    board.board[newUserMove[0] + 1][newUserMove[1]] = ""
                else:
                    board.board[newUserMove[0] - 1][newUserMove[1]] = ""

        board.board[newUserMove[0]][newUserMove[1]] = selectedPiece # moves the piece to new pos
        board.board[userMove[0]][userMove[1]] = "" # changes the old pos to empty
        selectedPiece.pos = newUserMove

        if isinstance(selectedPiece, Pawn): # checks if the move is a promition move
            if selectedPiece.color == 'white' and selectedPiece.pos[0] == 0:
                selectedPiece.promotePawn()
            elif selectedPiece.color == 'black' and selectedPiece.pos[0] == 7:
                selectedPiece.promotePawn()

        # set the has moved variable to true
        if isinstance(selectedPiece, (Pawn, Rook, King)):
            selectedPiece.hasMoved = True

        if board.checkStalemate(color):
            os.system('cls')
            print('stalemate')
            exit()


        # switches turn
        if color == 'white':
            color = 'black'
        else:
            color = 'white'

        otherColor = 'white' if color == 'black' else 'black'

        # checks if the king is in checkmate
        if board.kingInCheckMate(color):
            os.system('cls')
            print(f"Checkmate. {otherColor} wins!")
            exit()

    else:
        print("Invalid move")

    os.system('cls')
    movePiece()


def menu():

    print("Welcome to my Chess Game!")
    print("1. Play")
    print("2. Rules")
    print("3. Exit")


    choice = input("Enter your choice: ")
    if choice == '1':
        os.system('cls')
        movePiece()
        return
    elif choice == '2':
        os.system('cls')
        rules()
    elif choice == '3':
        exit()
    else:
        os.system('cls')
        print("Invalid choice")
        menu()

def rules():
    print('type done to go back')
    print("The game is played on an 8x8 board with 64 squares.")
    print("Each player has 16 pieces, including a king, queen, rooks, knights, bishops, and pawns.")
    print("The goal is to checkmate your opponent's king, making it unable to escape capture.")
    print("Each piece has a unique way of moving:")
    print("   - Kings move one square in any direction.")
    print("   - Queens move diagonally, horizontally, or vertically any number of squares.")
    print("   - Rooks move horizontally or vertically any number of squares.")
    print("   - Bishops move diagonally any number of squares.")
    print("   - Knights move in an L-shape.")
    print("   - Pawns move forward but capture diagonally.")
    print("Players take turns making one move at a time.")
    print("Captures are made by moving a piece onto an opponent's occupied square.")
    print("Special moves include castling, en passant captures, and pawn promotion.")
    print("The game ends when a player's king is checkmated or in a stalemate (no legal moves).")

    userInput = input(' ')
    if userInput.lower() == 'done':
        os.system('cls')
        menu()
    else:
        os.system('cls')
        print('Invalid Choice')
        rules()

# initliaze the board
board = Board()

# set the max and min of the board
BOARD_MAX = 7
BOARD_MIN = 0

color = 'white'
menu()


# add stalemate
# three fold repetition
# fifty move rule