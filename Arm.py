import pygame, sys, math, random
from pygame.locals import *
pygame.init()
FPS = 10
turnr = .02
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

def vadd(mag1, mag2, ang1, ang2, magOrAng):
    magx = mag1 * math.cos(ang1) + mag2 * math.cos(ang2)
    magy = mag1 * math.sin(ang1) + mag2 * math.sin(ang2)
    if magOrAng == 'mag':
        return int(math.sqrt(magx * magx + magy * magy))
    if magOrAng == 'ang':
        return math.atan2(magy, magx)

class weapon:
    typ = str()
    r = int()
    harm = int()
    harmr = int()
    addtime = int()
    fixedtime = int()
    
    def __init__(self):
        self.typ = ''
        self.r = 4999
        self.harm = 0
        self.harmr = 0
        self.addtime = 0
        self.fixedtime = 0

class cannon(weapon):
    rmin = float()
    rmax = float()
    
    def __init__(self):
        self.typ = 'cannon'
        self.rmin = 0
        self.rmax = 0
        self.r = 4999
        self.harm = 20
        self.harmr = 100
        self.addtime = 0
        self.fixedtime = 50

    def init(self, number):
        if number == 0:
            self.rmin = - math.pi / 6
            self.rmax = 3 * math.pi / 4
        elif number == 1 or number == 2:
            self.rmin = math.pi / 4
            self.rmax = 3 * math.pi / 4
        elif number == 3:
            self.rmin = math.pi / 4
            self.rmax = 7 * math.pi / 6
        elif number == 7:
            self.rmin = 5 * math.pi / 6
            self.rmax = 7 * math.pi / 4
        elif number == 5 or number == 6:
            self.rmin = 5 * math.pi / 4
            self.rmax = 7 * math.pi / 4
        elif number == 4:
            self.rmin = 5 * math.pi / 4
            self.rmax = math.pi / 6
       
    def fire(self, shipS, shipE):
        if self.addtime == 0:
            d = math.sqrt((min((shipS.x - shipE.x) % 10000, (shipE.x - shipS.x) % 10000)) ** 2 + (min((shipS.y - shipE.y) % 10000, (shipE.y - shipS.y) % 10000)) ** 2)
            if d < self.r:
                x = shipS.x - shipE.x
                y = shipS.y - shipE.y
                if x < -5000:
                    x += 10000
                elif x > 5000:
                    x -= 10000
                if y < -5000:
                    y += 10000
                elif y > 5000:
                    y -= 10000
                posAngel = (math.atan2(y, x) - shipS.theta) % (2 * math.pi)
                if (posAngel - self.rmin) % (2 * math.pi) <= (self.rmax - self.rmin) % (2 * math.pi):
                    angel = float()
                    angel = random.randint(0, 360) * 2 * math.pi / 360
                    pos = random.randint(0, int(d / 10))
                    shipE.hitten(self, int(pos * math.cos(angel)), int(pos * math.sin(angel)))
                    self.addtime = self.fixedtime
                    
class cannon100(cannon):
    def reInit(self):
        self.harm = 35
        self.fixedtime = 50

class cannon105(cannon):
    def reInit(self):
        self.harm = 40
        self.fixedtime = 60

class cannon120(cannon):
    def reInit(self):
        self.harm = 45
        self.fixedtime = 70

class cannon127(cannon):
    def reInit(self):
        self.harm = 50
        self.fixedtime = 80

class cannon130(cannon):
    def reInit(self):
        self.harm = 55
        self.fixedtime = 80

class cannon150(cannon):
    def reInit(self):
        self.harm = 60
        self.fixedtime = 90

class cannon152(cannon):
    def reInit(self):
        self.harm = 60
        self.fixedtime = 100
        
class cannon155(cannon):
    def reInit(self):
        self.harm = 65
        self.fixedtime = 100

class cannon356(cannon):
    def reInit(self):
        self.harm = 100
        self.fixedtime = 200

class cannon380(cannon):
    def reInit(self):
        self.harm = 110
        self.fixedtime = 220
        
