import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 4")

running = True

while running:
  # 4. 이벤트 처리
  for event in pygame.event.get():
    if event.type == pygame.QUIT:      # 창 닫기 버튼
      running = False
    if event.type == pygame.KEYDOWN:   # 키 눌림
      print("KEYDOWN:", event.key)
    if event.type == pygame.KEYUP:     # 키에서 손 뗌
      print("KEYUP:", event.key)
    if event.type == pygame.MOUSEBUTTONDOWN:   # 마우스 클릭
      print("Mouse Click:", event.pos)

  # (업데이트 로직이 들어갈 자리)

  # (그리기 로직)
  screen.fill((200, 200, 200))
  pygame.display.flip()

pygame.quit()