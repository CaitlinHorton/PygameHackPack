import pygame
from pygame.locals import*
import random

pygame.init()

width = 1200
height = 800
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4

speed = 2
level = 1

screen = pygame.display.set_mode((width, height)) # Set the size of the screen

# Load the cars
car = pygame.image.load("CarGame/car1.png") # https://helloartsy.com/how-to-draw-a-car-from-the-top/
car_loc = car.get_rect()
car_loc.center = left_lane, height*0.8

# Enemy
car2 = pygame.image.load("CarGame/car2.png") # https://pngtree.com/freepng/car-view-from-above-icon-object-web-design-above-vector_10530579.html
car2_loc = car.get_rect()
car2_loc.center = right_lane, height*0.2

pygame.display.update()

counter = 0
run = True
while run:

    # Increase difficuilty
    # Counter is how often it changes. Speed is how quickly it will start to go
    counter += 1
    if counter == 2500:
        speed += 0.25
        level += 1
        counter = 0
        print("Level Up!", level)

    # Make the enemy car move
    car2_loc[1] += speed
    if car2_loc[1] > height: # Makes sure that it runs in a loop
        # Make it change lanes randomly off screen
        if random.randint(0,1)==0:
            car2_loc.center = right_lane, -150
        else:
            car2_loc.center = left_lane, -150

    # End game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1]-200: # Removing the 250 allows for the game to end when the edges touch - not when the centers touch
        print("GAME OVER")
        break
    # Events
    for event in pygame.event.get():
        # If the exit button is clicked - exit
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            # Move Left
            if event.key in [K_a, K_LEFT]:
                if car_loc[0]-road_w/2> road_w/4: # Restriction
                    car_loc = car_loc.move([-int(road_w/2),0])
            if event.key in [K_s, K_RIGHT]:
                car_loc.center = car_loc.center = right_lane, height*0.8 # Restriction
                # car_loc = car_loc.move([int(road_w/2),0]) # this will just move it right without restrictions

    screen.fill((60, 220, 0)) # Set the background colour to green
    # Draw Road - draw it in the loop so that the cars don't duplicate
    pygame.draw.rect(screen,(50,50,50),(width/2 - road_w/2 , 0, road_w, height)) # Draw the grey part
    pygame.draw.rect(screen, (255, 240, 60), (width/2-roadmark_w/2 , 0, roadmark_w, height)) # Draw the yellow line
    pygame.draw.rect(screen, (255, 255, 255), (width/2-road_w/2+roadmark_w , 0, roadmark_w, height)) # Draw the left white line
    pygame.draw.rect(screen, (255, 255, 255), (width/2+road_w/2-2*roadmark_w , 0, roadmark_w, height)) # Draw the right white line

    
    screen.blit(car, car_loc) # for loading images - image, location
    screen.blit(car2, car2_loc)
    pygame.display.update()



pygame.quit()