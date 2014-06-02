import pygame, sys, Ship, math, Motion, Arm, ShipSta
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1500, 1500))
pygame.display.set_caption('TEST')
FPS = Ship.FPS
fpsClock = pygame.time.Clock()
white = (255, 255, 255)
sea = (60, 60, 100)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0 , 255, 0)
torlist = []

test = []
test.append(Ship.ship())
test.append(ShipSta.Shimakaze())
test[1].reInit()
test[1].inpC.left = K_a
test[1].inpC.right = K_d
test[1].inpC.up = K_w
test[1].inpC.down = K_s
test[1].inpC.cannonFire = K_q
test[1].inpC.torpedoFire = K_e
test[1].player = 1
test[1].x = 2500
test[0].theta = math.pi
test[0].x = 7500

while True:

    DISPLAYSURF.fill(black)
    pygame.draw.rect(DISPLAYSURF, sea, (250, 250, 1000, 1000))

    for ship in test:
        ship.clear()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN or event.type == KEYUP:
            for ship in test:
                Motion.motionRecord(ship, event)
                
    for ship in test:
        Motion.motionDisplay(DISPLAYSURF, ship)

    test[0].showSituation(DISPLAYSURF, 1300, 250)
    test[1].showSituation(DISPLAYSURF, 0, 250)

    for ship in test:
        for shipE in test:
            if ship.player != shipE.player:
                Motion.cannonFire(ship, shipE)
    for ship in test:
        Motion.torpedoFire(ship, torlist)

    for torpedoOb in torlist:
        if torpedoOb.state == False:
            torlist.remove(torpedoOb)

    for torpedoOb in torlist:
        torpedoOb.control(DISPLAYSURF)
        for ship in test:
            torpedoOb.fire(ship)

    test[0].revive(DISPLAYSURF, 1300, 750)
    test[1].revive(DISPLAYSURF, 0, 750)
    
    pygame.display.update()
    fpsClock.tick(FPS)
