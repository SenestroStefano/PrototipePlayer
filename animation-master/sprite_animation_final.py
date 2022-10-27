import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		path = "../animation/Rana/"
		self.sprites = []
		
		value = 4
		
		for i in range(9):
			img = pygame.image.load(path + 'attack_'+str(i+1)+'.png')
			img = pygame.transform.scale(img, (img.get_width()*value, img.get_height()*value))
			self.sprites.append(img)

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False
				
		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 900
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(screen_width/2-150, screen_height/2-250)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.attack()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)