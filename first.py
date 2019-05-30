
import pygame
pygame.init()


pygame.display.set_caption("SRP AlphaTest")

display_width = 500
display_height = 500
x = 50
y = 425
width = 40
height = 60
vel = 20
isJump = False
jumpCount = 10

window = pygame.display.set_mode((display_width, display_height))

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x+= vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y+= vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 50), (x, y, width, height))
    pygame.display.update()

pygame.quit()


