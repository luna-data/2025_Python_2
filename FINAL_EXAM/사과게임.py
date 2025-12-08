import pygame
import os
import random

base_dir = os.path.dirname(__file__)
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apple Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# ---------------- Player ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_path = os.path.join(base_dir, "bini.png")
        try:
            image = pygame.image.load(self.img_path).convert_alpha()
            image = pygame.transform.scale(image, (80, 80))
        except:
            image = pygame.Surface((80, 80), pygame.SRCALPHA)
            image.fill((0, 0, 255))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 80)
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

# ---------------- Apple ----------------
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (12, 12), 12)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -30)
        self.speed_y = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.reset()

# 그룹들
all_sprites = pygame.sprite.Group()
apple_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 사과 여러 개 생성
for _ in range(7):
    apple = Apple()
    all_sprites.add(apple)
    apple_group.add(apple)

score = 0
mode_get = True   # True면 먹는 게임, False면 피하는 게임
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 스페이스로 모드 전환(먹기/피하기)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            mode_get = not mode_get

    all_sprites.update()

    # 충돌 체크
    hit_list = pygame.sprite.spritecollide(player, apple_group, False)
    if hit_list:
        if mode_get:
            # 먹는 게임: 점수 +1, 사과 리스폰
            for a in hit_list:
                score += 1
                a.reset()
        else:
            # 피하는 게임: 점수 -1 (또는 라이프 감소)
            for a in hit_list:
                score -= 1
                a.reset()

    # ------------ 그리기 ------------
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 40, WIDTH, 40))

    all_sprites.draw(screen)

    text1 = font.render(f"Score: {score}", True, (0, 0, 0))
    text2 = font.render(
        "Mode: GET" if mode_get else "Mode: DODGE (SPACE로 전환)",
        True, (0, 0, 0)
    )
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 35))

    pygame.display.flip()

pygame.quit()
