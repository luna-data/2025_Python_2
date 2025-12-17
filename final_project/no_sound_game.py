'''파이썬 게임 - 카페알바 게임
클래스 - 알바생, 손님, 음료, 기계
랜덤 기능 - 손님생성, 음료생성
키보드 이벤트 - 스페이스바: 음료 드는 기능, 방향키: 알바생 위치조정, g키: 음료 드리기
1차 - 클래스와 배경 설정 중심 + 이동
2차 - 기능 완벽히 + 보완하기 
-> (게임 시작/끝 메시지 출력부분)
-> 손님이 너무 빨리 지나감
-> 커피들이 3초에 4종류 한번에 나오길 바랬는데, 이 부분에서 문제가 생김 -> 해결완료
이미지 생성 : 지피티
 '''

import pygame
import random
import os

base_dir = os.path.dirname(__file__)
pygame.init()

#화면 생성 (기존 게임코드보다 화면 확장)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("커피알바 게임")

clock = pygame.time.Clock()

#사용색상 정의 -> 정의 안하면 문제생김
WHITE = (255,255,255)
BLACK = (0,0,0)

#폰트 적용이 안되어서 이 코드로 폰트 적용하기!
pygame.font.init()

FONT_PATH = os.path.join(base_dir, "NanumGothic.ttf")
font = pygame.font.Font(FONT_PATH, 22)
font_big = pygame.font.Font(FONT_PATH, 40)

#일반 색상 배경 외에 사진배경 설정하고 싶어서 따로 정의하기!
bg_path=os.path.join(base_dir, "background.png")
bg_image=pygame.image.load(bg_path).convert()
bg_image=pygame.transform.scale(bg_image, (WIDTH,HEIGHT))

game_state="start" #게임상태 정의

