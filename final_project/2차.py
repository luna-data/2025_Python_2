import pygame
import sys
import random

# ============================================
# 기본 설정
# ============================================
WIDTH, HEIGHT = 800, 600
FPS = 60

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (205, 133, 63)
DARK_GRAY = (60, 60, 60)
FLOOR = (240, 230, 220)

MENU_ITEMS = ["Americano", "Latte", "Mocha"]


# ============================================
# 손님 클래스 (움직임 + 상태 + 말풍선)
# ============================================
class Customer:
    def __init__(self, seat_x, seat_y, order, max_wait=10.0, from_side="left"):
        # 최종 자리
        self.seat_x = seat_x
        self.seat_y = seat_y
        self.order = order

        # 입장 방향에 따른 초기 위치
        self.speed = 120  # 이동 속도
        if from_side == "left":
            self.x = -60
        else:
            self.x = WIDTH + 60
        self.y = seat_y

        # 상태: entering → waiting → leaving
        self.state = "entering"

        # 대기 관련
        self.max_wait = max_wait
        self.wait_time = 0.0
        self.timed_out = False
        self.timeout_penalized = False

        # 행복하게 나갔는지 여부
        self.left_happy = False

    def update(self, dt):
        if self.state == "entering":
            # 좌석까지 걸어오기
            if abs(self.x - self.seat_x) > 2:
                direction = 1 if self.seat_x > self.x else -1
                self.x += direction * self.speed * dt
            else:
                self.x = self.seat_x
                self.state = "waiting"
                self.wait_time = 0.0

        elif self.state == "waiting":
            # 자리에서 기다리는 중
            self.wait_time += dt
            if self.wait_time >= self.max_wait:
                self.state = "leaving"
                self.timed_out = True

        elif self.state == "leaving":
            # 오른쪽으로 퇴장
            self.x += self.speed * dt

    def get_rect(self):
        size = 70
        return pygame.Rect(self.x - size // 2, self.y - size // 2, size, size)

    def draw(self, screen, font_small):
        # 기다리는 동안 테두리 색 변화
        if self.state == "waiting":
            ratio = min(self.wait_time / self.max_wait, 1.0)
            border_color = (
                int(50 + 170 * ratio),     # R
                int(200 - 150 * ratio),    # G
                int(80 * (1 - ratio)),     # B
            )
        else:
            border_color = (80, 80, 80)

        # 얼굴
        pygame.draw.circle(screen, LIGHT_BROWN, (int(self.x), int(self.y)), 35)
        pygame.draw.circle(screen, border_color, (int(self.x), int(self.y)), 35, 3)

        # 말풍선 텍스트
        if self.state == "entering":
            text_str = "..."
        elif self.state == "waiting":
            text_str = self.order
        elif self.state == "leaving":
            text_str = "Thanks!" if self.left_happy else "ㅠㅠ"

        text = font_small.render(text_str, True, BLACK)
        text_rect = text.get_rect(center=(int(self.x), int(self.y - 55)))

        bubble_rect = pygame.Rect(
            text_rect.x - 4,
            text_rect.y - 2,
            text_rect.width + 8,
            text_rect.height + 4,
        )

        pygame.draw.rect(screen, WHITE, bubble_rect, border_radius=6)
        pygame.draw.rect(screen, BLACK, bubble_rect, 1, border_radius=6)
        screen.blit(text, text_rect)


# ============================================
# 플레이어(캐릭터) 클래스
# ============================================
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.speed = 250  # 픽셀/초

        # 들고 있는 커피 (문자열 or None)
        self.held_coffee = None

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x - self.width // 2),
            int(self.y - self.height),
            self.width,
            self.height
        )

    def update(self, dt, keys):
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1

        # 대각선 보정
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071

        self.x += dx * self.speed * dt
        self.y += dy * self.speed * dt

        # 화면 안으로만 이동
        min_y = HEIGHT // 2 + 40
        max_y = HEIGHT - 20
        self.x = max(self.width // 2, min(WIDTH - self.width // 2, self.x))
        self.y = max(min_y, min(max_y, self.y))

    def is_near(self, customer, max_dist=120):
        dx = self.x - customer.x
        dy = (self.y - self.height // 2) - customer.y
        return dx * dx + dy * dy <= max_dist * max_dist

    def draw(self, screen):
        # 몸통
        pygame.draw.rect(screen, (80, 120, 200), self.rect, border_radius=8)
        # 머리
        head_center = (self.rect.centerx, self.rect.top - 15)
        pygame.draw.circle(screen, (255, 224, 189), head_center, 15)


# ============================================
# 커피 컵 클래스 (머신에서 생성되는 컵)
# ============================================
class CoffeeCup:
    def __init__(self, x, y, coffee_type):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.coffee_type = coffee_type  # "Americano", "Latte", ...

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x - self.width // 2),
            int(self.y - self.height),
            self.width,
            self.height
        )

    def draw(self, screen, font_small):
        # 컵 몸체
        pygame.draw.rect(screen, (230, 230, 230), self.rect, border_radius=6)
        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=6)

        # 컵에 표시되는 글자 (커피 종류 첫 글자)
        label = self.coffee_type[0]  # 'A', 'L', 'M' 같은 느낌
        text = font_small.render(label, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


# ============================================
# 게임 메인 클래스
# ============================================
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mini I Love Coffee - Background & Coffee Machine")
        self.clock = pygame.time.Clock()

        # 폰트
        self.font_large = pygame.font.SysFont("malgungothic", 40)
        self.font_medium = pygame.font.SysFont("malgungothic", 24)
        self.font_small = pygame.font.SysFont("malgungothic", 18)

        # 배경 이미지 로드
        try:
            self.background = pygame.image.load("background.png")
            self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        except Exception as e:
            # 이미지가 없어도 에러 안 나게, 그냥 색으로 대체
            print("배경 이미지를 불러오지 못했습니다. (background.png가 필요해요)", e)
            self.background = None

        # 게임 상태
        self.running = True
        self.game_over = False

        # 손님 관련
        self.customers = []
        self.max_customers = 3
        self.spawn_interval = 3.0
        self.spawn_timer = 0.0

        # 점수/평판/시간
        self.money = 0
        self.reputation = 5
        self.game_time = 0.0
        self.time_limit = 60.0

        # 플레이어
        self.player = Player(WIDTH // 2, HEIGHT // 2 + 120)

        # 커피 머신 & 컵 관련
        self.coffee_cups = []
        self.coffee_spawn_interval = 4.0   # 커피 나오는 주기(초)
        self.coffee_spawn_timer = 0.0
        self.max_cups = 5

        # 머신 위치
        self.machine_x = WIDTH // 2
        self.machine_y = HEIGHT // 2 + 60

    # ---------------- 손님 / 커피 관련 로직 ----------------

    def spawn_customer(self):
        seat_positions = [
            (WIDTH // 4, HEIGHT // 2),
            (WIDTH // 2, HEIGHT // 2),
            (3 * WIDTH // 4, HEIGHT // 2),
        ]
        used = {(c.seat_x, c.seat_y) for c in self.customers if c.state != "leaving"}
        available = [pos for pos in seat_positions if pos not in used]
        if not available:
            return

        seat_x, seat_y = random.choice(available)
        order = random.choice(MENU_ITEMS)
        max_wait = random.uniform(8.0, 15.0)
        from_side = random.choice(["left", "right"])
        self.customers.append(Customer(seat_x, seat_y, order, max_wait, from_side))

    def spawn_coffee_cup(self):
        # 5잔 이상이면 더 이상 만들지 않음
        if len(self.coffee_cups) >= self.max_cups:
            return

        # 머신 앞에 좌→우로 줄 세우기
        base_x = self.machine_x - 90
        gap = 45
        x = base_x + len(self.coffee_cups) * gap
        y = self.machine_y + 40

        coffee_type = random.choice(MENU_ITEMS)
        cup = CoffeeCup(x, y, coffee_type)
        self.coffee_cups.append(cup)

    def player_pick_coffee(self):
        # 플레이어가 이미 들고 있으면 픽업 불가
        if self.player.held_coffee is not None:
            return

        for cup in list(self.coffee_cups):
            if self.player.rect.colliderect(cup.rect):
                self.player.held_coffee = cup.coffee_type
                self.coffee_cups.remove(cup)
                break

    def serve_customer(self):
        # 들고 있는 커피가 없으면 실패
        if self.player.held_coffee is None:
            self.reputation -= 1
            return

        # 플레이어 근처의 waiting 손님
        near_customers = [
            c for c in self.customers
            if c.state == "waiting" and self.player.is_near(c)
        ]

        if not near_customers:
            # 근처 손님 없음 → 서빙 실패
            self.reputation -= 1
            self.player.held_coffee = None
            return

        served = False

        for customer in near_customers:
            if customer.order == self.player.held_coffee:
                # 성공적으로 서빙
                wait_ratio = min(customer.wait_time / customer.max_wait, 1.0)
                tip = max(10, int(50 * (1.0 - wait_ratio)))
                self.money += tip

                if wait_ratio < 0.7:
                    self.reputation += 1
                else:
                    self.reputation -= 1

                customer.state = "leaving"
                customer.left_happy = True
                customer.timed_out = False
                served = True
                break

        if not served:
            # 메뉴가 안 맞음 → 평판 감소
            self.reputation -= 1

        # 커피는 어쨌든 손에서 사라짐
        self.player.held_coffee = None

    # ---------------- 업데이트 & 그리기 ----------------

    def update(self, dt):
        if self.game_over:
            return

        self.game_time += dt
        if self.game_time >= self.time_limit or self.reputation <= 0:
            self.game_over = True
            return

        keys = pygame.key.get_pressed()
        self.player.update(dt, keys)

        # 손님 생성 타이머
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval and len(self.customers) < self.max_customers:
            self.spawn_timer = 0.0
            self.spawn_customer()

        # 커피 생성 타이머
        self.coffee_spawn_timer += dt
        if self.coffee_spawn_timer >= self.coffee_spawn_interval:
            self.coffee_spawn_timer = 0.0
            self.spawn_coffee_cup()

        # 손님 업데이트
        for customer in list(self.customers):
            prev_state = customer.state
            customer.update(dt)

            # 타임아웃으로 떠나기 시작할 때 평판 감소 (한 번만)
            if customer.timed_out and not customer.timeout_penalized:
                if prev_state == "waiting" and customer.state == "leaving":
                    self.reputation -= 1
                    customer.timeout_penalized = True

            # 화면 밖으로 나가면 제거
            if customer.state == "leaving" and (customer.x > WIDTH + 100 or customer.x < -100):
                self.customers.remove(customer)

    def draw_background(self):
        # 배경 이미지 사용
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            # 이미지가 없으면 기본 배경
            self.screen.fill(FLOOR)

        # 카운터 (앞쪽 테이블)
        pygame.draw.rect(self.screen, BROWN, (0, HEIGHT // 2 + 60, WIDTH, 40))

        # 커피 머신
        machine_rect = pygame.Rect(self.machine_x - 40, self.machine_y - 60, 80, 60)
        pygame.draw.rect(self.screen, DARK_GRAY, machine_rect, border_radius=8)
        pygame.draw.rect(self.screen, BLACK, machine_rect, 2, border_radius=8)

        text = self.font_small.render("MACHINE", True, WHITE)
        text_rect = text.get_rect(center=machine_rect.center)
        self.screen.blit(text, text_rect)

    def draw_ui_bar(self):
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, WIDTH, 70))

        money_text = self.font_medium.render(f"돈: {self.money}원", True, WHITE)
        rep_text = self.font_medium.render(f"평판: {self.reputation}", True, WHITE)
        remaining = max(0, int(self.time_limit - self.game_time))
        time_text = self.font_medium.render(f"남은 시간: {remaining}초", True, WHITE)

        self.screen.blit(money_text, (20, 20))
        self.screen.blit(rep_text, (250, 20))
        self.screen.blit(time_text, (450, 20))

        held = self.player.held_coffee if self.player.held_coffee else "없음"
        held_text = self.font_medium.render(f"들고 있는 커피: {held}", True, WHITE)
        self.screen.blit(held_text, (620 - held_text.get_width() // 2, 20))

    def draw(self):
        self.draw_background()

        # 커피 컵
        for cup in self.coffee_cups:
            cup.draw(self.screen, self.font_small)

        # 손님
        for customer in self.customers:
            customer.draw(self.screen, self.font_small)

        # 플레이어
        self.player.draw(self.screen)

        # UI
        self.draw_ui_bar()

        # 게임 오버
        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))

            msg = "게임 종료!"
            msg2 = f"최종 돈: {self.money}원, 평판: {self.reputation}"
            msg3 = "ESC: 종료, R: 다시 시작"

            t1 = self.font_large.render(msg, True, WHITE)
            t2 = self.font_medium.render(msg2, True, WHITE)
            t3 = self.font_medium.render(msg3, True, WHITE)

            self.screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
            self.screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
            self.screen.blit(t3, t3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))

    # ---------------- 입력 처리 & 루프 ----------------

    def reset(self):
        self.customers.clear()
        self.coffee_cups.clear()
        self.money = 0
        self.reputation = 5
        self.game_time = 0.0
        self.spawn_timer = 0.0
        self.coffee_spawn_timer = 0.0
        self.player = Player(WIDTH // 2, HEIGHT // 2 + 120)
        self.game_over = False

    def handle_event(self, event):
        if self.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    self.reset()
            if event.type == pygame.QUIT:
                self.running = False
            return

        if event.type == pygame.QUIT:
            self.running = False
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            # 커피 줍기 (머신 앞 컵)
            if event.key == pygame.K_SPACE:
                self.player_pick_coffee()
            # 손님에게 서빙
            if event.key == pygame.K_f:
                self.serve_customer()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                self.handle_event(event)

            self.update(dt)
            self.draw()

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
