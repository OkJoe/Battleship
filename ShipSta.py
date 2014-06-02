import pygame, sys, Ship, Arm
from pygame.locals import *
pygame.init()
FPS = 10
turnr = .02
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

def addship(shiplist):
    level = 0
    while True:
        level = int(raw_input("please enter ship level"))
        if level <= 100 and level >= 0:
            break
        else:
            print "invalid level, please enter again"
    while True:
        name = raw_input("please enter a shipname")
        if name == 'Default':
            shiplist.append(Ship.ship())
            shiplist[-1].sta.level = level
            break
        elif name == 'Shimakaze':
            shiplist.append(Shimakaze())
            shiplist[-1].sta.level = level
            break
        elif name == 'Kongo':
            shiplist.append(Kongo())
            shiplist[-1].sta.level = level
            break
        else:
            print "no such ship found, please enter again"

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
        self.sta.color = (180, 180, 255)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level

class Kongo(Ship.ship):
    def reInit(self):
        self.sta.name = 'Kongo'
        self.sta.length = 222
        self.sta.propulsion = 150
        self.sta.evasion = 0.04
        self.sta.health = [82, 82, 82, 82, 82, 82, 82, 82]
        self.sta.armor = [94, 94, 94, 94, 94, 94, 94, 94]
        self.sta.weapon = [[Arm.cannon356(), Arm.cannon152(), Arm.cannon152(), Arm.torpedo553(), Arm.torpedo553(), Arm.torpedo553(), Arm.torpedo553()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152(), Arm.torpedo553(), Arm.torpedo553(), Arm.torpedo553(), Arm.torpedo553()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152()], [Arm.cannon356(), Arm.cannon152(), Arm.cannon152()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (255, 255, 0)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level

