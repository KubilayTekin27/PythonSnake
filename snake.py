import pygame,sys,random,string
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SNAKEGAMES")

background = pygame.image.load("./black.jpg")
pygame.display.update()
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))


class snakeparts :

    def __init__(self,x,y,k,color):
        self.x= x
        self.y = y
        self.k = k
        self.color= color

    def drowhead(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.k,self.k])

    def drowbody(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.k,self.k])


snakehead = snakeparts(200,60,20,(20,20,250))
body1 =snakeparts(180,60,20,(60,60,200))
body2 =snakeparts(160,60,20,(60,60,200))
body3 =snakeparts(140,60,20,(60,60,200))
body4 =snakeparts(120,60,20,(60,60,200))
headartısy=0
headartısx=20
fps = pygame.time.Clock()
parca_lıst=[snakehead,body1,body2,body3,body4]
#APPLE CREATE
applex = random.randint(0,39)*20
appley =random.randint(0,29)*20
apple = snakeparts(applex,appley,20,(255,31,31))

while True:
    screen.blit(background , (0 , 0))
    fps.tick(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP and headartısy !=20 :
                headartısx= 0
                headartısy = -20
            if event.key == pygame.K_DOWN and headartısy !=-20 :
                headartısy= 20
                headartısx =0
            if event.key==pygame.K_RIGHT and headartısx !=-20:
                headartısx=20
                headartısy=0
            if event.key==pygame.K_LEFT  and headartısx!=20 :
                headartısx= -20
                headartısy = 0
    snakehead.x += headartısx
    snakehead.y += headartısy
    def sınırlar ():
        if snakehead.x >780:
            snakehead.x = 0
        elif snakehead.x <0:
            snakehead.x = 800
        if snakehead.y >580:
            snakehead.y = 0
        elif snakehead.y <0:
            snakehead.y = 600


    sınırlar()
    apple.drowbody()

    i = len(parca_lıst)-1


    snakehead.drowhead()
    sayac = 1

    while sayac < len(parca_lıst):
        parca_lıst[i].drowbody()
        parca_lıst[i].x=parca_lıst[i-1].x
        parca_lıst[i].y =parca_lıst[i-1].y

        i -= 1
        sayac+=1

    #EAT APPLE

    if snakehead.x == apple.x and snakehead.y == apple.y :
        randomapplex = random.randint(0,39) * 20
        randomappley = random.randint(0,29) * 20
        apple.x = randomapplex
        apple.y = randomappley
        newpart = get_random_string(8)
        newpart = snakeparts(900,700,20,(60,60,200))
        parca_lıst.append(newpart)
    # SCORE

    font = pygame.font.Font('freesansbold.ttf', 20)
    textx = 40
    texty = 40
    # OYUNU KAYBETME

    def showscore(x, y):
        score = font.render("score :" + str(len(parca_lıst)-5), True, (255,255,255))
        screen.blit(score, (x, y))
    showscore(0,0)
    pygame.display.update()

