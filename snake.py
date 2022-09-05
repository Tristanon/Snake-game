#import:
import pygame , random ,time, sys, ctypes
pygame.init()
#load hình ảnh:
m = 20
Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(m,m))
Imghead = pygame.transform.scale(pygame.image.load('head.jpg'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('nguhung.jpg'),(m,m))
#tạo cưa sổ:
gameSurface = pygame.display.set_mode((1280,700))
pygame.display.set_caption('Game con rắn')
#màu sắc:
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
#khai báo biến
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,128)
foody = random.randrange(1,70)
if foodx % 2 != 0: foodx +=1
if foody % 2 != 0: foody +=1
foodpos = [foodx * 10, foody *10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0
#hàm gameover
def game_over():
    gfont = pygame.font.SysFont('consolas',40)
    gsurf = gfont.render('Game Over!',True,red)
    grect = gsurf.get_rect()
    grect.midtop = (640,250)
    gameSurface.blit(gsurf,grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()
#hàm show_score:
def show_score(choice = 1):
    sfont = pygame.font.SysFont('consolas',20)
    ssurf = sfont.render('Score: {0}'.format(score),True,black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (640,320)
    gameSurface.blit(ssurf,srect)
#vòng lặp chính
while True: 
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # xử lý phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                changeto = 'RIGHT'
            if event.key == pygame.K_a:
                changeto = 'LEFT'
            if event.key == pygame.K_w:
                changeto = 'DOWN'
            if event.key == pygame.K_s:
                changeto = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.evet.Event(pygame.QUIT))
    # hướng đi
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    #cập nhật vị trí:
    if direction == 'RIGHT':
        snakepos[0] +=m
    if direction == 'LEFT':
        snakepos[0] -=m
    if direction == 'UP':
        snakepos[1] +=m
    if direction == 'DOWN':
        snakepos[1] -=m
    #Cơ chế thêm khúc dài ra:
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score +=1
        foodflat =False
    else:
        snakebody.pop()
    #Sản sinh phuhungngu:
    if foodflat == False:
        foodx = random.randrange(1,128)
        foody = random.randrange(1,70) 
        if foodx %2 != 0: foodx +=1
        if foody %2 != 0: foody +=1
        foodpos = [foodx * 10 , foody * 10 ]
    foodflat = True
    #background(cập nhật lên cửa sổ):
    gameSurface.fill(white)
    for pos in snakebody:
        gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))
    gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m))
    gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))
    #Xử lý di chuyển đụng 4 cạnh biện:
    if snakepos[0] > 1200 or snakepos[0] < 10:
        game_over()
    if snakepos[1] > 680 or snakepos[1] < 10:
        game_over()
    #Xử lý tự ăn chính mình:
    for b in snakebody[1:]:
        if snakepos[0] == b[0] and snakepos[1] == b[1]:
            game_over()
    #Đường viền:
    pygame.draw.rect(gameSurface,red,(10,10,1280,700),2)
    show_score()
    pygame.display.flip() 