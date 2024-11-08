import pygame
from pygame_chess_api.api import Board, Pawn, Check, Piece
from pygame_chess_api.render import Gui

#Import the AI players
from chessAIQueen import chessAIQueen
from chessAI import chessAI

#assign ai to colors
white = chessAIQueen()
black = chessAI()
newWinner = False
blackWins = 0
whiteWins = 0
totalGames = 0
errorGames = 0
drawTracker = 0

#Alternate turns
def function_for_ai(board:Board):
    global white, black, drawTracker, errorGames, blackWins, whiteWins, totalGames, gui
    try:
        if board.cur_color_turn == 0:
            white.function_for_white()
        elif board.cur_color_turn == 1:
            black.function_for_black()
        m = board.move_history[-1]
        if type(m["piece"]) is Pawn:
            drawTracker = 0
        if m["move"].type == 2:
            print("capture")
            drawTracker = 0
        if drawTracker == 50:
            print("DRAW!!!!!!!!!!!")
            totalGames = totalGames + 1
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        else:
            drawTracker = drawTracker + 1
        if board.game_ended:
            print(f"AND THE WINNER IS {board.winner}")
            if board.winner == 1:
                blackWins = blackWins+1
            elif board.winner == 0:
                whiteWins = whiteWins+1
            totalGames = totalGames + 1
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    except:
        print("Uhh oh error")
        errorGames = errorGames + 1
        totalGames = totalGames + 1
        pygame.event.post(pygame.event.Event(pygame.QUIT))



'''The White color will be the human one and the Black color will be managed by the AI (by function_for_ai)'''
while totalGames < 10:
    pygame.init()
    board = Board()
    # while blackWins < 50 or whiteWins < 50 or totalGames < 500:
    white.setBoard(board)
    black.setBoard(board)
    gui = Gui(board, (Piece.WHITE,))
    gui.run_pygame_loop(function_for_ai)

print(f"BLACK WINS: {blackWins} WHITE WINS:{whiteWins} TOTAL GAMES: {totalGames}")
'''function_for_ai handles AI turns'''