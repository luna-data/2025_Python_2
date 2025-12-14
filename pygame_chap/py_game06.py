
import pygame
import os
base_dir=os.path.dirname(__file__)

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 6-이미지로 변경")

# 이동 테스트용 좌표
img_path=os.path.join(base_dir,"bini.png")
img=pygame.image.load(img_path)
img=pygame.transform.scale(img,(150,150))
rect=img.get_rect()
rect.center=(WIDTH//2,HEIGHT//2)

speed=1
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # 실시간 키 입력
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    rect.x -= speed
  if keys[pygame.K_RIGHT]:
    rect.x += speed
  if keys[pygame.K_UP]:
    rect.y -= speed
  if keys[pygame.K_DOWN]:
    rect.y += speed

  # 화면 경계 제한
  if rect.left < 0:
    rect.left = 0
  if rect.right > WIDTH:
    rect.right = WIDTH
  if rect.top < 0:
    rect.top = 0
  if rect.bottom > HEIGHT:
    rect.bottom = HEIGHT
  # 화면 그리기
  screen.fill((200, 200, 200))
  screen.blit(img,rect)

  pygame.display.flip()

pygame.quit()