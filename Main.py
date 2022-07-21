import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
height = 700
width = 934

platform_1_direction = 0	#платформа игрока
platform_1_x = 25			#
platform_1_y = height // 2	#

platform_2_direction = 0		#платформа бота
platform_2_x = width - 25 - 25	#
platform_2_y = height // 2		#

ball_x_cur = width // 2		#текущая x шара
ball_y_cur = height // 2	#текущая y шара

speed_x = 10	#x скорость шара
speed_y = 2		#y скорость шара

score_1 = 0		#счет игрока
score_2 = 0		#счет бота

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
screen.fill(BLACK)

num_0 = pygame.image.load("Images/0.png")
num_1 = pygame.image.load("Images/1.png")
num_2 = pygame.image.load("Images/2.png")
num_3 = pygame.image.load("Images/3.png")
num_4 = pygame.image.load("Images/4.png")
num_5 = pygame.image.load("Images/5.png")
num_6 = pygame.image.load("Images/6.png")
num_7 = pygame.image.load("Images/7.png")
num_8 = pygame.image.load("Images/8.png")
num_9 = pygame.image.load("Images/9.png")

pygame.display.update()

def draw_screen():
	screen.fill(BLACK)

	set_number(score_1, 0)
	set_number(score_2, 1)

	for i in range(10, height, 50):			#линия по середине
		pygame.draw.rect(screen, WHITE, [width//2-5, i*2, 10, 50])
	
	pygame.draw.rect(screen, WHITE, [platform_1_x, platform_1_y, 25, 150])	#платформа игрока
	pygame.draw.rect(screen, WHITE, [platform_2_x, platform_2_y, 25, 150])	#платформа бота

	pygame.draw.circle(screen, WHITE, (ball_x_cur, ball_y_cur), 16)		#шарик
	pygame.draw.circle(screen, BLACK, (ball_x_cur, ball_y_cur), 16, 3)	#обводка шарика

	pygame.display.update()	#обновить экран

def set_number(number, pos):
	if pos == 0:
		number_position = width//2-150
	elif pos == 1:
		number_position = width//2+50

	if number == 0:
		screen.blit(num_0, (number_position, 10))
	elif number == 1:
		screen.blit(num_1, (number_position, 10))
	elif number == 2:
		screen.blit(num_2, (number_position, 10))
	elif number == 3:
		screen.blit(num_3, (number_position, 10))
	elif number == 4:
		screen.blit(num_4, (number_position, 10))
	elif number == 5:
		screen.blit(num_5, (number_position, 10))
	elif number == 6:
		screen.blit(num_6, (number_position, 10))
	elif number == 7:
		screen.blit(num_7, (number_position, 10))
	elif number == 8:
		screen.blit(num_8, (number_position, 10))
	elif number == 9:
		screen.blit(num_9, (number_position, 10))

done = True
ball_move = False

while done:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			done = False
		elif i.type == pygame.KEYDOWN:
			ball_move = True
			if i.key == pygame.K_w:
				platform_1_direction = 1

			elif i.key == pygame.K_s:
				platform_1_direction = -1

		elif i.type == pygame.KEYUP:
			platform_1_direction = 0

	draw_screen()

#-------------------- Платформы --------------------
#---------- Платформа игрока----------
	if platform_1_direction == 1:
		platform_1_y -= 5
	elif platform_1_direction == -1:
		platform_1_y += 5

	if platform_1_y <= 0:
		platform_1_direction = 0
	elif platform_1_y >= height-150:
		platform_1_direction = 0
#---------- Платформа игрока ----------

#---------- Платформа бота ----------
	if platform_2_y + 75 > ball_y_cur + 5:
		platform_2_direction = 1
	elif platform_2_y + 75 < ball_y_cur - 5 :
		platform_2_direction = -1
	elif platform_2_y + 75 == ball_y_cur:
		platform_2_direction = 0
#---------- Платформа бота ----------

#---------- Платформа бота ----------
	if platform_2_direction == 1:
		platform_2_y -= 5
	elif platform_2_direction == -1:
		platform_2_y += 5

	if platform_2_y <= 0:
		platform_2_y += 5
		platform_2_direction = 0
	elif platform_2_y >= height-150:
		platform_2_y -= 5
		platform_2_direction = 0
#---------- Платформа бота ----------
#-------------------- Платформы --------------------

#-------------------- Шар --------------------
#---------- Полет шара ----------
	if ball_move == True:
		ball_x_cur += speed_x
		ball_y_cur += speed_y
#---------- Полет шара ----------

#---------- Столкновения шара ----------
	if ball_x_cur >= width-8 and ball_x_cur <= width-4:		#при столкновении с правой границей
		score_1 += 1
		ball_x_cur = width // 2
		ball_y_cur = height // 2
		ball_move = False

	if ball_x_cur >= 4 and ball_x_cur <= 8:		#при столкновении с левой границей
		score_2 += 1
		ball_x_cur = width // 2
		ball_y_cur = height // 2
		ball_move = False

	if ball_y_cur > platform_1_y and ball_y_cur < platform_1_y+150 and ball_x_cur <= platform_1_x+25+8:	#столкновение с платформой игрока
		speed_x /= -1
		speed_y = random.randint(-5, 5)

	if ball_y_cur > platform_2_y and ball_y_cur < platform_2_y+150 and ball_x_cur >= platform_2_x-8:	#столкновение с платформой бота
		speed_x /= -1
		speed_y = random.randint(-5, 5)

	if ball_y_cur > height-8:	#при столкновении с нижней границей
		speed_y /= -1
	if ball_y_cur < 8:			#при столкновении с верхней границей
		speed_y /= -1
#---------- Столкновения шара ----------
#-------------------- Шар --------------------

#---------- Обнуление счетчиков ----------
	if score_1 > 9:
		score_1 = 0
		# if speed_x > 0:	#на будующее __увеличение сложности__
		# 	speed_x += 2
		# else:
		# 	speed_x -= 2
	if score_2 > 9:
		score_2 = 0
#---------- Обнуление счетчиков ----------

	clock.tick(60)
pygame.quit()
