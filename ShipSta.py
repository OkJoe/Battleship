import pygame, sys, Ship, Arm
from pygame.locals import *
pygame.init()
FPS = 10
turnr = .02
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

class Shimakaze(Ship.ship):
    def reInit(self):
        self.sta.name = 'Shimakaze'
        self.sta.length = 130
        self.sta.propulsion = 205
        self.sta.evasion = 0.1
        self.sta.health = [36, 36, 36, 36, 36, 36, 36, 36]
        self.sta.armor = [59, 59, 59, 59, 59, 59, 59, 59]
        self.sta.weapon = [[Arm.cannon127(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610()], [Arm.cannon127()], [], [Arm.cannon127()], [Arm.cannon127(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610()], [Arm.cannon127()], [], [Arm.cannon127()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (200, 200, 255)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
