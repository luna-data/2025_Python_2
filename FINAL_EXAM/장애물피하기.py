import pygame
import os
import random

base_dir = os.path.dirname(__file__)
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Obstacle Dodge")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# ---------------- Player ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_path = os.path.join(base_dir, "bini.png")
        try:
            image = pygame.image.load(self.img_path).convert_alpha()
            image = pygame.transform.scale(image, (60, 60))
        except:
            image = pygame.Surface((60, 60), pygame.SRCALPHA)
            image.fill((0, 0, 255))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 70)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

# ---------------- Obstacle ----------------
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, name, x, y, speed_x, color):
        super().__init__()
        self.name = name
        self.base_color = color
        self.image = pygame.Surface((50, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = speed_x

    def update(self):
        self.rect.x += self.speed_x
        # 벽에 닿으면 방향 반전 + 색 변경
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
            # 색 랜덤 변경
            new_color = (
                random.randint(50, 255),
                random.randint(50, 255),
                random.randint(50, 255),
            )
            self.image.fill(new_color)

# 그룹
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

colors = [(255, 80, 80), (80, 255, 80), (80, 80, 255)]
for i in range(3):
    obs = Obstacle(
        name=f"block{i+1}",
        x=random.randint(50, WIDTH - 100),
        y=100 + i * 60,
        speed_x=random.choice([-3, -2, 2, 3]),
        color=colors[i],
    )
    all_sprites.add(obs)
    obstacles.add(obs)

running = True
game_over = False
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        # 충돌하면 게임 오버
        if pygame.sprite.spritecollide(player, obstacles, False):
            game_over = True

    # ---------- 그리기 ----------
    screen.fill((240, 240, 240))
    all_sprites.draw(screen)

    # 장애물 이름 표시
    names = ", ".join([o.name for o in obstacles])
    name_text = font.render(f"Objects: {names}", True, (0, 0, 0))
    screen.blit(name_text, (10, 10))

    if game_over:
        over_text = font.render("충돌! Game Over (창을 닫아 종료)", True, (200, 0, 0))
        screen.blit(over_text, (WIDTH // 2 - 150, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
