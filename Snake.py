import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((500, 500))  # screen size
screen.fill(THECOLORS['black'])  # screen color

r = pygame.Rect(250, 250, 10, 10)  # size of rect
pygame.draw.rect(screen, 'yellow', r, 0)  # draw.rect(screen, color, Rect, width)
pygame.draw.line(screen, (255, 250, 250), [50, 100], [170, 100], 4)  # draw.rect(screen, color, Rect, width)
font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('HELLO'), True, THECOLORS['green'])

# screen.blit(text, (50, 50))

for i in range(50, 100):
    screen.blit(text, (i, 50))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()