import pygame
from pygame_chess_api.api import Bishop, Board, Check, Knight, Move, Pawn, Piece, Queen, Rook
from random import choice

class chessAI:
    
    def __init__(self):
        self.board = 0

    def setBoard(self, board):
        self.board = board
    def function_for_white(self):
        move = self.determineMove()
        print(f"{move.piece} moves to {move.piece.move(move)} and it's a ")  # executing this move

    def determineMove(self):
        selected_move = None
        allowed_moves = []
        for piece in self.board.pieces_by_color[self.board.cur_color_turn]:
            for move in piece.get_moves_allowed():
                if move.special_type == move.EN_PASSANT_TYPE:
                    print(f"setting move to en passant move {move}")
                    selected_move = move
                    return move
                elif move.type == move.OVER_CHECK_MOVE:
                    print(f"setting move to overcheck move {move}")
                    selected_move = move
                    return move
                elif move.type == move.KILL_MOVE:
                    print(f"adding kill move {move} to allowed moves")
                    selected_move = move
                    allowed_moves.append(move)
                elif move.special_type == move.TO_PROMOTE_TYPE:
                    move.piece.promote_class_wanted = Queen
                    print(f"adding promotion move {move} to allowed moves")
                    selected_move = move
                    allowed_moves.append(move)
        while not allowed_moves:  # loop until we find some allowed move
            random_piece = choice(self.board.pieces_by_color[self.board.cur_color_turn])  # getting a random piece
            allowed_moves = random_piece.get_moves_allowed()  # fetching allowed moves for this piece
        while not selected_move:
            selected_move = choice(allowed_moves)
            print(f"adding random move {selected_move} to move")
        bestMove = selected_move
        if self.board.cur_color_turn == 0:
            turn = 1
        elif self.board.cur_color_turn == 1:
            turn = 0
        # bestScore = self.board.score_evaluation()[turn]
        bestScore = 0
        for move in allowed_moves:
            if move.type == move.KILL_MOVE:
                targetPiece = self.board.pieces_by_pos[move.target]
                if targetPiece.SCORE_VALUE > bestScore:
                    bestScore = targetPiece.SCORE_VALUE
                    bestMove = move
                    print(f"{bestMove} is the best move right now, capturing {self.board.pieces_by_pos[move.target]}")
                # tempBoard = self.board.create_hypothesis_board()
                # tempPiece = tempBoard.pieces_by_pos[move.piece.pos]
                # tempPiece.move(move)
                # tempScore = tempBoard.score_evaluation()[turn]
                # if tempScore < bestScore:
                #     bestScore = tempScore
                #     bestMove = move
        if bestMove.special_type == bestMove.TO_PROMOTE_TYPE:
            bestMove.piece.promote_class_wanted = Queen
        return bestMove

    def function_for_black(self):
        move = self.determineMove()
        print(f"{move.piece} moves to {move.piece.move(move)}") #executing this move