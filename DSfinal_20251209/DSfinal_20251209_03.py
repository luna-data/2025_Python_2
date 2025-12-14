import pygame
import os
import random
base_dir=os.path.dirname(__file__)

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9")

clock=pygame.time.Clock()

# 이동 테스트용 좌표
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_path=os.path.join(base_dir,"dukbird.png")
        self.image=pygame.image.load(self.img_path)
        self.image=pygame.transform.scale(self.image,(150,150))
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH//2,HEIGHT//2)
        self.speed=3

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_path=os.path.join(base_dir,"apple.png")
        self.image=pygame.image.load(self.img_path)
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.reset()

    def spawn_apple(self):
        side = "top"
        size= 40
        if side == "top":
            self.x = random.randint(0, WIDTH - size)
            self.y = -size
            self.vx = random.randint(-2, 2)
            self.vy = random.randint(2, 4)  


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


all_sprites=pygame.sprite.Group()
bullets = pygame.sprite.Group()
apple_group = pygame.sprite.Group()

player=Player()
all_sprites.add(player)

apples = [] 
apple_spawn_timer = 0
running = True
game_over = False  
score=0

running=True
game_over=False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if game_over and event.key == pygame.K_RETURN:
        game_over = False         #추가: 다시 플레이 가능
        score = 0                 #추가: 점수 초기화

        #추가: 플레이어 위치 초기화
        player.rect.center = (WIDTH // 2, HEIGHT // 2)

        #추가: 사과들 초기화(모두 제거)
        apples.clear()
        apple_spawn_timer = 0

  if not game_over:
    all_sprites.update()  

    #추가: 일정 주기마다 새로운 사과 생성 (사방팔방에서 계속 나옴)
    apple_spawn_timer += 1
    if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
      apple_spawn_timer = 0
      spawn_apple()

    #추가: 각 사과 이동 & 충돌 처리
    new_apples = []
    for apple in apples:
      rect = apple["rect"]
      vx = apple["vx"]
      vy = apple["vy"]

      rect.x += vx
      rect.y += vy

      #화면을 완전히 벗어난 사과는 버림
      if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
        continue

      #변경: 플레이어와 사과 충돌 처리
      if player.rect.colliderect(rect):
        score += 1
        print("사과 먹음!")
        # 먹힌 사과는 리스트에 다시 넣지 않음 (즉, 사라짐)
        continue

      new_apples.append(apple)

    apples = new_apples

    # 똥 충돌 (원래 코드와 같은 역할)
    hits = pygame.sprite.spritecollide(player, enemy_group, False)
    if hits:
      print("똥에 닿음! 게임 오버")
      game_over = True