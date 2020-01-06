import pygame as pg

#screen
HEIGHT = 800
WIDTH = 600
CENTER = (WIDTH // 2, HEIGHT // 2)
TITLE = "PONG"
#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#players
PLHEIGHT = 100
PLWIDTH = 15
PLOFFSET = 50
PSPEED = 2
#ball
BSIZE = 10
BSPEED = 1

def pong():

    pg.init()
    fps = pg.time.Clock()

    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)

    #start
    ball = {
        "x": HEIGHT // 2,
        "y": WIDTH // 2,
        "directionx": 1,
        "directiony": 1
    }
    player1 = pg.Rect(PLOFFSET, HEIGHT // 2 - PLHEIGHT // 2, PLWIDTH, PLHEIGHT)
    player2 = pg.Rect(WIDTH - PLOFFSET - PLWIDTH, HEIGHT // 2 - PLHEIGHT // 2, PLWIDTH, PLHEIGHT)
    scoreFont = pg.font.SysFont("arial", 50)
    score1 = 0
    score2 = 0

    running = True
    while(running):
        #players control
        keys = pg.key.get_pressed()
        if(keys[pg.K_w]):
            player1 = player1.move(0, -1 * PSPEED)
        if(keys[pg.K_s]):
            player1 = player1.move(0, 1 * PSPEED)
        if(keys[pg.K_UP]):
            player2 = player2.move(0, -1 * PSPEED)
        if(keys[pg.K_DOWN]):
            player2 = player2.move(0, 1 * PSPEED)

        #ball collisions   
        # walls
        if(ball['x'] + BSIZE // 2 >= HEIGHT):
            ball['directiony'] = -1
        if(ball['x'] - BSIZE // 2 <= 0):
            ball['directiony'] = 1
        if(ball['y'] - BSIZE // 2 <= 0):
            score2 += 1
            ball['x'] = CENTER[1]
            ball['y'] = CENTER[0]
            ball['directionx'] = 1
            ball['directiony'] = 1
        if(ball['y'] + BSIZE // 2 >= WIDTH):
            score1 += 1
            ball['x'] = CENTER[1]
            ball['y'] = CENTER[0]
            ball['directionx'] = -1
            ball['directiony'] = -1
        # players
        if(player1.collidepoint(ball['y'], ball['x'])):
            ball['directionx'] *= -1
        if(player2.collidepoint(ball['y'], ball['x'])):
            ball['directionx'] *= -1

        #move ball
        ball['y'] += BSPEED * ball['directionx']
        ball['x'] += BSPEED * ball['directiony']

        #score update
        scoreText1 = scoreFont.render(str(score1), True, WHITE)
        scoreText2 = scoreFont.render(str(score2), True, WHITE)
        scoreRect1 = scoreText1.get_rect()
        scoreRect2 = scoreText2.get_rect()
        scoreRect1.center = (25, 25)
        scoreRect2.center = (WIDTH - 25, 25)

        #display update
        screen.fill(BLACK)
        screen.blit(scoreText1, scoreRect1)
        screen.blit(scoreText2, scoreRect2)
        pg.draw.circle(screen, WHITE, (ball['y'], ball['x']), BSIZE)
        pg.draw.rect(screen, WHITE, player1)
        pg.draw.rect(screen, WHITE, player2)
        pg.display.update()

        #quit
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False

        fps.tick(144)

    pg.quit()

if __name__ == '__main__':
    pong()