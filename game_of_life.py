import pygame 
import time

from cell import * 
from utils import *

pygame.init()

pygame.display.set_caption('Game of life')

cells = [[]]

init_cells(cells)

class GameState:
    def __init__(self, state = 'paused', quit = False, sim_delay = 0.05, last_time = time.time(),last_pos = (0,0)):
        self.state = state
        self.quit = quit
        self.sim_delay = sim_delay
        self.last_time = last_time
        self.last_pos = last_pos

    def state_manager(self):
        if self.state == 'paused':
            self.paused()
        if self.state == 'running':
            self.running()

    def paint_cells(self):
        pos = pygame.mouse.get_pos()
        pos_x = pos[0]//cell_size
        pos_y = pos[1]//cell_size
        last_pos_x = self.last_pos[0]//cell_size 
        last_pos_y = self.last_pos[1]//cell_size
        keyboard = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0] and keyboard[pygame.K_LSHIFT] and not (pos_x == last_pos_x and pos_y == last_pos_y): 
            cells[pos_y][pos_x].kill(pos)
            self.last_pos = pos

        elif pygame.mouse.get_pressed()[0] and not (pos_x == last_pos_x and pos_y == last_pos_y):
            cells[pos_y][pos_x].spawn(pos)
            self.last_pos = pos

    def paused(self):
        self.paint_cells()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'running'
                    print("STATE: RUNNING")
                if event.key == pygame.K_LEFT:
                    delay *= 1.5 
                if event.key == pygame.K_RIGHT:
                    delay *= 0.5   
                if event.key == pygame.K_r:
                    randomize(cells)
                if event.key == pygame.K_c:
                    clear(cells)
                if event.key == pygame.K_q:
                    self.quit = True
        time.sleep(0.02)
        pygame.display.update()

    def running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'paused'
                    print("STATE: PAUSED")
                if event.key == pygame.K_LEFT:
                    self.sim_delay *= 1.5 
                    print("DELAY:",self.sim_delay)
                if event.key == pygame.K_RIGHT:
                    self.sim_delay *= 0.5   
                    print("DELAY:",self.sim_delay)
                if event.key == pygame.K_r:
                    clear(cells)
                    randomize(cells)
                if event.key == pygame.K_q:
                    self.quit = True
        time.sleep(0.02)
        if time.time() - self.last_time > self.sim_delay:
            next_generation(screen,cells)
            self.last_time = time.time()
            pygame.display.update()
            return True

game = GameState()
while not game.quit:
    game.state_manager()

