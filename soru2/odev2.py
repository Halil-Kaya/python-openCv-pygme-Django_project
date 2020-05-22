import pygame, time, sys

pygame.init()
pencere = pygame.display.set_mode((800, 600))
arka_plan = pygame.image.load("resim.jpeg")
kutu = pygame.Rect((50, 50), (100, 100))
pygame.key.set_repeat(10, 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if kutu.left < 0:
                    kutu.left = 800
                else:
                    kutu.left -= 10
            if event.key == pygame.K_RIGHT:
                if kutu.right > 800:
                    kutu.right = 0
                else:
                    kutu.right += 10
            if event.key == pygame.K_UP:
                if kutu.top < 0:
                    kutu.top = 600
                else:
                    kutu.top -= 10
            if event.key == pygame.K_DOWN:
                if kutu.bottom > 600:
                    kutu.bottom = 0
                else:
                    kutu.bottom += 10

    pencere.blit(arka_plan, (0,0))
    pygame.draw.rect(pencere, (139, 180, 120), kutu)
    pygame.display.update()
    time.sleep(0.025)
