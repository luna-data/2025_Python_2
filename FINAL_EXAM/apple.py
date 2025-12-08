import pygame
import os
import random

# =========================================
# 기본 초기화
# =========================================
base_dir = os.path.dirname(__file__)

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apple Game - 종합 버전")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("malgungothic", 20)  # 한글 폰트(윈도우 기준)

# 게임 모드 선택: "eat" -> 사과 먹기 / "avoid" -> 사과 피하기
GAME_MODE = "eat"   # "avoid" 로 바꾸면 라이프 깎이는 피하기 모드


# =========================================
# Player 클래스
# =========================================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_path = os.path.join(base_dir, "dukbird.png")
        self.image = pygame.image.load(self.img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 80)
        self.speed = 4

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

        # 화면 밖으로 나가지 않게
        self.rect.clamp_ip(screen.get_rect())


# =========================================
# Apple 클래스 (떨어지는 사과)
# =========================================
class Apple(pygame.sprite.Sprite):
    def __init__(self, speed=3):
        super().__init__()
        self.img_path = os.path.join(base_dir, "apple.png")
        self.image = pygame.image.load(self.img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.reset_position()

    def reset_position(self):
        # x는 화면 안 랜덤, y는 화면 위쪽 바깥
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += self.speed
        # 화면 아래로 사라지면 다시 위에서 떨어지도록
        if self.rect.top > HEIGHT:
            self.reset_position()


# =========================================
# Poop 클래스 (떨어지는 똥 - 점수 감소)
# =========================================
class Poop(pygame.sprite.Sprite):
    def __init__(self, speed=3):
        super().__init__()
        self.img_path = os.path.join(base_dir, "poop.png")  # 똥 이미지 파일
        self.image = pygame.image.load(self.img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset_position()


# =========================================
# 파일 I/O: 최고 점수 관리
# =========================================
HIGHSCORE_FILE = "highscore.txt"


def load_highscore():
    try:
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_highscore(score):
    try:
        with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
            f.write(str(score))
    except IOError:
        # 시험에서는 그냥 패스하거나, print 정도만 해도 됨
        print("highscore 저장 실패")


# =========================================
# 게임 초기 상태 설정
# =========================================
all_sprites = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
poop_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 처음에 생성할 사과 개수
initial_apple_count = 5
for _ in range(initial_apple_count):
    apple = Apple(speed=3)
    all_sprites.add(apple)
    apple_group.add(apple)

# 똥 객체 여러 개 생성
for _ in range(3):  # 개수 조절 가능
    poop = Poop(speed=3)
    all_sprites.add(poop)
    poop_group.add(poop)

score = 0
life = 3 if GAME_MODE == "avoid" else None  # 피하기 모드일 때만 라이프 사용
running = True
game_over = False

start_ticks = pygame.time.get_ticks()  # 시작 시간
highscore = load_highscore()
new_record = False


# 난이도 조절 관련
#  - 10초마다 속도 증가
#  - 10초마다 사과 1개씩 추가 (최대 15개)  ← (int(elapsed_sec // 10) 기준)
def update_difficulty():
    global apple_group, poop_group, all_sprites

    elapsed_ms = pygame.time.get_ticks() - start_ticks
    elapsed_sec = elapsed_ms / 1000

    # 10초마다 속도 1 증가
    speed_bonus = int(elapsed_sec // 10)  # 0, 1, 2, ...
    for apple in apple_group:
        apple.speed = 3 + speed_bonus
    for poop in poop_group:
        poop.speed = 3 + speed_bonus

    # 10초마다 사과 개수 늘리기 (최대 15개)
    target_count = min(initial_apple_count + int(elapsed_sec // 10), 15)
    while len(apple_group) < target_count:
        new_apple = Apple(speed=3 + speed_bonus)
        apple_group.add(new_apple)
        all_sprites.add(new_apple)


# =========================================
# 텍스트 렌더링 함수
# =========================================
def draw_text(surface, text, x, y, color=(0, 0, 0)):
    img = FONT.render(text, True, color)
    surface.blit(img, (x, y))


# =========================================
# 메인 루프
# =========================================
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()
        update_difficulty()

        # ===========================
        # 1) 사과 충돌 처리
        # ===========================
        apple_hits = pygame.sprite.spritecollide(player, apple_group, False)
        if apple_hits:
            if GAME_MODE == "eat":
                # 먹기 게임: 점수 올리고, 사과 위치 리셋
                for apple in apple_hits:
                    score += 1
                    apple.reset_position()
            elif GAME_MODE == "avoid":
                # 피하기 게임: 라이프 감소
                for apple in apple_hits:
                    apple.reset_position()
                if life is not None:
                    life -= 1
                    if life <= 0:
                        game_over = True
                        # 게임 끝나면 최고 점수 갱신(모드 상관없이 score 사용)
                        if score > highscore:
                            save_highscore(score)
                            new_record = True

        # ===========================
        # 2) 똥 충돌 처리 (점수 감소)
        # ===========================
        poop_hits = pygame.sprite.spritecollide(player, poop_group, False)
        if poop_hits:
            for p in poop_hits:
                score -= 1
                if score < 0:
                    score = 0  # 음수 방지 (선택)
                p.reset_position()

        # 피하기 모드가 아니어도, 일정 시간 뒤 게임 끝 처리하고 싶으면 여기서 조건 추가 가능
        # (예: 60초 버티기 등)

    else:
        # 게임 오버 상태에서 엔터 누르면 다시 시작
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            # 간단한 리셋(전체 초기화)
            score = 0
            life = 3 if GAME_MODE == "avoid" else None
            game_over = False
            new_record = False
            start_ticks = pygame.time.get_ticks()

            # 사과/똥 초기 위치 재배치
            for apple in apple_group:
                apple.reset_position()
            for poop in poop_group:
                poop.reset_position()

    # =========================================
    # 화면 그리기
    # =========================================
    screen.fill((170, 200, 255))  # 하늘색 배경

    # 바닥(잔디)
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    all_sprites.draw(screen)

    # 점수, 시간, 하이스코어 표시
    elapsed_ms = pygame.time.get_ticks() - start_ticks
    elapsed_sec = elapsed_ms / 1000

    draw_text(screen, f"Score: {score}", 10, 10)
    draw_text(screen, f"Time: {elapsed_sec:4.1f}s", 10, 35)
    draw_text(screen, f"HighScore: {highscore}", 10, 60)

    if GAME_MODE == "avoid" and life is not None:
        draw_text(screen, f"Life: {life}", 10, 85, (200, 0, 0))

    if game_over:
        draw_text(screen, "Game Over", WIDTH // 2 - 60, HEIGHT // 2 - 20, (200, 0, 0))
        if new_record:
            draw_text(screen, "New High Score!", WIDTH // 2 - 80, HEIGHT // 2 + 10, (0, 0, 200))
        draw_text(screen, "다시 시작: Enter 키", WIDTH // 2 - 90, HEIGHT // 2 + 40, (0, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
