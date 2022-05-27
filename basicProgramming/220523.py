# def main() :
#     l = [
#         [1, 2, 3],
#         [0, 2, "-"],
#         [0, 1, 3],
#         [0, 2, "-"]
#     ]

#     for i in range(4) :
#         for j in range(3) :
#             print(l[i][j])




# import pygame

# pygame.init()
# pygame.display.set_mode((600, 600))

# while True :
#     for event in pygame.event.get() :
#         if event.type == QUIT :
#             pygame.quit()

#     pygame.display.update()




# import pygame
# from pygame.locals import QUIT

# pygame.init()
# display_surface = pygame.display.set_mode((600, 600))
# pygame.display.set_caption("Window Test")

# BLUE = (0, 0, 255)

# def main():
#     running = True
#     while running:
#         display_surface.fill(BLUE)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()

#     pygame.display.update()

# if __name__ == '__main__':
#     main()




import pygame
from pygame.locals import QUIT

pygame.init()
display_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Window Test")

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)


def main():
    running = True
    while running:
        display_surface.fill(BLUE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    pygame.display.update()


if __name__ == '__main__':
    main()