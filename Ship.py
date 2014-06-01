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
    r = int()
    harm = int()
    harmr = int()
    addtime = int()
    fixedtime = int()
    
    def __init__(self):
        self.r = 0
        self.harm = 0
        self.harmr = 0
        self.addtime = 0
        self.fixedtime = 0

class cannon(weapon):
    rmin = float()
    rmax = float()
    
    def __init__(self):
        self.rmin = 0
        self.rmax = 0
        self.r = 2000
        self.harm = 20
        self.harmr = 100
        self.addtime = 0
        self.fixedtime = 50

    def init(self, number):
        if number == 0:
            self.rmin = 0
            self.rmax = 3 * math.pi / 4
        elif number == 1 or number == 2:
            self.rmin = math.pi / 4
            self.rmax = 3 * math.pi / 4
        elif number == 3:
            self.rmin = math.pi / 4
            self.rmax = math.pi
        elif number == 4:
            self.rmin = math.pi
            self.rmax = 7 * math.pi / 4
        elif number == 5 or number == 6:
            self.rmin = 5 * math.pi / 4
            self.rmax = 7 * math.pi / 4
        elif number == 7:
            self.rmin = 5 * math.pi / 4
            self.rmax = 2 * math.pi
       
    def fire(self, shipS, shipE):
        if self.addtime == 0:
            d = math.sqrt((min((shipS.x - shipE.x) % 10000, (shipE.x - shipS.x) % 10000)) ** 2 + (min((shipS.y - shipE.y) % 10000, (shipE.y - shipS.y) % 10000)) ** 2)
            if d < self.r:
                x = shipE.x - shipS.x
                y = shipE.y - shipS.y
                if x < -5000:
                    x += 10000
                elif x > 5000:
                    x -= 10000
                if y < -5000:
                    y += 10000
                elif y > 5000:
                    y -= 10000
                posAngel = (math.atan2(y, x) - shipS.theta) % (2 * math.pi)
                if self.rmin <= posAngel and posAngel <= self.rmax:
                    angel = float()
                    angel = random.randint(0, 360) * 2 * math.pi / 360
                    pos = random.randint(0, int(d / 10))
                    shipE.hitten(self, int(pos * math.cos(angel)), int(pos * math.sin(angel)))
                self.addtime = self.fixedtime

class statistics:
    name = ''
    length = int()
    resistance = int()
    propulsion = int()
    evasion = float()
    health = []
    armor = []
    weapon = []
    block = []
    color = (255, 0, 0)
    def __init__(self):
        self.name = ''
        self.length = 100
        self.resistance = 10
        self.propulsion = 100
        self.evasion = .1
        self.armor = [20, 20, 20, 20, 20, 20, 20, 20]
        self.health = [30, 30, 30, 30, 30, 30, 30, 30]
        self.weapon = [[cannon()], [cannon()], [cannon()], [cannon()], [cannon()], [cannon()], [cannon()], [cannon()]]
        self.color = (255, 0, 0)
        self.block = [block(), block(), block(), block(), block(), block(), block(), block()]
        for i in range(0, 8):
            self.block[i].number = i
            self.block[i].init(self)

class block:
    state = bool()
    number = int()
    armor = int()
    health = int()
    weapon = []
    addtime = int()
    def __init__(self):
        self.state = True
        self.number = 0
        self.armor = 0
        self.health = 0
        self.weapon = []
        self.addtime = 50
    def init(self, sta):
        self.armor = sta.armor[self.number]
        self.health = sta.health[self.number]
        self.weapon = sta.weapon[self.number]
        for weapon in self.weapon:
            weapon.init(self.number)

    def hitten(self, harm):
        if self.armor > 5:
            self.armor -= 5
        else:
            self.armor = 0
        if self.health > harm / (self.armor + 10):
            harm = harm / (self.armor + 10)
            self.health -= harm
            for weapon in self.weapon:
                if random.randint(0, 1) == 0:
                    weapon.harm -= harm / (self.health + harm)
        else:
            self.state = False

    def cannonFire(self, shipS, shipE):
        for weapon in self.weapon:
            weapon.fire(shipS, shipE)
            
class inputRecord:
    left = bool()
    right = bool()
    up = bool()
    down = bool()
    fire = bool()
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.fire = False

class inputControl:
    left = K_LEFT
    right = K_RIGHT
    up = K_UP
    down = K_DOWN
    fire = K_l
    def __init__(self):
        self.left = K_LEFT
        self.right = K_RIGHT
        self.up = K_UP
        self.down = K_DOWN
        self.fire = K_l
    
