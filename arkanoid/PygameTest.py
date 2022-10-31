# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# creating a running loop
while True:

    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:

            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                print("Key A has been pressed")

            # checking if key "J" was pressed
            if event.key == pygame.K_j:
                print("Key J has been pressed")

            # checking if key "P" was pressed
            if event.key == pygame.K_p:
                print("Key P has been pressed")

            # checking if key "M" was pressed
            if event.key == pygame.K_m:
                print("Key M has been pressed")