import pygame
pygame.init()
pygame.display.set_caption("first step")
screen = pygame.display.set_mode((560,272))
walkRight = [pygame.image.load('R_1.png'),pygame.image.load('R_2.png'),pygame.image.load('R_3.png'),pygame.image.load('R_4.png'),pygame.image.load('R_5.png'),pygame.image.load('R_6.png')]
walkLeft = [pygame.image.load('L_1.png'),pygame.image.load('L_2.png'),pygame.image.load('L_3.png'),pygame.image.load('L_4.png'),pygame.image.load('L_5.png'),pygame.image.load('L_6.png')]
jumpRight = [pygame.image.load('JUMP_R_1.png'),pygame.image.load('JUMP_R_2.png'),pygame.image.load('JUMP_R_3.png'),pygame.image.load('JUMP_R_4.png'),pygame.image.load('JUMP_R_5.png'),pygame.image.load('JUMP_R_6.png')]
jumpLeft = [pygame.image.load('JUMP_L_1.png'),pygame.image.load('JUMP_L_2.png'),pygame.image.load('JUMP_L_3.png'),pygame.image.load('JUMP_L_4.png'),pygame.image.load('JUMP_L_5.png'),pygame.image.load('JUMP_L_6.png')]
bg = pygame.image.load('background.gif')
char = pygame.image.load('char.png')
clock = pygame.time.Clock()
class Player:
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.velo=5
		self.isjump=False
		self.jumpCount=10
		self.left=False
		self.right=False
		self.walkCount= 0
	def draw(self,screen):
		if self.walkCount >= 20:
			self.walkCount=0
		if self.walkCount 




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
			screen.blit(char,(self.x,self.y))


james=Player(0,210,48,48)
running = True
def redraw_game_window():
	screen.blit(bg, (0,0))
	james.draw(screen)
	pygame.display.update()
while running:
	clock.tick(20)
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and james.x>0:
		james.x -= james.velo
		james.left = True
		james.right = False
	elif keys[pygame.K_RIGHT] and james.x<560-james.width-james.velo:
		james.x += james.velo
		james.left = False
		james.right = True
	else:
		james.right = False
		james.left = False
		james.walkCount = 0
	if not james.isjump:
		if keys[pygame.K_SPACE]:
				james.isjump = True
				james.left = False
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