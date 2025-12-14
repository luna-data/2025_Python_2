'''파이썬 게임 - 카페알바 게임
클래스 - 알바생, 손님, 음료
랜덤 기능 - 손님생성, 음료생성
키보드 이벤트 - 스페이스바: 음료 드는 기능, 방향키: 알바생 위치조정, g키: 음료 드리기
1차 - 클래스와 배경 설정 중심 + 이동
2차 - 기능 완벽히 + 보완하기 
-> (게임 시작/끝 메시지 출력부분)
-> 손님이 너무 빨리 지나감
-> 커피들이 3초에 4종류 한번에 나오길 바랬는데, 이 부분에서 문제가 생김
이미지 생성 : 지피티
 '''

import pygame
import random
import os

base_dir = os.path.dirname(__file__)
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("커피알바 게임")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)

#폰트 적용이 안되어서 이 코드로 폰트 적용하기!
pygame.font.init()

FONT_PATH = os.path.join(base_dir, "NanumGothic.ttf")
font = pygame.font.Font(FONT_PATH, 22)
font_big = pygame.font.Font(FONT_PATH, 40)


bg_path=os.path.join(base_dir, "background.png")
bg_image=pygame.image.load(bg_path).convert()
bg_image=pygame.transform.scale(bg_image, (WIDTH,HEIGHT))



pygame.mixer.init()
BGM_PATH = os.path.join(base_dir, "bgm_fixed.wav")
pygame.mixer.music.load(BGM_PATH)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.img_path=os.path.join(base_dir,"bini.png")
    self.image=pygame.image.load(self.img_path)
    self.image=pygame.transform.scale(self.image,(100,100))
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

coffee=["americano","ade","chocolatte","icetea"]
coffee_images={}
for i in coffee:
    path = os.path.join(base_dir, f"{i}.png")
    img = pygame.image.load(path).convert_alpha()
    coffee_images[i] = pygame.transform.scale(img, (50, 50))


class Coffee(pygame.sprite.Sprite):
    TYPE=None # 자식클래스에서 각각 지정할 예정
    def __init__(self, x, y,slot):
        super().__init__()
        if self.TYPE is None: #타입 지정하지 않을 시 에러 날 수 있게 합니다
            raise ValueError("coffee TYPE 이 자식클래스에서 반드시 정의되어야 합니다!!")
        
        #딕셔너리 이용해서 이미지 연결할 때 사용
        self.image=coffee_images[self.TYPE]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.slot=slot

        self.speed_x = 0                 
        self.speed_y = 0     

#수업시간에 배웠던 상속구조 활용           
class Americano(Coffee):
    TYPE="americano"
class Ade(Coffee):
    TYPE="ade"
class Chocolatte(Coffee):
    TYPE="chocolatte"
class Icetea(Coffee):
    TYPE="icetea"


#입구부터 시작 그리고 테이블 근처 좌표 설정
ENTRANCE=(-60,180)
TABLE_POSITIONS=[(250,220),(400,220),(550,220)]


#손님클래스 시작 부분
#손님이 들어오는 입구는 한곳으로 지정, 각 테이블로 랜덤으로 이동
#즉, 입구에서 생성되어 테이블 중 하나로 가고 근처에서 멈추기
# 입장-> 이동 -> 대기 후 (5초) -> 퇴장
class Customer(pygame.sprite.Sprite):
    def __init__(self,seat,order):
        super().__init__()

        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (205, 133, 63), (25, 25), 25)
        pygame.draw.circle(self.image, (80, 80, 80), (25, 25), 25, 2)
        
        self.rect=self.image.get_rect(center=ENTRANCE)
        self.order = order

        self.seat=seat

        self.state="walking"
        self.wait_frames=0
        self.max_wait_frames=random.randint(60*6, 60*10)

        self.left_happy=False
        self.timeout_penalized=False
        self.walk_speed=2


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
        elif self.state=="waiting":
            self.wait_frames += 1
            if self.wait_frames >= self.max_wait_frames:
                self.state = "leaving"
        elif self.state =="leaving":
            self.rect.x+=3

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

class Machine:
    def __init__(self,rect,drink_c,type_group,all_sprites,all_drink_group,cap=5):
        self.rect=rect
        self.drink_c=drink_c
        self.type_group=type_group
        self.all_sprites=all_sprites
        self.all_drink_group=all_drink_group
        self.cap=cap

    def can_spawn(self):
        return len(self.type_group)<self.cap
    
    def spawn(self):
        if not self.can_spawn():
            return None
        
        used_slots = {d.slot for d in self.type_group}
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

PRICE={
    "americano": 2500,
    "ade": 3500,
    "chocolatte": 4000,
    "icetea": 3000
}

machines=[
    Machine(M1,Americano,a_group,all_sprites,coffee_group,cap=3),
    Machine(M2,Ade,ad_group,all_sprites,coffee_group,cap=3),
    Machine(M3,Chocolatte,c_group,all_sprites,coffee_group,cap=3),
    Machine(M4,Icetea,i_group,all_sprites,coffee_group,cap=3),
]

