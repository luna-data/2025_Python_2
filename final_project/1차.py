import pygame
import random
import sys

# ==========================
# 윷 던지기 로직
# ==========================
def throw_yut():
    """
    윷 4개를 던져서 결과를 반환
    fronts = 1의 개수(앞면 개수)로 판단:
    1개 -> 도(1칸)
    2개 -> 개(2칸)
    3개 -> 걸(3칸)
    4개 -> 윷(4칸, 한 번 더)
    0개 -> 모(5칸, 한 번 더)
    """
    sticks = [random.randint(0, 1) for _ in range(4)]
    fronts = sum(sticks)

    if fronts == 1:
        name, move, extra = "도", 1, False
    elif fronts == 2:
        name, move, extra = "개", 2, False
    elif fronts == 3:
        name, move, extra = "걸", 3, False
    elif fronts == 4:
        name, move, extra = "윷", 4, True
    else:  # fronts == 0
        name, move, extra = "모", 5, True

    return sticks, name, move, extra

# ==========================
# 보드 좌표 생성 (원형 20칸)
# ==========================
def create_board_positions(center, radius, count):
    """
    원형으로 배치된 말 칸의 좌표 리스트 생성
    """
    import math
    cx, cy = center
    positions = []
    for i in range(count):
        angle = 2 * math.pi * i / count - math.pi / 2  # 위쪽에서 시작
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        positions.append((int(x), int(y)))
    return positions

