import pygame
import random
import os

base_dir = os.path.dirname(__file__)
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("커피알바 게임")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.img_path=os.path.join(base_dir,"bini.png")
    self.image=pygame.image.load(self.img_path)
    self.image=pygame.transform.scale(self.image,(40,40))
    self.rect=self.image.get_rect()
    self.rect.center=(WIDTH//2,HEIGHT//2)
    self.speed=3

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


# ------------------ 색 ------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FLOOR = (240, 230, 220)
BROWN = (139, 69, 19)
DARK_GRAY = (60, 60, 60)

# ✅ 메뉴 이름/종류 변경
MENU_ITEMS = ["Americano", "IcedTea", "Ade", "ChocoLatte"]
MENU_LETTER = {"Americano": "A", "IcedTea": "T", "Ade": "D", "ChocoLatte": "C"}

# ------------------ 이미지 로드(없으면 대체) ------------------
def load_image(path, size):
    try:
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, size)
        return img
    except:
        return None

player_img = load_image(os.path.join(base_dir, "bini.png"), (40, 40))
customer_img = load_image(os.path.join(base_dir, "customer.png"), (50, 50))  # 없으면 대체됨
cup_img = load_image(os.path.join(base_dir, "cup.png"), (28, 36))            # 없으면 대체됨

font = pygame.font.SysFont("malgungothic", 18)
font_big = pygame.font.SysFont("malgungothic", 30)

# ------------------ 카페 머신 위치 ------------------
MACHINE_RECT = pygame.Rect(WIDTH//2 - 45, HEIGHT//2 - 20, 90, 40)

# ------------------ Player ------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if player_img:
            self.image = player_img
        else:
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.rect(self.image, (80, 120, 200), (0, 0, 40, 40), border_radius=8)

        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2 + 120))
        self.speed = 4
        self.held_coffee = None  # "Americano" 등 or None

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())

# ------------------ Customer ------------------
class Customer(pygame.sprite.Sprite):
    def __init__(self, seat_pos, order):
        super().__init__()
        if customer_img:
            self.image = customer_img
        else:
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (205, 133, 63), (25, 25), 25)
            pygame.draw.circle(self.image, (80, 80, 80), (25, 25), 25, 2)

        self.rect = self.image.get_rect(center=seat_pos)
        self.order = order

        self.state = "waiting"  # waiting / leaving
        self.wait_frames = 0
        self.max_wait_frames = random.randint(60*6, 60*10)  # 6~10초(@60fps)
        self.left_happy = False
        self.timeout_penalized = False

    def update(self):
        if self.state == "waiting":
            self.wait_frames += 1
            if self.wait_frames >= self.max_wait_frames:
                self.state = "leaving"  # 타임아웃 -> 떠남

        elif self.state == "leaving":
            self.rect.x += 3

    def draw_bubble(self, surf):
        if self.state == "waiting":
            text_str = self.order
        else:
            text_str = "Thanks!" if self.left_happy else "ㅠㅠ"

        txt = font.render(text_str, True, BLACK)
        bubble = pygame.Rect(0, 0, txt.get_width()+10, txt.get_height()+6)
        bubble.midbottom = (self.rect.centerx, self.rect.top - 5)

        pygame.draw.rect(surf, WHITE, bubble, border_radius=6)
        pygame.draw.rect(surf, BLACK, bubble, 1, border_radius=6)
        surf.blit(txt, (bubble.x+5, bubble.y+3))

# ------------------ CoffeeCup ------------------
class CoffeeCup(pygame.sprite.Sprite):
    def __init__(self, x, y, coffee_type):
        super().__init__()
        self.coffee_type = coffee_type

        if cup_img:
            self.image = cup_img
        else:
            self.image = pygame.Surface((28, 36), pygame.SRCALPHA)
            pygame.draw.rect(self.image, (230, 230, 230), (0, 0, 28, 36), border_radius=6)
            pygame.draw.rect(self.image, BLACK, (0, 0, 28, 36), 2, border_radius=6)

        self.rect = self.image.get_rect(midbottom=(x, y))

    def draw_label(self, surf):
        letter = MENU_LETTER.get(self.coffee_type, "?")
        txt = font.render(letter, True, BLACK)
        surf.blit(txt, txt.get_rect(center=self.rect.center))

