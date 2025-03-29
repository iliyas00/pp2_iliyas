import pygame
import datetime
import math

pygame.init()
screen = pygame.display.set_mode((1200, 800))
width, height = 1200 // 2, 800 // 2
done = False
image = pygame.image.load(r'C:\Users\izhek\Desktop\python_works\pp2_iliyas\Lab_7\mainclock.png')
sec = pygame.image.load(r'C:\Users\izhek\Desktop\python_works\pp2_iliyas\Lab_7\leftarm.png')
mik_sec = sec.get_rect(center=(width, height))
minute=pygame.image.load(r'C:\Users\izhek\Desktop\python_works\pp2_iliyas\Lab_7\rightarm.png')
mik_min=minute.get_rect(center=(width, height))
mik_rec = image.get_rect(center=(width, height))
font = pygame.font.SysFont('Micky', 100)
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    time = datetime.datetime.now()
    time_render = font.render(time.strftime("%H:%M:%S"), True, pygame.Color('blue'), pygame.Color('orange')) #true для глаживания текста
    screen.blit(image, mik_rec)
    screen.blit(time_render, (10, 10))
    
    # Calculate the angle for the second hand
    angle = (time.second / 60) * 360
    
    # Rotate the second hand image
    rotated_image = pygame.transform.rotate(sec, -angle) #минус это чтоб по часовой
    
    # Get the rect of the rotated image and center it
    rotated_rect = rotated_image.get_rect(center=mik_sec.center)
    
    # Blit the rotated image onto the screen
    screen.blit(rotated_image, rotated_rect)
    minute_angle = ((time.minute + time.second / 60) / 60) * 360
    rotated_minute = pygame.transform.rotate(minute, -minute_angle)
    
    # Get the rect of the rotated minute hand image and center it
    rotated_minute_rect = rotated_minute.get_rect(center=mik_min.center)
    
    # Blit the rotated minute hand image onto the screen
    screen.blit(rotated_minute, rotated_minute_rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()