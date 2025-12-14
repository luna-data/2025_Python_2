import pygame

pygame.init()

# 화면(디스플레이) 생성
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 2")

# 화면을 하얗게 칠함
screen.fill((255, 255, 255))
pygame.display.flip()

# 2초 기다렸다가 종료
pygame.time.delay(2000)

pygame.quit()