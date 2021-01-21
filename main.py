import pygame

DARK_BLUE = (0, 0, 50)
LIGHT_BLUE = (150, 188, 235)
GREEN = (50, 255, 50)
WHITE = (255, 255, 255)
PLANE_WIDTH, PLANE_HEIGHT = 800, 450
# main
if __name__ == '__main__':
    delta = pygame.Rect(-200, 400, PLANE_WIDTH, PLANE_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("plane")
    # blocks
    delta_737_image = pygame.image.load(
        'b738_icon11.png'
    )

    kill = pygame.image.load(
        'kill brick.png'
    )
    game_icon = pygame.image.load('b738_icon11.png')
    pygame.display.set_icon(game_icon)
    BORDER = pygame.Rect(500, 0, 0, 600)
    # main:2
    FPS = 40
    VEL = 2
    done = False
    direct = 0
    frame = 0
    while not done:
        frame += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Keys
        Keys_pressed = pygame.key.get_pressed()
        if Keys_pressed[pygame.K_LEFT]:
            delta.x -= VEL
            if direct == 0:
                direct = 1
                delta_737_image = pygame.transform.flip(delta_737_image, True, False)
        if Keys_pressed[pygame.K_UP]:
            delta.y -= VEL
        if Keys_pressed[pygame.K_RIGHT]:
            delta.x += VEL
            if direct == 1:
                direct = 0
                delta_737_image = pygame.transform.flip(delta_737_image, True, False)
        if Keys_pressed[pygame.K_DOWN]:
            delta.y += VEL
        if delta_737_image:
            # color
            screen.fill(DARK_BLUE)
        screen.fill(GREEN, (0, 600, 1024, 168))
        screen.blit(delta_737_image, (delta.x, delta.y))
        screen.blit(kill, (500, 600))
        # DO NOT DELETE

        pygame.display.update()
