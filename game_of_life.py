import pygame 
import time

from cell import * 
from utils import *

pygame.init()

class GameState:
    def __init__(self, state = 'paused', sim_delay = 0.1):
        self.state = state
        self.sim_delay = sim_delay

    def state_manager(self):
        if self.state == 'paused':
            self.paused()
        if self.state == 'running':
            self.running()

    def paused(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                detect_click(cells)
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
                    pygame.quit()
        time.sleep(0.01)
        pygame.display.update()

    def running(self):
        next_generation(screen,cells)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                detect_click(cells)
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
                    pygame.quit()
        time.sleep(self.sim_delay)
        pygame.display.update()

game = GameState()
while True:
    game.state_manager()
