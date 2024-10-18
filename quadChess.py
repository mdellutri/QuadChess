import pygame
from pygame_chess_api.api import Board, Pawn, Check
from pygame_chess_api.render import Gui

#Import the AI players
from chessAIQueen import chessAIQueen
from chessAI import chessAI

#assign ai to colors
white = chessAIQueen()
black = chessAI()

drawTracker = 0

#Alternate turns
def function_for_ai(board:Board):
    global white, black, drawTracker
    if board.cur_color_turn == 0:
        white.function_for_white()
    elif board.cur_color_turn == 1:
        black.function_for_black()
    m = board.move_history[-1]
    print(m["piece"])
    if type(m["piece"]) is Pawn:
        drawTracker = 0
    if board.cur_color_turn_in_check:
        drawTracker = 0
    if drawTracker == 50:
        print("DRAW!!!!!!!!!!!")
        pygame.quit()
    else:
        drawTracker = drawTracker + 1

pygame.init()

board = Board()
white.setBoard(board)
black.setBoard(board)
gui = Gui(board, ())
'''The White color will be the human one and the Black color will be managed by the AI (by function_for_ai)'''
gui.run_pygame_loop(function_for_ai)
'''function_for_ai handles AI turns'''