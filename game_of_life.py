import pygame 
import time

from cell import * 
from utils import *

pygame.init()

pygame.display.set_caption('Game of life')

cells = [[]]

init_cells(cells)

class GameState:
    def __init__(self, state = 'paused', sim_delay = 0.5, quit = False, last_time = time.time()):
        self.state = state
        self.sim_delay = sim_delay
        self.quit = quit
        self.last_time = last_time

    def state_manager(self):
        cur_time = time.time()
        if self.state == 'paused':
            self.paused()
        if self.state == 'running':
            self.running(cur_time, self.last_time)

    def paused(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//20][pos[0]//20].clicked(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'running'
                    print("STATE: RUNNING")
                if event.key == pygame.K_LEFT:
                    delay += 1.5 
                if event.key == pygame.K_RIGHT:
                    delay += 0.5   
                if event.key == pygame.K_r:
                    randomize(cells)
                if event.key == pygame.K_c:
                    clear(cells)
                if event.key == pygame.K_q:
                    self.quit = True
        time.sleep(0.01)
        pygame.display.update()

    def running(self, cur_time, last_time):
        if cur_time - last_time > self.sim_delay:
            next_generation(screen,cells)
            rendered = True
            self.last_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
                #detect_click(cells)
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
        time.sleep(0.01)
        pygame.display.update()

game = GameState()
while not game.quit:
    game.state_manager()