class ship:
    player = int()
    x = int()
    y = int()
    theta = float()
    v = int()
    vangel = float()
    ax = int()
    ay = int()
    sta = statistics()
    inpR = inputRecord()
    inpC = inputControl()
    
    def clear(self):
        self.ax = 0
        self.ay = 0
        self.alpha = 0
    
    def __init__(self):
        player = 0
        self.x = 5000
        self.y = 5000
        self.theta = 0
        self.v = 0
        self.vangel = 0
        self.ax = 0
        self.ay = 0
        self.sta = statistics()
        self.inpR = inputRecord()
        self.inpC = inputControl()
    
    def control(self):
        if (self.vangel - self.theta) % (2 * math.pi) <= math.pi / 2 and (self.vangel - self.theta) % (2 * math.pi) > turnr:
            self.vangel -= turnr
        elif (self.vangel - self.theta) % (2 * math.pi) >= 3 * math.pi / 2 and (self.vangel -self.theta) % (2 * math.pi) < 2 * math.pi - turnr:
            self.vangel += turnr
        elif (self.vangel - self.theta) % (2 * math.pi) > math.pi / 2 and (self.vangel - self.theta) % (2 * math.pi) < math.pi - turnr:
            self.vangel -= turnr
        elif (self.vangel - self.theta) % (2 * math.pi) < 3 * math.pi / 2 and (self.vangel -self.theta) % (2 * math.pi) > math.pi + turnr:
            self.vangel += turnr
        elif (self.vangel - self.theta) % (2 * math.pi) <= turnr or (self.vangel - self.theta) % (2 * math.pi) >= 2 * math.pi - turnr:
            self.vangel = self.theta
        elif (self.vangel - self.theta) % (2 * math.pi) <= math.pi + turnr and (self.vangel - self.theta) % (2 * math.pi) >= math.pi - turnr:
            self.vangel = self.theta + math.pi
        vx = int(self.v * math.cos(self.vangel))
        vy = int(self.v * math.sin(self.vangel))
        self.ax -= int(self.v * self.v * math.cos(self.vangel) / 100) / self.sta.resistance
        self.ay -= int(self.v * self.v * math.sin(self.vangel) / 100) / self.sta.resistance
        vx += self.ax / FPS
        vy += self.ay / FPS
        self.x = (self.x + vx / FPS) % 10000
        self.y = (self.y + vy / FPS) % 10000
        self.v = math.sqrt(vx * vx + vy * vy)
        self.vangel = math.atan2(vy, vx)
        
    def left(self):
        self.theta -= self.sta.evasion
    def right(self):
        self.theta += self.sta.evasion
    def up(self):
        self.ax += int(self.sta.propulsion * math.cos(self.theta))
        self.ay += int(self.sta.propulsion * math.sin(self.theta))
    def down(self):
        self.ax -= int(self.sta.propulsion * math.cos(self.theta) / 2)
        self.ay -= int(self.sta.propulsion * math.sin(self.theta) / 2)
        
    def showSituation(self, DISPLAYSURF, x, y):
        for i in range(0, 8):
            pygame.draw.rect(DISPLAYSURF, (self.sta.block[i].health * 8, self.sta.block[i].health * 8, self.sta.block[i].health * 8), (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))
            if self.sta.block[i].state == False:
                pygame.draw.rect(DISPLAYSURF, red, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))

    def hitten(self, weapon, x, y):
        for block in self.sta.block:
            centerx = ((block.number / 4) * 2 - 1) * self.sta.length / 10
            centery = ((block.number % 4) * 2 - 3) * self.sta.length / 8
            d = math.sqrt((centerx - x) * (centerx - x) + (centery - y) * (centery - y))
            if d < weapon.harmr:
                block.hitten(weapon.harm)
            if d < weapon.harmr / 2:
                block.hitten(weapon.harm)
            if d < weapon.harmr / 4:
                block.hitten(weapon.harm)
    def cannonFire(self, shipE):
        for block in self.sta.block:
            if block.state:
                block.cannonFire(self, shipE)

    def revive(self, DISPLAYSURF, x, y):
        for i in range(0, 8):
            if self.sta.block[i].armor < self.sta.armor[i]:
                if self.sta.block[i].addtime < 0:
                    self.sta.block[i].addtime -= 1
                else:
                    self.sta.block[i].addtime = 50
                    self.sta.block[i].armor += 1
            for weapon in self.sta.block[i].weapon:
                if weapon.addtime > 0:
                    weapon.addtime -= 1
                    pygame.draw.rect(DISPLAYSURF, (255 - 5 * weapon.addtime, 255 - 5 * weapon.addtime, 255 - 5 * weapon.addtime), (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))
                else:
                    pygame.draw.rect(DISPLAYSURF, green, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))
            if self.sta.block[i].state == False:
                pygame.draw.rect(DISPLAYSURF, red, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))