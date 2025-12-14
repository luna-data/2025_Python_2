import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 3")

running = True

while running: # 아직 이벤트는 자세히 다루지 않고, QUIT만 처리
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # (나중에: 업데이트 로직 들어갈 자리)
  # (나중에: 그리기 로직 들어갈 자리)

  screen.fill((200, 200, 200))
  pygame.display.flip()

pygame.quit()