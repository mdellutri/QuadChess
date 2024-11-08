from pygame_chess_api.api import Bishop, Board, Check, Knight, Move, Pawn, Piece, Queen, Rook
from random import choice

class chessAIQueen:
    
    def __init__(self):
        self.board = 0;

    def setBoard(self, board):
        self.board = board
    def function_for_white(self):
        #finding the best move to do... Here we will execute a random move for a random piece as an example
            allowed_moves = None
            while not allowed_moves: #loop until we find some allowed move
                random_piece = choice(self.board.pieces_by_color[self.board.cur_color_turn]) #getting a random piece
                allowed_moves = random_piece.get_moves_allowed() #fetching allowed moves for this piece

            random_move = choice(random_piece.get_moves_allowed()) #getting one random move from the allowed moves

            if random_move.special_type == random_move.TO_PROMOTE_TYPE:
                '''if we have to specify a pawn promotion we promote it to a Bishop'''
                random_piece.promote_class_wanted = Queen

            print(f"{random_piece} moves to {random_piece.move(random_move)}") #executing this move
    
    def function_for_black(self):
        #finding the best move to do... Here we will execute a random move for a random piece as an example
            allowed_moves = None
            while not allowed_moves: #loop until we find some allowed move
                random_piece = choice(self.board.pieces_by_color[self.board.cur_color_turn]) #getting a random piece
                allowed_moves = random_piece.get_moves_allowed() #fetching allowed moves for this piece

            random_move = choice(random_piece.get_moves_allowed()) #getting one random move from the allowed moves

            if random_move.special_type == random_move.TO_PROMOTE_TYPE:
                '''if we have to specify a pawn promotion we promote it to a Queen'''
                random_piece.promote_class_wanted = Queen

            random_piece.move(random_move) #executing this move