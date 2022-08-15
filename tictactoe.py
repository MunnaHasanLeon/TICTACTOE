from ast import Pass
import pygame, sys
import numpy as np


pygame.init()
HEIGHT=400
WIDTH=HEIGHT


LINE_WIDTH=15


RED=(255, 0, 0)
BG_COLOR=(28,170,156)
LINE_COLOR=(23,145,135)
BOARD_ROWS =3
BOARD_COLS=3
SQUARES=HEIGHT//BOARD_COLS
CIRCLE_RADIUS=SQUARES//3
CIRCLE_WIDTH=15
CIRCLE_COLOR=(239, 231, 200 )
CROSS_WIDTH=25
SPACE=SQUARES//4
CROSS_COLOR=(66,66,66)




screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOR )

#board
board=np.zeros( (BOARD_ROWS, BOARD_COLS) )
print(board)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col*SQUARES+SQUARES//2), int(row*SQUARES+SQUARES//2)),CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col]==2:
                pygame.draw.line(screen, CROSS_COLOR, (col*SQUARES+SPACE, row*SQUARES+SQUARES-SPACE), (col*SQUARES+SQUARES-SPACE, row*SQUARES+SPACE),CROSS_WIDTH,)
                pygame.draw.line(screen, CROSS_COLOR, (col*SQUARES+SPACE, row*SQUARES+SPACE), (col*SQUARES+SQUARES-SPACE, row*SQUARES+SQUARES-SPACE),CROSS_WIDTH,)


def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_wining_line(col, player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row, player)
            return True
    #desc diagonal check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal_winning_line()
        return True
    #asc diagonal check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal_winning_line()
        return True

    return False


def draw_vertical_wining_line(col, player):
    posX= col*SQUARES+SQUARES//2
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), 15)
    

def draw_horizontal_winning_line(row, player):
    posY= row*SQUARES+SQUARES//2
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY),(WIDTH-15, posY),15)

def draw_asc_diagonal_winning_line():
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT-15),(WIDTH-15, 15),15)

def draw_desc_diagonal_winning_line():
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15),(WIDTH-15, HEIGHT-15),15) 



def mark_square(row, col, player):
    board[row][col]=player
def available_square(row, col):
    return board[row][col]==0
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==0:
                return False
    return True
                
            
                
             


def draw_lines():
    #1 horizontal 
    pygame.draw.line(screen, LINE_COLOR, (0,SQUARES), (HEIGHT, SQUARES), LINE_WIDTH)
    #2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,2*SQUARES), (HEIGHT, 2*SQUARES), LINE_WIDTH)
    #1 ver4tical
    pygame.draw.line(screen, LINE_COLOR, (SQUARES,0), (SQUARES, HEIGHT), LINE_WIDTH)
    # 2 vertical 
    pygame.draw.line(screen, LINE_COLOR, (2*SQUARES,0), (2*SQUARES, HEIGHT), LINE_WIDTH)

draw_lines()

player=1
gameOver= False

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0


#mainloop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX=event.pos[0]#x
            mouseY=event.pos[1]#y

            clicked_row= int(mouseY//(HEIGHT//3))
            clicked_col=int(mouseX//(HEIGHT//3))
            
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    gameOver=True
                player=player%2+1
                draw_figures()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                gameOver=False
                restart()   
            


    pygame.display.update()