#알바생 - 플레이어 클래스
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.img_path=os.path.join(base_dir,"bini.png")
    self.image=pygame.image.load(self.img_path)
    self.image=pygame.transform.scale(self.image,(100,100))
    self.rect=self.image.get_rect() #화면에 표시될 사각형(범위) 생성
    self.rect.center=(WIDTH//2,HEIGHT//2)
    self.speed=3 #이동 속도

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

    #화면 밖으로 나가지 못하도록 고정하기
    self.rect.clamp_ip(screen.get_rect())

#음료종류 리스트와 이미지 불러오기 (각 음료별 다른 이미지)
coffee=["americano","ade","chocolatte","icetea"]
coffee_images={}
for i in coffee:
    path = os.path.join(base_dir, f"{i}.png")
    img = pygame.image.load(path).convert_alpha()
    coffee_images[i] = pygame.transform.scale(img, (50, 50))

#음료 클래스(커피클래스 - 부모)
class Coffee(pygame.sprite.Sprite):
    TYPE=None # 자식클래스에서 각각 지정할 예정
    def __init__(self, x, y,slot):
        super().__init__()
        if self.TYPE is None: #타입 지정하지 않을 시 에러 날 수 있게 합니다
            raise ValueError("coffee TYPE 이 자식클래스에서 반드시 정의되어야 합니다!!")
        
        #딕셔너리 이용해서 이미지 연결할 때 사용, 각 TYPE에 맞는 이미지 사용하기
        self.image=coffee_images[self.TYPE]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.slot=slot

        self.speed_x = 0                 
        self.speed_y = 0     

#수업시간에 배웠던 상속구조 활용, 음료 종류별 자식클래스           
class Americano(Coffee):
    TYPE="americano"
class Ade(Coffee):
    TYPE="ade"
class Chocolatte(Coffee):
    TYPE="chocolatte"
class Icetea(Coffee):
    TYPE="icetea"


#입구부터 시작 그리고 테이블 근처 좌표 설정
ENTRANCE=(-60,180) #손님이 들어오는 시작위치로 왼쪽 밖에서 생성됨
TABLE_POSITIONS=[(200,220),(250,220),(300,220),(400,220),(480,220),(550,220)] #손님이 테이블에 오는 좌표


#손님클래스 시작 부분
#손님이 들어오는 입구는 한곳으로 지정, 각 테이블로 랜덤으로 이동
#즉, 입구에서 생성되어 테이블 중 하나로 가고 근처에서 멈추기
# 입장-> 이동 -> 대기 후 (5초) -> 퇴장
class Customer(pygame.sprite.Sprite):
    def __init__(self,seat,order):
        super().__init__()

        self.image = pygame.Surface((50, 50), pygame.SRCALPHA) #손님 표현은 동그라미로
        pygame.draw.circle(self.image, (205, 133, 63), (25, 25), 25)
        pygame.draw.circle(self.image, (80, 80, 80), (25, 25), 25, 2)
        
        self.rect=self.image.get_rect(center=ENTRANCE)
        self.order = order

        self.seat=seat

        self.state="walking" #손님의 상태 나타내기
        self.wait_frames=0 #손님이 기다린 시간 

        #손님이 기다리는 최대시간은 5~8초로 설정
        self.max_wait_frames=random.randint(60*5, 60*8)

        #서빙결과와 시간초과 관련
        self.left_happy=False
        self.timeout_penalized=False
        self.walk_speed=2 #이동 속도 설정

    #손님의 움직임 상태를 업데이트 하는 함수
    def update(self):
        if self.state=="walking":
            tarx,tary=self.seat
            carx,cary=self.rect.center

            disx=tarx-carx
            disy=tary-cary

            if abs(disx) <=2 and abs(disy) <=2:
                self.rect.center=self.seat
                self.state="waiting"
            else:
                if disx>0:
                    self.rect.x +=self.walk_speed
                elif disx<0:
                    self.rect.x -= self.walk_speed

                if disy>0:
                    self.rect.y +=self.walk_speed
                elif disy<0:
                    self.rect.y -= self.walk_speed

        #자리에서 기다리는 시간 증가시키는 부분
        elif self.state=="waiting":
            self.wait_frames += 1
            if self.wait_frames >= self.max_wait_frames: #기다리는 시간의 최대치 넘으면 퇴장
                self.state = "leaving"
        elif self.state =="leaving":
            self.rect.x+=3

    #손님의 주문과 미션에 대한 감정(감사, 슬픔) 표시
    def draw_bubble(self,surf):
        if self.state in ("walking","waiting"):
            text_str=self.order
        else:
            if self.left_happy==True:
                text_str="Thanks" 
            else:
                text_str="ㅠㅠ"

        txt=font.render(text_str,True,BLACK)

        bubble=pygame.Rect(0,0,txt.get_width()+10,txt.get_height()+6)
        bubble.midbottom=(self.rect.centerx, self.rect.top-5)

        pygame.draw.rect(surf,WHITE,bubble,border_radius=6)
        pygame.draw.rect(surf,BLACK,bubble,1,border_radius=6)
        surf.blit(txt,(bubble.x+5,bubble.y+3))

#커피머신 클래스
class Machine:
    def __init__(self,rect,drink_c,type_group,all_sprites,all_drink_group,cap=5):
        self.rect=rect
        self.drink_c=drink_c
        self.type_group=type_group
        self.all_sprites=all_sprites
        self.all_drink_group=all_drink_group #모든 커피 담는 곳
        self.cap=cap #머신에서 최대로 만들 수 있는 커피 수

    #cap보다 적으면 생성하기
    def can_spawn(self):
        return len(self.type_group)<self.cap
    
    #실제 음료 생성부분
    def spawn(self):
        if not self.can_spawn():
            return None
        
        #이미 음료가 제조된 부분의 번호 수집
        used_slots = {d.slot for d in self.type_group}

        #빈 곳에 음료를 생성할 수 있게 찾기
        slot=None
        for i in range(self.cap):
            if i not in used_slots:
                slot=i
                break
        if slot is None:
            return None
        
        x=self.rect.x+10+slot*55
        y=self.rect.bottom+5

        drink=self.drink_c(x,y,slot)
        self.type_group.add(drink)
        self.all_sprites.add(drink)
        self.all_drink_group.add(drink)
        return drink
    
#===================
#커피 머신 시작 (x,y,width,height)
M1=pygame.Rect(70,430,150,60)
M2=pygame.Rect(250,430,150,60)
M3=pygame.Rect(430,430,150,60)
M4=pygame.Rect(610,430,150,60)

all_sprites = pygame.sprite.Group()
customer_group = pygame.sprite.Group()

a_group=pygame.sprite.Group()
ad_group=pygame.sprite.Group()
c_group=pygame.sprite.Group()
i_group=pygame.sprite.Group()

coffee_group=pygame.sprite.Group()

player = Player()
all_sprites.add(player)

LIVES_MAX = 3
lives = LIVES_MAX
money=0

#커피 가격표 
PRICE={
    "americano": 2500,
    "ade": 3500,
    "chocolatte": 4000,
    "icetea": 3000
}

#머신 리스트로 각 머신은 한 종류만 생성할 수 있도록 지정
machines=[
    Machine(M1,Americano,a_group,all_sprites,coffee_group,cap=3),
    Machine(M2,Ade,ad_group,all_sprites,coffee_group,cap=3),
    Machine(M3,Chocolatte,c_group,all_sprites,coffee_group,cap=3),
    Machine(M4,Icetea,i_group,all_sprites,coffee_group,cap=3),
]

#클래스 외 함수 부분
def spawn_customer():
    seat=random.choice(TABLE_POSITIONS)

    seated=set() #이미 테이블에 손님이 있으면 그 테이블은 피하기
    for c in customer_group:
        if c.state in ("walking","waiting"):
            seated.add(c.seat)

    #비어있는 테이블 수집
    available=[]
    for pos in TABLE_POSITIONS:
        if pos not in seated:
            available.append(pos)
    
    #빈 테이블을 랜덤 선택하기
    if available:
        seat=random.choice(available)
    
    #주문 랜덤 선택하기
    order=random.choice(coffee)

    #손님 생성 후 그룹에 추가
    c=Customer(seat,order)
    customer_group.add(c)
    all_sprites.add(c)

#3초마다 각 머신에서 음료 생성되는 코드
FPS = 60
SPAWN_INTERVAL_FRAMES = 3 * FPS
spawn_timer = 0
spawn_index = 0

def spawn_all_coffee_every_3s():
    global spawn_timer
    spawn_timer += 1
    if spawn_timer < SPAWN_INTERVAL_FRAMES:
        return
    spawn_timer = 0

    #첫번쨰 다음부터 이 코드로 실행, cap(3개) 넘지 않게 실행
    for m in machines:
        if m.can_spawn():
            m.spawn()

#손님 생성 타이머로 빠르게 게임을 하고싶다면 이부분을 더 짧게 바꾸기
customer_timer = 1
CUSTOMER_INTERVAL = 300 #커피 생성 속도와 같은 3초로 설정, 이부분을 늘리면 더 빨라짐

#플레이어가 들고 있는 음료 저장
player.held = None

#제한시간 설정 (1분)
TIME_LIMIT=60
time_left=TIME_LIMIT * FPS

sell_count=0 #판매한 음료 '잔 수' 카운트하는 변수

#SPACE 바로 음료 들기
def pick_coffee():
    if player.held is not None:
        return

    #머신 근처에서만 들 수있음
    if not any(player.rect.colliderect(m.rect.inflate(80, 80)) for m in machines):
        return

    if len(coffee_group)==0:
        return
    
    #플레이어의 현재 위치에서 가장 가까운 커피 찾기
    px,py=player.rect.center
    min_dist=float("inf")

    for cup in coffee_group:
        cx,cy=cup.rect.center
        dist=(cx-px) **2+(cy-py) **2
        if dist<min_dist:
            min_dist=dist
            chosen=cup

    #거리가 멀면 잡지 못하도록 설정
    if min_dist>80**2:
        return
    
    player.held = chosen # 음료 객체를 든 상태
    chosen.kill() #음료는 플레이어가 든 상태라 화면에서 제거

    a_group.remove(chosen)
    ad_group.remove(chosen)
    c_group.remove(chosen)
    i_group.remove(chosen)
    #위 코드에서 플레이어가 든 음료는 종류별 그룹에서도 제거해야함.
    #이 과정을 거치지 않으면 나중에 꼬일 수있음
       
#G키로 가까운 손님에게 음료 드리기
def give_coffee():
    global lives, money, sell_count

    if player.held is None:
        lives-=1
        return

    #서빙가능한 범위 설정하기
    near_zone = player.rect.inflate(160, 160)
    served = False

    #waiting 상태의 손님 중 가까운 손님에게만 서빙할 수 있도록 설정하기
    for c in list(customer_group):
        if c.state != "waiting":
            continue

        if near_zone.colliderect(c.rect):
            served=True

            #주문 맞디면 성공!! -> 돈 증가 + 판매 잔수 증가
            if c.order == player.held.TYPE:
                c.left_happy = True
                money+=PRICE.get(c.order,0)
                sell_count+=1
            else:
                c.left_happy = False
                lives-=1

            c.state = "leaving"
            break
    # 손님으로부터 멀리 떨어져서 서빙 시 불친절 -> 목숨한개 잃기
    if not served:
        lives -=1

    #커피는 잘못된 손님께 드려도 어차피 사용된 상태로 표현됨
    player.held.kill()  #들고있던 객체는 화면에서 제거하기
    player.held = None

#생명(3개 동그라미 그리기)
def draw_lives(surf, lives):
    y=45
    r=10
    for i in range(LIVES_MAX):
        x=20+i*26
        if i<lives:
            pygame.draw.circle(surf,(250,205,70),(x,y),r)
            pygame.draw.circle(surf,(150,110,30),(x,y),r,2)
        else:
            pygame.draw.circle(surf,(210,210,210),(x,y),r)
            pygame.draw.circle(surf,(120,120,120),(x,y),r,2)

#판매금액 표시하기
def draw_money(surf, money):
    txt=font.render(f"판매: {money}원", True, BLACK)
    surf.blit(txt,(10,70))

#남은시간 표시하기
def draw_timer(surf, time_left):
    seconds = max(0, time_left // FPS)
    txt = font.render(f"Time: {seconds}s", True, BLACK)
    surf.blit(txt, (WIDTH - 140, 10))

#게임 재시작 부분 -> 초기화와 그룹 비우기
def reset_game():
    global lives, money, customer_timer, spawn_timer, time_left, sell_count
    lives=LIVES_MAX

    lives=LIVES_MAX
    money=0
    sell_count=0
    time_left=TIME_LIMIT*FPS

    player.rect.center=(WIDTH//2,HEIGHT//2)
    player.held=None

    #플레이어 객체만 놔두고 모두 비워주기. 새 게임 시작
    all_sprites.empty()
    all_sprites.add(player)

    customer_group.empty()
    coffee_group.empty()
    a_group.empty()
    ad_group.empty()
    c_group.empty()
    i_group.empty()


    customer_timer=0
    spawn_timer=0

#==================작동 실행부분 -- 메인루프가 돌아가는 코드==================
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 버튼
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #esc 누르면 게임 종료
                running = False

            if game_state=="start":
                if event.key==pygame.K_RETURN: #엔터 게임 시작
                    reset_game()
                    game_state="play"

            elif game_state=="gameover":
                if event.key==pygame.K_RETURN:
                    reset_game()
                    game_state="play"

            elif game_state=="play": #스페이스바와 g키로 음료 들고 서빙
                if event.key == pygame.K_SPACE:
                    pick_coffee()
                if event.key == pygame.K_g:
                    give_coffee()

    if game_state=="play":
        time_left -= 1 #1초마다 제한시간 감소
        if time_left <=0: #시간이 끝나면 게임오버
            game_state="gameover"

        all_sprites.update()
        spawn_all_coffee_every_3s()

        #손님은 일정 프레임마다 생성됩니다.
        customer_timer += 1
        if customer_timer >= CUSTOMER_INTERVAL:
            customer_timer = 0
            spawn_customer()
        
        #화면 밖 손님 제거
        for c in list(customer_group):
            if c.rect.left>WIDTH+80:
                c.kill()
        
        #목숨 0개 이하면 게임 끝
        if lives <=0:
            game_state="gameover"

        #손님이 시간초과로 떠난 경우 패널티 (목숨-1)
        for c in list(customer_group):
            if c.state == "leaving" and not c.left_happy and not c.timeout_penalized:
                if c.wait_frames >= c.max_wait_frames:
                    lives -= 1
                    c.timeout_penalized = True


    # ------------------ 그리기 ------------------
    screen.blit(bg_image, (0, 0))

    #머신 그리기
    for m in machines:
        pygame.draw.rect(screen, (60, 60, 60), m.rect, border_radius=12)
        pygame.draw.rect(screen, BLACK, m.rect, 2, border_radius=12)

    #머신 라벨
    labels = ["AME", "ADE", "CHOCO", "TEA"]
    for idx, m in enumerate(machines):
        t = font.render(labels[idx], True, WHITE)
        screen.blit(t, t.get_rect(center=m.rect.center))

    #플레이어가 가장 윗부분에 보이도록 설정 -> 이전에는 커피나 다른그림에 가려짐
    for s in all_sprites:
        if s!= player:
            screen.blit(s.image, s.rect)
    screen.blit(player.image, player.rect)

    #손님 말풍선
    for c in customer_group:
        c.draw_bubble(screen)

    #들고있는 음료 표시
    held = player.held.TYPE if player.held else "none"
    ui = font.render(f"현재 선택 음료: {held}", True, BLACK)
    screen.blit(ui, (10, 10))

    #게임 화면에 표시할 부분
    draw_lives(screen,lives)
    draw_money(screen, money)
    draw_timer(screen, time_left)

    #게임 시작 부분 안내사항
    if game_state == "start":
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))
        t1 = font.render("커피알바 게임 [제한시간: 1분]", True, WHITE)
        t2 = font.render("Enter: 시작하기  /  SPACE: 음료 들기  G: 서빙하기", True, WHITE)
        t3 = font.render("방향키로 알바생 위치 조정, 스페이스로 음료 선택 후 g키로 음료 서빙하시면 됩니다.",True, WHITE)
        t4 = font.render("\n 목숨은 총 3개이며 잘못된 서빙, 손님이 기다리다 나간 상황에서는 -1 됩니다.",True, WHITE)
        
        screen.blit(t1, t1.get_rect(center=(WIDTH//2, HEIGHT//2 - 90)))
        screen.blit(t2, t2.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
        screen.blit(t3, t3.get_rect(center=(WIDTH//2, HEIGHT//2 + 30)))
        screen.blit(t4, t4.get_rect(center=(WIDTH//2, HEIGHT//2 + 60)))

    #게임오버 화면 
    elif game_state == "gameover":
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))
        t1 = font.render("GAME OVER", True, WHITE)
        t2 = font.render(f"판매금액: {money}원  /  판매 잔수: {sell_count}잔", True, WHITE)
        t3 = font.render(f"재시작하시겠습니까? (Enter: 재시작하기)", True, WHITE)
        screen.blit(t1, t1.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
        screen.blit(t2, t2.get_rect(center=(WIDTH//2, HEIGHT//2 - 10)))
        screen.blit(t3, t3.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()