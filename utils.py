import pygame
import random

black = (0,0,0)
grey = (200,200,200)
white = (255,255,255)

screen_w = 1600 
screen_h = 900 
screen = pygame.display.set_mode((screen_w,screen_h))

#screen.fill(grey)

pygame.display.set_caption('Game of life')
def detect_click(cells):
    pos = pygame.mouse.get_pos()
    for x in range(len(cells[0])):
        for y in range(len(cells)):
            cells[y][x].clicked(pos)
        
def count_neighbours(cells,x,y):
    sum = 0
    len_x = len(cells[0])
    len_y = len(cells)

    # Define the relative positions of neighboring cells
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for dx, dy in neighbors:
        # Calculate the coordinates of the neighboring cell
        nx, ny = x + dx, y + dy

        # Check if the neighboring cell is within bounds
        if 0 <= nx < len_x and 0 <= ny < len_y:
            # Check if the neighboring cell is alive
            if cells[ny][nx].alive:
                sum += 1

    return sum


def next_generation(screen,cells):
    for y in range(len(cells)):
        for x in range(len(cells[0])):
            cnt = count_neighbours(cells,x,y)
            if cells[y][x].alive:
                if cnt < 2 and cells[y][x].alive:
                    # underpop
                    cells[y][x].alive_next_gen = False  
                elif cnt == 2 or cnt == 3:
                    # lives on
                    cells[y][x].alive_next_gen = True
                elif cnt > 3:
                    # overpop   
                    cells[y][x].alive_next_gen = False   
            else:
                if cnt == 3:
                    # reproduction
                    cells[y][x].alive_next_gen = True
    for y in range(len(cells)):
        for x in range(len(cells[0])):
            cells[y][x].alive = cells[y][x].alive_next_gen
            cells[y][x].draw(screen,cells[y][x].x,cells[y][x].y,cells[y][x].alive)

def randomize(cells):
    alive_prob = 0.1
    for y in range(len(cells)):
        for x in range(len(cells[0])):
            rand = random.uniform(0,1)
            if rand < alive_prob:
                cells[y][x].alive = True
            else:
                cells[y][x].alive = False
            cells[y][x].draw(screen,cells[y][x].x,cells[y][x].y,cells[y][x].alive)

def clear(cells):
    for y in range(len(cells)):
        for x in range(len(cells[0])):
            cells[y][x].alive = False
            cells[y][x].alive_next_gen = False
            cells[y][x].draw(screen,cells[y][x].x,cells[y][x].y,cells[y][x].alive)
