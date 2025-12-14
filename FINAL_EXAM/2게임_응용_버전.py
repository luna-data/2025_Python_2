import pygame
import os
base_dir=os.path.dirname(__file__)

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("제목")

#게임 속도 조절
clock=pygame.time.Clock()

# 이동 테스트용 좌표 - 선수 상속, 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #플레이어 생성자 --> 사진으로 선수 불러오고 크기조절
        self.img_path=os.path.join(base_dir,"dukbird.png")
        self.image=pygame.image.load(self.img_path)
        self.image=pygame.transform.scale(self.image,(150,150))
        #이미지 감싸는 사각형 정보 저장 -> 중심을 화면 중앙에 배치
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH//2,HEIGHT//2)
        self.speed=3

    def update(self):
        #눌리는 모든 키의 상태를 가져옴
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())


#스프라이트 그룹
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)

running=True

#게임 루프
while running:
    #창 닫으면 루프 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

  # 화면 그리기
    screen.fill((170,200,255))
    pygame.draw.rect(screen,(80,170,80),(0,HEIGHT-60,WIDTH,60)) #바닥 그림 초록
    pygame.draw.rect(screen,(255,80,80),(50,280,40,40)) #데코용 도형들
    pygame.draw.circle(screen,(0,255,0),(450,150),20)
    pygame.draw.line(screen,(0,0,0),(300,300),(500,500),5)

    all_sprites.draw(screen) #선수 그리기
    
    #화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()