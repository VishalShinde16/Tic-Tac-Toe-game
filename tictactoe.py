import pygame, sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=600
LINE_COLOR=(0, 179, 134)
BG=(102, 255, 176)
BOARD_ROWS=3
BOARD_COL=3
CIRCLE_RADIUS=60
CIRCLE_COLOR=(230, 255, 242)
CIRCLE_WIDTH=15
CROSS_WIDTH=15
CROSS_COLOR=(0, 51, 25)
SPACE=55
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG)

#BOard
board = np.zeros((BOARD_ROWS,BOARD_COL))

#print(board)
#pygame.draw.line(screen,RED,(10,10),(300,300),10)
def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),10)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),10)

    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),10)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),10)
    
draw_lines()

def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col] == 0:
                return False
                
    return True

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col]==1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*200+100),int(row*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen,CROSS_COLOR,(col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),CIRCLE_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)


def check_win(player):
    #for vertical
    for col in range(BOARD_COL):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True
    #for horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True
    #for asc
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    #for desc
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    #if no one win
    return False
        
def draw_vertical_winning_line(col,player):
    posX = col*200+100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)
    
def draw_horizontal_winning_line(row,player):
    posY = row*200+100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)




player = 1
game_over=False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:#not True =false so if game over it will not enter in if loop
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
        
            clicked_row = int(mouse_y//200)
            clicked_col = int(mouse_x//200)
        

            if available_square(clicked_row,clicked_col):
                if player==1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over=True
                    player = 2
                elif player==2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over=True
                    player = 1

                draw_figures()
        
        
    
    pygame.display.update()