# ==========================
# 메인 게임
# ==========================
def main():
    pygame.init()
    WIDTH, HEIGHT = 900, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("파이게임 윷놀이 (2인용)")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("malgungothic", 26)
    small_font = pygame.font.SysFont("malgungothic", 20)

    # 보드 20칸 생성
    BOARD_COUNT = 20
    board_positions = create_board_positions(center=(WIDTH // 2, HEIGHT // 2), 
                                             radius=200, 
                                             count=BOARD_COUNT)

    # 플레이어 말 위치 (-1 = 아직 출발 안함)
    player_positions = [-1, -1]  # [P1, P2]
    current_player = 0           # 0: P1, 1: P2

    # 메시지 상태
    yut_result_text = "스페이스바를 눌러 윷을 던지세요"
    info_text = "플레이어 1 차례"

    # 게임 상태
    game_over = False
    winner = None

    # 윷 막대 시각화용 좌표
    stick_rects = []
    base_x = 80
    base_y = 100
    stick_width = 40
    stick_height = 120
    gap = 10
    for i in range(4):
        x = base_x + i * (stick_width + gap)
        rect = pygame.Rect(x, base_y, stick_width, stick_height)
        stick_rects.append(rect)

    # 색깔 정의
    BG_COLOR = (240, 240, 255)
    BOARD_COLOR = (200, 200, 220)
    PLAYER_COLORS = [(255, 100, 100), (80, 160, 255)]
    STICK_BACK_COLOR = (210, 180, 140)  # 0 (뒷면)
    STICK_FRONT_COLOR = (255, 230, 180) # 1 (앞면)
    BLACK = (0, 0, 0)

    # 윷 결과 (stick 시각화용)
    last_sticks = [0, 0, 0, 0]

    def draw_board():
        # 배경
        screen.fill(BG_COLOR)

        # 보드 원형 배경
        pygame.draw.circle(screen, BOARD_COLOR, (WIDTH // 2, HEIGHT // 2), 220, 4)

        # 칸 표시 (작은 원)
        for i, pos in enumerate(board_positions):
            pygame.draw.circle(screen, (180, 180, 200), pos, 15, 2)
            # 칸 번호 (원래 윷판과는 다르지만, 이해를 위해 번호 표시)
            num_text = small_font.render(str(i), True, BLACK)
            text_rect = num_text.get_rect(center=(pos[0], pos[1] - 25))
            screen.blit(num_text, text_rect)

    def draw_pieces():
        # 각 플레이어 말 그리기
        # 같은 칸에 있을 때 살짝 옆으로 이동
        OFFSET = 8
        for p_idx in range(2):
            pos_idx = player_positions[p_idx]
            if pos_idx >= 0 and pos_idx < BOARD_COUNT:
                base_pos = board_positions[pos_idx]
                if p_idx == 0:
                    draw_pos = (base_pos[0] - OFFSET, base_pos[1])
                else:
                    draw_pos = (base_pos[0] + OFFSET, base_pos[1])
                pygame.draw.circle(screen, PLAYER_COLORS[p_idx], draw_pos, 12)

    def draw_yut_sticks():
        # 윷 막대 4개 그리기
        for i, rect in enumerate(stick_rects):
            val = last_sticks[i]
            color = STICK_FRONT_COLOR if val == 1 else STICK_BACK_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=8)
            pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
            # 앞/뒤 텍스트
            label = "앞" if val == 1 else "뒤"
            text = small_font.render(label, True, BLACK)
            text_rect = text.get_rect(center=(rect.centerx, rect.centery))
            screen.blit(text, text_rect)

        # 윷 설명 텍스트
        caption = small_font.render("윷 막대 (앞/뒤)", True, BLACK)
        screen.blit(caption, (stick_rects[0].x, stick_rects[0].y - 25))

    def draw_texts():
        # 상단 안내
        result_surface = font.render(yut_result_text, True, BLACK)
        screen.blit(result_surface, (50, 20))

        info_surface = font.render(info_text, True, BLACK)
        screen.blit(info_surface, (50, 60))

        # 플레이어 색 안내
        p1_label = small_font.render("플레이어 1 (빨강)", True, PLAYER_COLORS[0])
        p2_label = small_font.render("플레이어 2 (파랑)", True, PLAYER_COLORS[1])
        screen.blit(p1_label, (WIDTH - 250, 20))
        screen.blit(p2_label, (WIDTH - 250, 50))

        if game_over and winner is not None:
            win_text = font.render(f"플레이어 {winner+1} 승리! R 키로 재시작", True, (200, 0, 0))
            rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT - 60))
            screen.blit(win_text, rect)
        else:
            tip_text = small_font.render("스페이스바: 윷 던지기 / ESC: 종료", True, BLACK)
            rect = tip_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
            screen.blit(tip_text, rect)

    # ==========================
    # 메인 루프
    # ==========================
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

                # 게임 오버 후 재시작
                if game_over and event.key == pygame.K_r:
                    player_positions = [-1, -1]
                    current_player = 0
                    yut_result_text = "스페이스바를 눌러 윷을 던지세요"
                    info_text = "플레이어 1 차례"
                    last_sticks = [0, 0, 0, 0]
                    game_over = False
                    winner = None
                    continue

                # 스페이스바로 윷 던지기
                if event.key == pygame.K_SPACE and not game_over:
                    sticks, name, move, extra = throw_yut()
                    last_sticks = sticks

                    # 말 이동
                    old_pos = player_positions[current_player]
                    if old_pos == -1:
                        new_pos = move - 1  # 출발 시 0번 칸부터
                    else:
                        new_pos = old_pos + move

                    player_positions[current_player] = new_pos

                    # 승리 체크 (BOARD_COUNT를 넘으면 도착으로 간주)
                    if new_pos >= BOARD_COUNT:
                        game_over = True
                        winner = current_player
                        yut_result_text = f"플레이어 {current_player+1}이(가) {name}로 도착! 승리!"
                        info_text = "R 키로 게임을 다시 시작할 수 있습니다."
                    else:
                        # 턴 처리
                        if extra:
                            # 윷, 모면 한 번 더
                            yut_result_text = f"{name}! {move}칸 이동 + 한 번 더!"
                            info_text = f"플레이어 {current_player+1}이(가) 한 번 더 던집니다."
                        else:
                            yut_result_text = f"{name}! {move}칸 이동"
                            current_player = 1 - current_player
                            info_text = f"플레이어 {current_player+1} 차례"

        # 그리기
        draw_board()
        draw_pieces()
        draw_yut_sticks()
        draw_texts()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
