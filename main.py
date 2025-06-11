import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('LOG')
sq = pygame.Surface((600,150))
sq.fill('white')
sq2 = pygame.Surface((600,150))
sq2.fill('white')
run = True
while run:
    screen.blit(sq,(1,1))
    screen.blit(sq2, (1, 440))

    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
            pygame.quit()






