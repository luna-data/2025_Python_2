import pygame
import os
import random

#플레이어는 한명, 사과는 위에서 떨어짐. 먹기모드와 피하기 모드가 있음, 목숨이 0이 되면 끝
# ============================================
# 0. 기본 설정
# ============================================

# 현재 파일이 있는 폴더 경로 (이미지 파일 불러올 때 사용)
base_dir = os.path.dirname(__file__)

# pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apple Game - Life & Restart")

# FPS 설정용 Clock
clock = pygame.time.Clock()

# 글꼴 설정 (없으면 기본 글꼴 사용)
font = pygame.font.SysFont(None, 28)


# ============================================
# 1. Player 클래스 (플레이어 캐릭터)
# ============================================

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 플레이어 이미지 불러오기
        img_path = os.path.join(base_dir, "bini.png")  # 자신의 이미지 이름으로 수정 가능

        try:
            image = pygame.image.load(img_path).convert_alpha()
            image = pygame.transform.scale(image, (80, 80))  # 크기 조절
        except:
            # 이미지가 없을 경우 대비: 파란색 네모로 대체
            image = pygame.Surface((80, 80))
            image.fill((0, 0, 255))

        self.image = image
        # 충돌 및 위치를 관리하는 rect 정보
        self.rect = self.image.get_rect()
        # 초기 위치: 화면 아래쪽 중앙
        self.rect.center = (WIDTH // 2, HEIGHT - 80)

        # 이동 속도
        self.speed = 5

    def update(self):
        """키보드 입력에 따라 플레이어 위치 업데이트"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 화면 범위를 벗어나지 않도록 제한
        self.rect.clamp_ip(screen.get_rect())


# ============================================
# 2. Apple 클래스 (위에서 아래로 떨어지는 사과)
# ============================================

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 여기서는 단순히 빨간 원으로 사과를 표현
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (12, 12), 12)
        self.rect = self.image.get_rect()

        # 처음 생성할 때 랜덤 위치로 설정
        self.reset()

    def reset(self):
        """사과 위치를 화면 위쪽 랜덤 위치로 리셋"""
        # x: 화면 안에서 랜덤
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        # y: 화면 위쪽 바깥(-200 ~ -30 사이)에서 등장하도록
        self.rect.y = random.randint(-200, -30)
        # 떨어지는 속도 랜덤 (2~5)
        self.speed_y = random.randint(2, 5)

    def update(self):
        """아래로 떨어지게 하는 로직"""
        self.rect.y += self.speed_y

        # 화면 바닥(HEIGHT) 보다 더 내려가면 다시 위로 리셋
        if self.rect.top > HEIGHT:
            self.reset()


# ============================================
# 3. 스프라이트 그룹 생성
# ============================================

# 모든 스프라이트(플레이어, 사과들)를 담는 그룹
all_sprites = pygame.sprite.Group()

# 사과들만 따로 관리하는 그룹 (충돌 체크용)
apple_group = pygame.sprite.Group()

# 플레이어 생성 및 그룹에 추가
player = Player()
all_sprites.add(player)

# 사과 여러 개 생성
for _ in range(7):  # 사과 개수 (원하면 늘려도 됨)
    apple = Apple()
    all_sprites.add(apple)
    apple_group.add(apple)


# ============================================
# 4. 게임 상태 변수들
# ============================================

score = 0          # 점수
life = 3           # 플레이어 목숨
game_over = False  # 게임 오버 상태 여부

# 게임 모드:
#   True  → 먹기 모드 (GET): 사과 먹으면 점수 +1
#   False → 피하기 모드 (DODGE): 사과에 맞으면 목숨 -1
mode_get = True

running = True     # 메인 루프 실행 여부


# ============================================
# 5. 텍스트 출력 함수
# ============================================

def draw_text(surface, text, x, y, color=(0, 0, 0)):
    """화면에 텍스트를 그리는 작은 헬퍼 함수"""
    img = font.render(text, True, color)
    surface.blit(img, (x, y))


# ============================================
# 6. 게임 재시작을 위한 함수
# ============================================

def reset_game():
    """게임을 처음 상태로 재설정 (점수, 목숨, 사과 위치 등)"""
    global score, life, game_over

    score = 0
    life = 3
    game_over = False

    # 플레이어 위치 초기화
    player.rect.center = (WIDTH // 2, HEIGHT - 80)

    # 모든 사과를 다시 위로 리셋
    for apple in apple_group:
        apple.reset()


# ============================================
# 7. 메인 게임 루프
# ============================================

while running:
    clock.tick(60)  # FPS 60으로 고정

    # -----------------------------
    # (1) 이벤트 처리
    # -----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 모드 전환은 게임 오버가 아닐 때만 가능하게
        if not game_over and event.type == pygame.KEYDOWN:
            # SPACE: 먹기 모드 / 피하기 모드 전환
            if event.key == pygame.K_SPACE:
                mode_get = not mode_get

        # 게임 오버 상태에서 Enter 키를 누르면 재시작
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset_game()

    # -----------------------------
    # (2) 게임 로직 업데이트
    # -----------------------------
    if not game_over:
        # 플레이어와 사과들의 위치 업데이트
        all_sprites.update()

        # 플레이어와 사과의 충돌 체크
        #   dokill=False → 충돌해도 사과 객체는 죽지 않음(그냥 위치만 리셋)
        hit_list = pygame.sprite.spritecollide(player, apple_group, False)

        if hit_list:
            # [모드 1] 먹기 모드: 사과 먹으면 점수 +1
            if mode_get:
                for apple in hit_list:
                    score += 1
                    apple.reset()
            else:
                # [모드 2] 피하기 모드: 사과에 맞으면 목숨 -1
                # 여러 개 동시에 맞을 수도 있으니, 맞은 개수만큼 감소 가능 (여기서는 1번에 1만 줄이는 것도 가능)
                life -= 1
                # 맞은 사과들은 다시 위로 리셋
                for apple in hit_list:
                    apple.reset()

                # 목숨이 0 이하가 되면 게임 오버 처리
                if life <= 0:
                    game_over = True

    # -----------------------------
    # (3) 화면 그리기
    # -----------------------------
    screen.fill((170, 200, 255))   # 하늘색 배경

    # 바닥 잔디
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 40, WIDTH, 40))

    # 스프라이트(플레이어 + 사과들) 그리기
    all_sprites.draw(screen)

    # 점수 / 목숨 / 모드 표시
    draw_text(screen, f"Score: {score}", 10, 10)
    draw_text(screen, f"Life: {life}", 10, 35, (200, 0, 0))

    mode_text = "Mode: GET (SPACE로 DODGE 전환)" if mode_get else "Mode: DODGE (SPACE로 GET 전환)"
    draw_text(screen, mode_text, 10, 60)

    # 게임 오버 메시지
    if game_over:
        # 반투명한 검은 배경을 화면 중앙에 깔아줄 수도 있음(선택)
        # 여기서는 단순 텍스트만 표시
        draw_text(screen, "GAME OVER", WIDTH//2 - 70, HEIGHT//2 - 20, (255, 0, 0))
        draw_text(screen, "다시 시작: Enter 키", WIDTH//2 - 90, HEIGHT//2 + 10, (0, 0, 0))

    # 실제 화면에 반영
    pygame.display.flip()

# 루프 종료 후 pygame 종료
pygame.quit()
