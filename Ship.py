import pygame, sys, math, random, Arm
from pygame.locals import *
pygame.init()
FPS = 10
turnr = .02
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

def vadd(mag1, mag2, ang1, ang2, magOrAng):
    magx = mag1 * math.cos(ang1) + mag2 * math.cos(ang2)
    magy = mag1 * math.sin(ang1) + mag2 * math.sin(ang2)
    if magOrAng == 'mag':
        return int(math.sqrt(magx * magx + magy * magy))
    if magOrAng == 'ang':
        return math.atan2(magy, magx)

class statistics:
    level = int()
    name = 'Default'
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
        self.level = 0
        self.name = 'Default'
        self.length = 100
        self.resistance = 10
        self.propulsion = 100
        self.evasion = .1
        self.armor = [50, 50, 50, 50, 50, 50, 50, 50]
        self.health = [30, 30, 30, 30, 30, 30, 30, 30]
        self.weapon = [[Arm.cannon127()], [Arm.cannon127()], [Arm.cannon127()], [Arm.cannon127()], [Arm.cannon127()], [Arm.cannon127()], [Arm.cannon127()], [Arm.cannon127()]]
        self.color = white
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
            weapon.reInit()

    def hitten(self, harm, ship):
        if self.armor > 5:
            self.armor -= 5
        else:
            self.armor = 0
        if self.health > harm / (self.armor + 10):
            harm = int(harm / (self.armor + 10))
            self.health -= harm
            if ship.sta.propulsion >= harm + 50:
                ship.sta.propulsion -= harm
            else:
                ship.sta.propulsion = 50
            for weapon in self.weapon:
                if random.randint(0, 4) == 0:
                    weapon.harm -= int(weapon.harm * harm/ (self.health + harm))
                    if weapon.harm <= 1:
                        weapon.harm = 0
        else:
            self.state = False

    def cannonFire(self, shipS, shipE):
        for weapon in self.weapon:
            if weapon.typ == 'cannon':
                weapon.fire(shipS, shipE)

    def torpedoFire(self, torlist, shipS):
        for weapon in self.weapon:
            if weapon.typ == 'torpedo':
                weapon.fire(torlist, shipS)
            
class inputRecord:
    left = bool()
    right = bool()
    up = bool()
    down = bool()
    cannonFire = bool()
    torpedoFire = bool()
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.cannonFire = False
        self.torpedoFire = False

class inputControl:
    left = K_LEFT
    right = K_RIGHT
    up = K_UP
    down = K_DOWN
    cannonFire = K_l
    torpedoFire = K_m
    def __init__(self):
        self.left = K_LEFT
        self.right = K_RIGHT
        self.up = K_UP
        self.down = K_DOWN
        self.cannonFire = K_l
        self.torpedoFire = K_m
    
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

    def reInit(self):
        for block in self.sta.block:
            block.armor += self.sta.level
            block.health += self.sta.level
            for weapon in block.weapon:
                weapon.harm += self.sta.level
    
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
            pygame.draw.rect(DISPLAYSURF, (self.sta.block[i].health, self.sta.block[i].health, self.sta.block[i].health), (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))
            if self.sta.block[i].state == False:
                pygame.draw.rect(DISPLAYSURF, red, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))

    def hitten(self, weapon, x, y):
        for block in self.sta.block:
            centerx = ((block.number / 4) * 2 - 1) * self.sta.length / 10
            centery = (3 - (block.number % 4) * 2) * self.sta.length / 8
            d = math.sqrt((centerx - x) * (centerx - x) + (centery - y) * (centery - y))
            if d < weapon.harmr:
                block.hitten(weapon.harm, self)
            if d < weapon.harmr / 2:
                block.hitten(weapon.harm, self)
            if d < weapon.harmr / 4:
                block.hitten(weapon.harm, self)
                
    def cannonFire(self, shipE):
        for block in self.sta.block:
            if block.state:
                block.cannonFire(self, shipE)

    def torpedoFire(self, torlist):
        for block in self.sta.block:
            if block.state:
                block.torpedoFire(torlist, self)

    def revive(self, DISPLAYSURF, x, y):
        for i in range(0, 8):
            conditionmaincan = False
            existmaincan = 0
            if self.sta.block[i].armor < self.sta.armor[i]:
                if self.sta.block[i].addtime < 0:
                    self.sta.block[i].addtime -= 1
                else:
                    self.sta.block[i].addtime = 50
                    self.sta.block[i].armor += 1

            conditioncan = False
            existcan = False
            conditiontor = False
            existtor = False
                    
            for weapon in self.sta.block[i].weapon:
                if weapon.typ == 'cannon':
                    existcan = True
                    existmaincan += 1
                    if weapon.addtime > 0:
                        weapon.addtime -= 1
                        pygame.draw.rect(DISPLAYSURF, (255 - weapon.addtime, 255 - weapon.addtime, 255 - weapon.addtime), (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))
                    else:
                        pygame.draw.rect(DISPLAYSURF, green, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))
                    if weapon.harm != 0:
                        conditioncan = True
                        if existmaincan == 1:
                            if weapon.addtime == 0:
                                conditionmaincan = True
                if weapon.typ == 'torpedo':
                    existtor = True
                    if weapon.addtime > 0:
                        weapon.addtime -= 1
                        pygame.draw.rect(DISPLAYSURF, (255 - weapon.addtime, 255 - weapon.addtime, 255 - weapon.addtime), (x + (i / 4) * 50, y + (i % 4) * 50 + 300, 50, 50))
                    else:
                        pygame.draw.rect(DISPLAYSURF, green, (x + (i / 4) * 50, y + (i % 4) * 50 + 300, 50, 50))
                    if weapon.harm != 0:
                        conditiontor = True

            if conditionmaincan:
                pygame.draw.rect(DISPLAYSURF, yellow, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))

            if (self.sta.block[i].state == False or conditioncan == False) and existcan:
                pygame.draw.rect(DISPLAYSURF, red, (x + (i / 4) * 50, y + (i % 4) * 50, 50, 50))

            if (self.sta.block[i].state == False or conditiontor == False) and existtor:
                pygame.draw.rect(DISPLAYSURF, red, (x + (i / 4) * 50, y + (i % 4) * 50 + 300, 50, 50))
