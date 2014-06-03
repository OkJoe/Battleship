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
        if level <= 200 and level >= 0:
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
        elif name == 'Fletcher':
            shiplist.append(Fletcher())
            shiplist[-1].sta.level = level
            break
        elif name == 'Kongo':
            shiplist.append(Kongo())
            shiplist[-1].sta.level = level
            break
        elif name == 'Bismarck':
            shiplist.append(Bismarck())
            shiplist[-1].sta.level = level
            break
        elif name == 'NorthCarolina':
            shiplist.append(NorthCarolina())
            shiplist[-1].sta.level = level
            break
        elif name == 'Iowa':
            shiplist.append(Iowa())
            shiplist[-1].sta.level = level
            break
        elif name == 'Yamato':
            shiplist.append(Yamato())
            shiplist[-1].sta.level = level
            break
        elif name == 'Soyuz':
            shiplist.append(Soyuz())
            shiplist[-1].sta.level = level
            break
        elif name == 'G3':
            shiplist.append(G3())
            shiplist[-1].sta.level = level
            break
        elif name == 'Richelieu':
            shiplist.append(Richelieu())
            shiplist[-1].sta.level = level
            break
        else:
            print "no such ship found, please enter again"

class Shimakaze(Ship.ship):
    def reInit(self):
        self.sta.name = 'Shimakaze'
        self.sta.length = 130
        self.sta.propulsion = 205
        self.sta.evasion = 0.08
        self.sta.health = [36, 36, 36, 36, 36, 36, 36, 36]
        self.sta.armor = [59, 59, 59, 59, 59, 59, 59, 59]
        self.sta.weapon = [[Arm.cannon460(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610()], [Arm.cannon460()], [], [Arm.cannon460()], [Arm.cannon460(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610()], [Arm.cannon460()], [], [Arm.cannon460()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (255, 200, 200)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level

class Fletcher(Ship.ship):
    def reInit(self):
        self.sta.name = 'Fletcher'
        self.sta.length = 115
        self.sta.propulsion = 180
        self.sta.evasion = 0.1
        self.sta.health = [30, 30, 30, 30, 30, 30, 30, 30]
        self.sta.armor = [50, 50, 50, 50, 50, 50, 50, 50]
        self.sta.weapon = [[Arm.cannon460(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610()], [Arm.cannon460()], [], [Arm.cannon460()], [Arm.cannon460(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610(), Arm.torpedo610()], [Arm.cannon460()], [], [Arm.cannon460()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (128, 128, 255)
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
        self.sta.color = (255, 200, 200)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level

class Bismarck(Ship.ship):
    def reInit(self):
        self.sta.name = 'Bismark'
        self.sta.length = 250
        self.sta.propulsion = 175
        self.sta.evasion = 0.04
        self.sta.health = [96, 96, 96, 96, 96, 96, 96, 96]
        self.sta.armor = [100, 90, 90, 100, 100, 90, 90, 100]
        self.sta.weapon = [[Arm.cannon380(), Arm.cannon150(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()],[Arm.cannon380(), Arm.cannon150(), Arm.cannon150(), Arm.cannon105(), Arm.cannon105()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (128, 128, 128)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level
                
class NorthCarolina(Ship.ship):
    def reInit(self):
        self.sta.name = 'NorthCarolina'
        self.sta.length = 222
        self.sta.propulsion = 140
        self.sta.evasion = 0.04
        self.sta.health = [80, 80, 80, 80, 80, 80, 80, 80]
        self.sta.armor = [95, 95, 95, 95, 95, 95, 95, 95]
        self.sta.weapon = [[Arm.cannon410(), Arm.cannon410(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon130(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon130(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon410(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon130(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon130(), Arm.cannon130()],[Arm.cannon410(), Arm.cannon130(), Arm.cannon130(), Arm.cannon130()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (128, 128, 255)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level
                
class Iowa(Ship.ship):
    def reInit(self):
        self.sta.name = 'Iowa'
        self.sta.length = 263
        self.sta.propulsion = 163
        self.sta.evasion = 0.04
        self.sta.health = [100, 100, 100, 100, 100, 100, 100, 100]
        self.sta.armor = [100, 100, 100, 100, 100, 100, 100, 100]
        self.sta.weapon = [[Arm.cannon406(), Arm.cannon406(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon127(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon127(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon406(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon127(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon406(), Arm.cannon127(), Arm.cannon127(), Arm.cannon127()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (128, 128, 255)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level

class Yamato(Ship.ship):
    def reInit(self):
        self.sta.name = 'Yamato'
        self.sta.length = 263
        self.sta.propulsion = 135
        self.sta.evasion = 0.04
        self.sta.health = [130, 130, 130, 130, 130, 130, 130, 130]
        self.sta.armor = [130, 130, 130, 130, 130, 130, 130, 130]
        self.sta.weapon = [[Arm.cannon460(), Arm.cannon460(), Arm.cannon155(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon155(), Arm.cannon155(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon155(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon155(), Arm.cannon155(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon460(), Arm.cannon155(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon155(), Arm.cannon155(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon155(), Arm.cannon127(), Arm.cannon127()],[Arm.cannon460(), Arm.cannon155(), Arm.cannon155(), Arm.cannon127(), Arm.cannon127()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (255, 200, 200)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level

class Soyuz(Ship.ship):
    def reInit(self):
        self.sta.name = 'Soyuz'
        self.sta.length = 269
        self.sta.propulsion = 140
        self.sta.evasion = 0.04
        self.sta.health = [130, 130, 130, 130, 130, 130, 130, 130]
        self.sta.armor = [130, 130, 130, 130, 130, 130, 130, 130]
        self.sta.weapon = [[Arm.cannon406(), Arm.cannon406(), Arm.cannon152(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon406(), Arm.cannon152(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (255, 0, 0)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level
                
class G3(Ship.ship):
    def reInit(self):
        self.sta.name = 'G3'
        self.sta.length = 261
        self.sta.propulsion = 160
        self.sta.evasion = 0.04
        self.sta.health = [115, 115, 115, 115, 115, 115, 115, 115]
        self.sta.armor = [115, 115, 115, 115, 115, 115, 115, 115]
        self.sta.weapon =[[Arm.cannon406(), Arm.cannon406(), Arm.cannon152(), Arm.cannon152()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon120()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon120()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon120()],[Arm.cannon406(), Arm.cannon406(), Arm.cannon152(), Arm.cannon152()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon120()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon120()],[Arm.cannon406(), Arm.cannon152(), Arm.cannon152(), Arm.cannon120()]]
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

class Richelieu(Ship.ship):
    def reInit(self):
        self.sta.name = 'Richlieu'
        self.sta.length = 248
        self.sta.propulsion = 150
        self.sta.evasion = 0.04
        self.sta.health = [100, 100, 100, 100, 100, 100, 100, 100]
        self.sta.armor = [100, 100, 100, 100, 100, 100, 100, 100]
        self.sta.weapon = [[Arm.cannon380(), Arm.cannon152(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()],[Arm.cannon380(), Arm.cannon152(), Arm.cannon100(), Arm.cannon100(), Arm.cannon100()]]
        self.sta.block = [Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block(), Ship.block()]
        self.sta.color = (0, 0, 0)
        for i in range(0, 8):
            self.sta.block[i].number = i
            self.sta.block[i].init(self.sta)
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level
