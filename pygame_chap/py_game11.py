import pygame, random
import os
base_dir=os.path.dirname(__file__)

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9")

clock=pygame.time.Clock()

apple_path=os.path.join(base_dir,"apple.png")
apple_image=pygame.image.load(apple_path)
apple_image=pygame.transform.scale(apple_image,(40,40))

poop_path=os.path.join(base_dir,"poop.png")
poop_image=pygame.image.load(poop_path)
poop_image=pygame.transform.scale(poop_image,(40,40))

# 이동 테스트용 좌표
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_path=os.path.join(base_dir,"bini.png")
        self.image=pygame.image.load(self.img_path)
        self.image=pygame.transform.scale(self.image,(150,150))
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH//2,HEIGHT//2)
        self.speed=3

    def update(self):
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
class Enemy(pygame.sprite.Sprite): # 추가: Enemy Sprite 클래스 (빨간 박스 위치에 적 배치)
    def __init__(self, x, y):
        super().__init__()
        self.image = poop_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed_x = 3
        self.speed_y = 2

    def update(self): # 좌우로 살짝 움직이게 해서 "살아있는 적" 느낌
        self.rect.x += self.speed_x
        self.rect.y +=self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top<0 or self.rect.bottom>HEIGHT:
            self.speed_y *= -1

all_sprites=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()

player=Player()
all_sprites.add(player)

enemy=Enemy(50,260)
all_sprites.add(enemy)
enemy_group.add(enemy)
coin_rect=pygame.Rect(430,130,40,40)

coin_speed_x=2
coin_speed_y=2

score=0
running=True
game_over=False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if game_over and event.key==pygame.K_RETURN:
                game_over=False
                score=0

                player.rect.center=(WIDTH//2, HEIGHT//2)

                enemy.rect.topleft=(50,260)
                enemy.speed_x=3
                enemy.speed_y=2

                coin_rect.x=430
                coin_rect.y=130
                coin_speed_x=2
                coin_speed_y=2

        if not game_over:
            all_sprites.update()
            coin_rect.x+= coin_speed_x
            coin_rect.y+=coin_speed_y

            if coin_rect.left<0 or coin_rect.right > WIDTH:
                coin_speed_x *= -1
            if coin_rect.top<0 or coin_rect.bottom>HEIGHT:
                coin_speed_y *= -1

            if player.rect.colliderect(coin_rect):
                score+=1
                print("사과 먹음!")
                
                #추가: 사과를 화면 내 랜덤 위치로 순간 이동
                coin_rect.x = random.randint(0, WIDTH - coin_rect.width)
                coin_rect.y = random.randint(0, HEIGHT - coin_rect.height)

                #추가: 이동 방향도 랜덤하게 반전
                coin_speed_x *= random.choice([-1, 1])
                coin_speed_y *= random.choice([-1, 1])

                # hits=pygame.sprite.spritecollide(player,enemy_group)

        
        hits=pygame.sprite.spritecollide(player, enemy_group,False)
        if hits:
            print('똥에 닿음! 게임 오버')
            game_over=True

  # 화면 그리기
    screen.fill((170,200,255))
    pygame.draw.rect(screen,(80,170,80),(0,HEIGHT-60,WIDTH,60))
        #pygame.draw.circle(screen,(0,255,0),(coin_rect.x+coin_rect.width//2,coin_rect.y+coin_rect.height//2),20)
       # pygame.draw.line(screen,(0,0,0),(300,300),(500,500),5)
    screen.blit(apple_image,coin_rect)
    all_sprites.draw(screen)
    
    font=pygame.font.SysFont(None, 24)
    text=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(text,(10,10))

    if game_over:
        over_text=font.render("GAME OVER",True, (255,0,0))
        over_x=(WIDTH-over_text.get_width())//2
        over_y=(HEIGHT-over_text.get_height())//2
        screen.blit(over_text, (over_x, over_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()