# ------------------ 스폰 함수 ------------------
SEATS = [(WIDTH//4, HEIGHT//2 + 10), (WIDTH//2, HEIGHT//2 + 10), (3*WIDTH//4, HEIGHT//2 + 10)]

def spawn_customer(customer_group, all_sprites):
    used = {c.rect.center for c in customer_group if c.state != "leaving"}
    available = [pos for pos in SEATS if pos not in used]
    if not available:
        return

    seat = random.choice(available)
    order = random.choice(MENU_ITEMS)
    c = Customer(seat, order)
    customer_group.add(c)
    all_sprites.add(c)

def spawn_cup(cup_group, all_sprites):
    if len(cup_group) >= 5:
        return
    base_x = MACHINE_RECT.centerx - 70
    gap = 35
    x = base_x + len(cup_group) * gap
    y = MACHINE_RECT.bottom + 35

    coffee_type = random.choice(MENU_ITEMS)
    cup = CoffeeCup(x, y, coffee_type)
    cup_group.add(cup)
    all_sprites.add(cup)

# ------------------ 게임 변수 ------------------
all_sprites = pygame.sprite.Group()
customer_group = pygame.sprite.Group()
cup_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

money = 0

# ✅ reputation(평판) -> lives(목숨)로 기능 변경
lives = 5

score = 0

game_over = False
running = True

# ✅ 전체 시간 제한 추가
TOTAL_TIME_SEC = 90
time_left_frames = TOTAL_TIME_SEC * 60  # 60fps 기준

# 프레임 타이머 (네 코드 스타일)
customer_spawn_timer = 0
CUSTOMER_SPAWN_INTERVAL = 180  # 3초
cup_spawn_timer = 0
CUP_SPAWN_INTERVAL = 240       # 4초

# ------------------ 상호작용 ------------------
def pick_cup():
    if player.held_coffee is not None:
        return

    hits = pygame.sprite.spritecollide(player, cup_group, dokill=True)
    if hits:
        player.held_coffee = hits[0].coffee_type

def serve():
    global money, lives, score

    # ✅ 커피 없으면 목숨 -1
    if player.held_coffee is None:
        lives -= 1
        return

    served = False
    near_zone = player.rect.inflate(120, 120)

    for c in list(customer_group):
        if c.state != "waiting":
            continue
        if near_zone.colliderect(c.rect):
            # ✅ 주문 맞으면 성공
            if c.order == player.held_coffee:
                score += 1
                money += 50
                c.state = "leaving"
                c.left_happy = True
                served = True
                break

    # ✅ 근처 손님 없거나 주문 틀리면 목숨 -1
    if not served:
        lives -= 1

    player.held_coffee = None

# ------------------ 메인 루프 ------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if not game_over:
                if event.key == pygame.K_SPACE:
                    if player.rect.colliderect(MACHINE_RECT.inflate(40, 40)):
                        pick_cup()
                if event.key == pygame.K_f:
                    serve()

            else:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    money = 0
                    lives = 5
                    score = 0
                    player.rect.center = (WIDTH//2, HEIGHT//2 + 120)
                    player.held_coffee = None

                    for s in list(customer_group): s.kill()
                    for s in list(cup_group): s.kill()

                    customer_spawn_timer = 0
                    cup_spawn_timer = 0

                    # ✅ 시간 리셋
                    time_left_frames = TOTAL_TIME_SEC * 60

    if not game_over:
        all_sprites.update()

        # ✅ 전체 시간 감소
        time_left_frames -= 1
        if time_left_frames <= 0:
            game_over = True

        # 손님 스폰
        customer_spawn_timer += 1
        if customer_spawn_timer >= CUSTOMER_SPAWN_INTERVAL:
            customer_spawn_timer = 0
            if len([c for c in customer_group if c.state != "leaving"]) < 3:
                spawn_customer(customer_group, all_sprites)

        # 컵 스폰
        cup_spawn_timer += 1
        if cup_spawn_timer >= CUP_SPAWN_INTERVAL:
            cup_spawn_timer = 0
            spawn_cup(cup_group, all_sprites)

        # ✅ 타임아웃 손님 -> 목숨 감소(1회) + 화면 밖 제거
        for c in list(customer_group):
            if c.state == "leaving" and not c.left_happy and not c.timeout_penalized:
                if c.wait_frames >= c.max_wait_frames:
                    lives -= 1
                    c.timeout_penalized = True

            if c.rect.left > WIDTH + 80:
                c.kill()

        # ✅ 목숨 0이면 게임오버
        if lives <= 0:
            game_over = True

    # ------------------ 그리기 ------------------
    screen.fill(FLOOR)

    # 카운터
    pygame.draw.rect(screen, BROWN, (0, HEIGHT//2 + 60, WIDTH, 30))

    # 머신
    pygame.draw.rect(screen, DARK_GRAY, MACHINE_RECT, border_radius=8)
    pygame.draw.rect(screen, BLACK, MACHINE_RECT, 2, border_radius=8)
    screen.blit(font.render("MACHINE", True, WHITE),
                font.render("MACHINE", True, WHITE).get_rect(center=MACHINE_RECT.center))

    # 스프라이트(플레이어/손님/컵)
    all_sprites.draw(screen)

    # 컵 라벨(A/T/D/C)
    for cup in cup_group:
        cup.draw_label(screen)

    # 손님 말풍선
    for c in customer_group:
        c.draw_bubble(screen)

    # ✅ 코인(목숨) UI 추가
    coin_y = 14
    coin_r = 9
    for i in range(5):
        cx = 12 + i * 24
        if i < lives:
            pygame.draw.circle(screen, (255, 205, 70), (cx, coin_y), coin_r)
            pygame.draw.circle(screen, (150, 110, 30), (cx, coin_y), coin_r, 2)
        else:
            pygame.draw.circle(screen, (210, 210, 210), (cx, coin_y), coin_r)
            pygame.draw.circle(screen, (120, 120, 120), (cx, coin_y), coin_r, 2)

    # UI
    held = player.held_coffee if player.held_coffee else "없음"
    time_sec = max(0, time_left_frames // 60)
    ui = font.render(f"돈:{money}  서빙:{score}  남은시간:{time_sec}s  들고있는음료:{held}", True, BLACK)
    screen.blit(ui, (10, 28))

    guide = font.render("SPACE: 머신에서 컵 줍기(근처) / F: 손님 서빙 / Enter: 재시작", True, BLACK)
    screen.blit(guide, (10, 50))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        t = font_big.render("GAME OVER (Press Enter)", True, WHITE)
        screen.blit(t, t.get_rect(center=(WIDTH//2, HEIGHT//2)))
        t2 = font.render(f"최종 돈:{money}  목숨:{lives}  서빙:{score}", True, WHITE)
        screen.blit(t2, t2.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
