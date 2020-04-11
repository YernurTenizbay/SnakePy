import pygame
import random


def main():
    pygame.init()
    clock = pygame.time.Clock()
    size=(720,460)
    screen=pygame.display.set_mode(size)
    #----------
    
    up = False
    down = True
    right = False
    left = False
    snakeh = [200,40]
    snake = [[200,40],[200,30],[200,20]]
    #--------
    foodx =200
    foody=200
    run=True
    while run:
        for f in pygame.event.get():
            if f.type == pygame.QUIT:
                run=False
            if f.type == pygame.KEYDOWN:
                if f.key == pygame.K_UP and down == False and not(snakeh[1]-10==snake[1][1]):
                    up = True
                    down = False
                    right = False
                    left = False
                elif f.key == pygame.K_DOWN and up == False and not(snakeh[1]+10==snake[1][1]):
                    down = True
                    up = False
                    right = False
                    left = False
                elif f.key == pygame.K_RIGHT and left == False and not(snakeh[0]+10==snake[1][0]):
                    right = True
                    up = False
                    down = False
                    left = False
                elif f.key == pygame.K_LEFT and right == False and not(snakeh[0]-10 == snake[1][0]):
                    left = True
                    up = False
                    down = False
                    right = False       
        screen.fill((255,255,255))
        i = 0
        if up: snakeh[1]-=10
        if down: snakeh[1]+=10
        if right: snakeh[0]+=10
        if left: snakeh[0]-=10
        for f in snake[1:]:
            #print(snakeh[0],f[0],snakeh[1],f[1])
            # print(snake)
            if f[0]==snakeh[0] and f[1]==snakeh[1]:
                run=False
        i = 0
        for f in snake:
            if i ==0:
                pygame.draw.rect(screen,(0,0,255),(f[0],f[1],10,10))
            else: pygame.draw.rect(screen,(0,255,0),(f[0],f[1],10,10))
            i+=1
        pygame.draw.rect(screen,(23,34,54),(foodx,foody,10,10))
        pygame.display.update()
        snake.insert(0,list(snakeh))
        if foodx == snakeh[0] and foody == snakeh[1]: 
            foodx = random.randrange(0, 72)*10
            foody = random.randrange(0,46)*10
        else: 
            snake.pop()
        if (snakeh[0]>=720 or snakeh[0]<=-10) or (snakeh[1]>=460 or snakeh[1]<=0): 
            run=False
        clock.tick(30)
main()

