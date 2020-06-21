import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

running = True


rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissor_img = pygame.image.load('scissor.png')
fonts = pygame.font.Font('freesansbold.ttf',50)
message = ''
button_presed = ''
second_font = pygame.font.Font('freesansbold.ttf',50)
def score():
	score_on_screen = fonts.render('Message : ' + message,True,(255,255,255))
	screen.blit(score_on_screen,(30,30))
def button():
	buttons = second_font.render('You pressed ' + button_presed,True,(255,255,255))
	screen.blit(buttons,(50,100))

def random_no():
	result = random.randint(1,3)
	return result

while running:
	screen.fill((25,21,35))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				final_result = random_no()
				button_presed = 'rock'
				button()
				if final_result == 1:
					message = 'draw'
				elif final_result == 2:
					message = 'You lost'
				elif final_result == 3:
					message = 'You win'
			if event.key == pygame.K_s:
				final_result = random_no()
				if final_result == 1:
					message = 'You win'
				elif final_result == 2:
					message = 'draw'
				elif final_result == 3:
					message = 'You lost'
			if event.key == pygame.K_d:
				final_result = random_no()
				if final_result == 1:
					message = 'You lost'
				elif final_result == 2:
					message = 'You win'
				elif final_result == 3:
					message = 'draw'


	screen.blit(rock_img,(100,300))
	screen.blit(paper_img,(300,300))
	screen.blit(scissor_img,(500,300))
	score()

	pygame.display.update()