class cannon406(cannon):
    def reInit(self):
        self.harm = 125
        self.fixedtime = 230

class cannon410(cannon):
    def reInit(self):
        self.harm = 130
        self.fixedtime = 250

class cannon460(cannon):
    def reInit(self):
        self.harm = 150
        self.fixedtime = 255

class torpedoOb(weapon):
    x = int()
    y = int()
    v = int()
    vangel = float()
    r = int()
    state = bool()
    addtime = int()
    def __init__(self):
        self.typ = 'torpedoOb'
        self.x = 0
        self.y = 0
        self.v = 1000
        self.vangel = 0
        self.r = 0
        self.state = True
        self.addtime = 75
        self.harm = 0
        self.harmr = 300
        self.addtime = 0
        self.fixedtime = 0

    def init(self, x, y, theta, length):
        self.vangel = theta
        self.x = (x + math.cos(self.vangel) * length) % 10000
        self.y = (y + math.sin(self.vangel) * length) % 10000

    def control(self, DISPLAYSURF):
        self.addtime -= 1
        self.x = int(self.x + self.v * math.cos(self.vangel) / FPS) % 10000
        self.y = int(self.y + self.v * math.sin(self.vangel) / FPS) % 10000
        if self.addtime < 0:
            self.state = False
        pygame.draw.line(DISPLAYSURF, (255, 255, 255), (int(250 + (self.x - 10 * math.cos(self.vangel)) / 10), int(250 + (self.y - 10 * math.sin(self.vangel)) / 10)), (250 + int(self.x / 10), 250 + int(self.y / 10)), 3)

    def fire(self, ship):
        x = self.x - ship.x
        y = self.y - ship.y
        if x < -5000:
            x += 10000
        elif x > 5000:
            x -= 10000
        if y < -5000:
            y += 10000
        elif y > 5000:
            y -= 10000
        d = int(math.sqrt(x ** 2 + y ** 2))
        if d < ship.sta.length + 200:
            posAngel = (math.atan2(y, x) - ship.theta) % (2 * math.pi)
            x = d * math.cos(posAngel)
            y = d * math.sin(posAngel)
            for block in ship.sta.block:
                centerx = ((block.number / 4) * 2 - 1) * ship.sta.length / 10
                centery = ((block.number % 4) * 2 - 3) * ship.sta.length / 8
                d = int(math.sqrt((centerx - x) * (centerx - x) + (centery - y) * (centery - y)))
                if d < self.harmr / 4:
                    ship.hitten(self, x, y)
                    self.state = False
                    break

class torpedo610Ob(torpedoOb):
    def reInit(self):
        self.harm = 610
        
class torpedo553Ob(torpedoOb):
    def reInit(self):
        self.harm = 550
        self.v = 800
        
class torpedo(weapon):
    def init(self, number):
        self.typ = 'torpedo'
        self.harm = 1
        self.fixedtime = 200

class torpedo610(torpedo):
    def fire(self, torlist, ship):
        if self.addtime == 0 and self.harm >= 1:
            newtor = torpedo610Ob()
            newtor.reInit()
            newtor.x = ship.x + int(math.cos(ship.theta) * ship.sta.length)
            newtor.y = ship.y + int(math.sin(ship.theta) * ship.sta.length)
            newtor.vangel = ship.theta - 0.05 + 0.1 * random.random()
            torlist.append(newtor)
            torlist[-1].addtime = 75
            self.addtime = self.fixedtime
    def reInit(self):
        whatever = 0

class torpedo553(torpedo):
    def fire(self, torlist, ship):
        if self.addtime == 0 and self.harm >= 1:
            newtor = torpedo553Ob()
            newtor.reInit()
            newtor.x = ship.x + int(math.cos(ship.theta) * ship.sta.length)
            newtor.y = ship.y + int(math.sin(ship.theta) * ship.sta.length)
            newtor.vangel = ship.theta - 0.05 + 0.1 * random.random()
            torlist.append(newtor)
            torlist[-1].addtime = 75
            self.addtime = self.fixedtime
    def reInit(self):
        whatever = 0
