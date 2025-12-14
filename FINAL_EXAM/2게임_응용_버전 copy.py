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

# ====================================
# Player 클래스 (베이스 코드 그대로)
# ====================================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # 스프라이트 이미지 불러오기
        self.img_path = os.path.join(base_dir, "dukbird.png")
        try:
            image = pygame.image.load(self.img_path).convert_alpha()
            image = pygame.transform.scale(image, (80, 80))
        except:
            # 이미지가 없을 경우 예외 처리
            image = pygame.Surface((80, 80))
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

        # 화면 밖 제한
        self.rect.clamp_ip(screen.get_rect())


# ====================================
# Apple 클래스 (새로 추가된 핵심)
# ====================================
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 사과는 동그라미로 그림
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (12, 12), 12)

        self.rect = self.image.get_rect()
        self.reset()  # 랜덤 초기값 설정

    def reset(self):
        # x는 무작위 / y는 화면 위쪽 바깥
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -30)
        self.speed_y = random.randint(2, 5)  # 떨어지는 속도

    def update(self):
        self.rect.y += self.speed_y
        
        # 화면 아래로 사라지면 다시 위에서 떨어짐
        if self.rect.top > HEIGHT:
            self.reset()


# ====================================
# 스프라이트 그룹 생성
# ====================================
all_sprites = pygame.sprite.Group()
apple_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 사과 여러 개 생성 (베이스 코드에는 없던 부분)
for _ in range(7):
    apple = Apple()
    all_sprites.add(apple)
    apple_group.add(apple)


# ====================================
# 게임 상태 변수
# ====================================
score = 0
mode_get = True   # True = 먹기 모드, False = 피하기 모드
running = True


# ====================================
# 메인 루프
# ====================================
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # SPACE 키 → 모드 전환
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            mode_get = not mode_get

    # 모든 스프라이트 업데이트
    all_sprites.update()

    # 플레이어와 사과 충돌 검사
    hit_list = pygame.sprite.spritecollide(player, apple_group, False)

    if hit_list:
        if mode_get:
            # 먹기: 점수 증가 + 사과 리셋
            for a in hit_list:
                score += 1
                a.reset()
        else:
            # 피하기: 점수 감소 + 사과 리셋
            for a in hit_list:
                score -= 1
                a.reset()

    # ====================================
    # 화면 그리기
    # ====================================
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 40, WIDTH, 40))

    all_sprites.draw(screen)

    # 점수 & 모드 텍스트 표시
    text1 = font.render(f"Score: {score}", True, (0, 0, 0))
    text2 = font.render(
        "Mode: GET" if mode_get else "Mode: DODGE (SPACE로 전환)",
        True, (0, 0, 0)
    )

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 35))

    pygame.display.flip()

pygame.quit()
