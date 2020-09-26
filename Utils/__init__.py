import pygame


def buttonPress(event, player):
    dx = 0
    dy = 0

    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_w:
    #         dy = -1
    #     elif event.key == pygame.K_a:
    #         dx = -1
    #     elif event.key == pygame.K_s:
    #         dy = 1
    #     elif event.key == pygame.K_d:
    #         dx = 1
    #     elif event.key == pygame.K_SPACE:
    #         player.attack()
    #     elif event.key == pygame.K_i:
    #         print('INVENTORY OPENED')

    # More stable than above
    if event.unicode.lower() == 'w':
        dy = -1
    elif event.unicode.lower() == 'a':
        dx = -1
    elif event.unicode.lower() == 's':
        dy = 1
    elif event.unicode.lower() == 'd':
        dx = 1
    elif event.unicode == ' ':
        player.attack()
    elif event.unicode.lower() == 'i':
        print('INVENTORY OPENED')

    return dx, dy