def spawn_customer():
    seat=random.choice(TABLE_POSITIONS)

    seated=set()
    for c in customer_group:
        if c.state in ("walking","waiting"):
            seated.add(c.seat)
    available=[]
    for pos in TABLE_POSITIONS:
        if pos not in seated:
            available.append(pos)
    if available:
        seat=random.choice(available)
    
    order=random.choice(coffee)
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

    #첫번쨰 다음부터 이 코드로 실행, 3개 넘지 않게 실행
    for m in machines:
        if m.can_spawn():
            m.spawn()

#손님 생성 타이머로 빠르게 게임을 하고싶다면 이부분을 더 짧게 바꾸기
customer_timer = 1
CUSTOMER_INTERVAL = 300  #커피 생성 속도와 같은 3초로 설정, 너무 짧음. 3->5초

#플레이어가 들고 있는 음료 저장
player.held = None

#SPACE 바로 음료 들기
def pick_coffee():
    if player.held is not None:
        return

    #머신 근처에서만 들 수있음
    if not any(player.rect.colliderect(m.rect.inflate(80, 80)) for m in machines):
        return

    if len(coffee_group)==0:
        return
    
    px,py=player.rect.center
    min_dist=float("inf")

    for cup in coffee_group:
        cx,cy=cup.rect.center
        dist=(cx-px) **2+(cy-py) **2
        if dist<min_dist:
            min_dist=dist
            chosen=cup
    if min_dist>80**2:
        return
    
    player.held = chosen # 음료 객체를 든 상태
    chosen.kill()

    a_group.remove(chosen)
    ad_group.remove(chosen)
    c_group.remove(chosen)
    i_group.remove(chosen)
    #위 코드에서 플레이어가 든 음료는 종류별 그룹에서도 제거해야함.
    #이 과정을 거치지 않으면 나중에 꼬일 수있음
       
#G키로 가까운 손님에게 음료 드리기
def give_coffee():
    global lives, money

    if player.held is None:
        lives-=1
        return

    near_zone = player.rect.inflate(160, 160)
    served = False

    for c in list(customer_group):
        if c.state != "waiting":
            continue

        if near_zone.colliderect(c.rect):
            served=True

            #주문 맞디면 성공!!
            if c.order == player.held.TYPE:
                c.left_happy = True
                money+=PRICE.get(c.order,0)
            else:
                c.left_happy = False
                lives-=1

            c.state = "leaving"
            break

    if not served:
        lives -=1

    #커피는 잘못된 손님께 드려도 어차피 사용된 상태로 표현됨
    player.held.kill()  #들고있던 객체는 화면에서 제거하기
    player.held = None

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
def draw_money(surf, money):
    txt=font.render(f"판매: {money}원", True, BLACK)
    surf.blit(txt,(10,70))

game_state="start"

def reset_game():
    global lives, money, customer_timer, spawn_timer,spawn_index
    lives=LIVES_MAX
    money=0
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

#작동 실행부분 -- 메인루프가 돌아가는 코드
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if game_state=="start":
                if event.key==pygame.K_RETURN:
                    reset_game()
                    game_state="play"
                    pygame.mixer.music.play(-1)

            elif game_state=="gameover":
                if event.key==pygame.K_RETURN:
                    reset_game()
                    game_state="play"
                    pygame.mixer.music.play(-1)

            elif game_state=="play":
                if event.key == pygame.K_SPACE:
                    pick_coffee()
                if event.key == pygame.K_g:
                    give_coffee()

    if game_state=="play":
        all_sprites.update()
        spawn_all_coffee_every_3s()

        #손님은 3초마다 생성됩니당
        customer_timer += 1
        if customer_timer >= CUSTOMER_INTERVAL:
            customer_timer = 0
            spawn_customer()
        
        #화면 밖 손님 제거
        for c in list(customer_group):
            if c.rect.left>WIDTH+80:
                c.kill()
        
        if lives <=0:
            game_state="gameover"
            pygame.mixer.music.stop()

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
    ui = font.render(f"beverage: {held}", True, BLACK)
    screen.blit(ui, (10, 10))

    draw_lives(screen,lives)
    draw_money(screen, money)

    if game_state == "start":
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))
        t1 = font.render("커피알바 게임", True, WHITE)
        t2 = font.render("Enter: 시작하기  /  SPACE: 음료 들기  G: 서빙하기", True, WHITE)
        t3 = font.render("방향키로 알바생 위치 조정, 스페이스로 음료 선택 후 g키로 음료 서빙하시면 됩니다.",True, WHITE)
        t4 = font.render("목숨은 총 3개이며 잘못된 서빙, 손님이 기다리다 나간 상황에서는 -1 됩니다.",True, WHITE)
        
        screen.blit(t1, t1.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
        screen.blit(t2, t2.get_rect(center=(WIDTH//2, HEIGHT//2 - 30)))
        screen.blit(t3, t3.get_rect(center=(WIDTH//2, HEIGHT//2 + 30)))
        screen.blit(t4, t4.get_rect(center=(WIDTH//2, HEIGHT//2 + 60)))

    elif game_state == "gameover":
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))
        t1 = font.render("GAME OVER", True, WHITE)
        t2 = font.render(f"판매금액: {money}원  /  Enter: 재시작하기", True, WHITE)
        screen.blit(t1, t1.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
        screen.blit(t2, t2.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()