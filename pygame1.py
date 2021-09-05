import pygame
pygame.init()
pygame.display.set_caption("The wonderful life of Woody")
screen = pygame.display.set_mode((560,272))
walkRight = [pygame.image.load('R_1.png'),pygame.image.load('R_2.png'),pygame.image.load('R_3.png'),pygame.image.load('R_4.png'),pygame.image.load('R_5.png'),pygame.image.load('R_6.png')]
walkLeft = [pygame.image.load('L_1.png'),pygame.image.load('L_2.png'),pygame.image.load('L_3.png'),pygame.image.load('L_4.png'),pygame.image.load('L_5.png'),pygame.image.load('L_6.png')]
jumpRight = [pygame.image.load('JUMP_R_1.png'),pygame.image.load('JUMP_R_2.png'),pygame.image.load('JUMP_R_3.png'),pygame.image.load('JUMP_R_4.png'),pygame.image.load('JUMP_R_5.png'),pygame.image.load('JUMP_R_6.png')]
jumpLeft = [pygame.image.load('JUMP_L_1.png'),pygame.image.load('JUMP_L_2.png'),pygame.image.load('JUMP_L_3.png'),pygame.image.load('JUMP_L_4.png'),pygame.image.load('JUMP_L_5.png'),pygame.image.load('JUMP_L_6.png')]
runRight = [pygame.image.load('RUN_R_1.png'),pygame.image.load('RUN_R_2.png'),pygame.image.load('RUN_R_3.png'),pygame.image.load('RUN_R_4.png'),pygame.image.load('RUN_R_5.png'),pygame.image.load('RUN_R_6.png')]
runLeft = [pygame.image.load('RUN_L_1.png'),pygame.image.load('RUN_L_2.png'),pygame.image.load('RUN_L_3.png'),pygame.image.load('RUN_L_4.png'),pygame.image.load('RUN_L_5.png'),pygame.image.load('RUN_L_6.png')]

bg = pygame.image.load('background.gif')
char = [pygame.image.load('IDLE_1.PNG'),pygame.image.load('IDLE_2.PNG'),pygame.image.load('IDLE_3.PNG'),pygame.image.load('IDLE_4.PNG')]
clock = pygame.time.Clock()
class Player:
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.velo=60*1/60
		self.isjump=False
		self.jumpCount=10
		self.left=False
		self.right=False
		self.walkCount= 0
		self.isrun = False
		self.runCount=0
		self.idleCount=0
	def draw(self,screen):
		if self.isrun == False:
			if self.walkCount >= 20:
				self.walkCount=0
			if self.idleCount >= 30:
				self.idleCount=0
			if self.left and self.isjump==False:
				screen.blit(walkLeft[self.walkCount//4],(self.x,self.y))
				self.walkCount+=1
			elif self.right and self.isjump==False:
				screen.blit(walkRight[self.walkCount//4],(self.x,self.y))
				self.walkCount+=1
			elif self.right and self.isjump:
				screen.blit(jumpRight[abs(self.jumpCount-10)//4],(self.x,self.y))
			elif self.left and self.isjump:
				screen.blit(jumpLeft[abs(self.jumpCount-10)//4],(self.x,self.y)) 
			else:
				screen.blit(char[self.idleCount//10],(self.x,self.y))
				self.idleCount+=1
		if self.isrun:
			if self.runCount >= 20:
				self.runCount=0			
			if self.idleCount >= 30:
				self.idleCount=0
			elif self.left and self.isrun:
				screen.blit(runLeft[self.runCount//4],(self.x,self.y))
				self.runCount += 1				
			elif self.right and self.isrun:
				screen.blit(runRight[self.runCount//4],(self.x,self.y))
				self.runCount += 1	
			else:
				screen.blit(char[self.idleCount//10],(self.x,self.y))
				self.idleCount+=1
james=Player(10,210,48,48)
running = True
def redraw_game_window():
	screen.blit(bg, (0,0))
	james.draw(screen)
	pygame.display.update()
while running:
	clock.tick(60)
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and james.x>0:
		if keys[pygame.K_LSHIFT]:
			james.x -= james.velo * 1.5
			james.isrun=True
		else:
			james.x -= james.velo
			james.isrun = False
		james.left = True
		james.right = False
	elif keys[pygame.K_RIGHT] and james.x<560-james.width-james.velo:
		if keys[pygame.K_LSHIFT]:
			james.x += james.velo * 1.5
			james.isrun=True
		else:
			james.x += james.velo
			james.isrun = False
		james.left = False
		james.right = True
	else:
		james.right = False
		james.left = False
		james.walkCount = 0
		james.runCount = 0
	if not james.isjump:
		if keys[pygame.K_SPACE]:
				james.isjump = True
				james.left = False#de y cai nay sao nay nghich them
				james.right = False
	if james.isjump:
		if james.jumpCount >= -10:
			james.y -= (james.jumpCount * abs(james.jumpCount)) * 0.1
			james.jumpCount -= 1
		else:
			james.isjump = False	
			james.jumpCount = 10
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			print("Hello world")
	redraw_game_window()
pygame.quit()
