import pygame, sys, Ship, math
from pygame.locals import *

def motionRecord(ship, event):

    ship.clear()
    
    if event.type == KEYDOWN:
        turn = True
    elif event.type == KEYUP:
        turn = False
        
    if event.key == ship.inpC.left:
        ship.inpR.left = turn
    elif event.key == ship.inpC.right:
        ship.inpR.right = turn
    elif event.key == ship.inpC.up:
        ship.inpR.up = turn
    elif event.key == ship.inpC.down:
        ship.inpR.down = turn
    elif event.key == ship.inpC.cannonFire:
        ship.inpR.cannonFire = turn
    elif event.key == ship.inpC.torpedoFire:
        ship.inpR.torpedoFire = turn
    elif event.key == ship.inpC.sidekickleft:
        ship.inpR.sidekickleft = turn
    elif event.key == ship.inpC.sidekickright:
        ship.inpR.sidekickright = turn
            
def motionDisplay(DISPLAYSURF, ship):
    
    if ship.inpR.left:
        ship.left()
    if ship.inpR.right:
        ship.right()
    if ship.inpR.up:
        ship.up()
    if ship.inpR.down:
        ship.down()
    if ship.inpR.sidekickleft:
        ship.sidekickleft()
    if ship.inpR.sidekickright:
        ship.sidekickright()
        
    ship.control()
            
    pygame.draw.line(DISPLAYSURF, ship.sta.color, (250 + int((ship.x - ship.sta.length * math.cos(ship.theta) / 2) / 10), 250 + int((ship.y - ship.sta.length * math.sin(ship.theta) / 2) / 10)), (250 + int(ship.x / 10), 250 + int(ship.y / 10)), 5)
    pygame.draw.line(DISPLAYSURF, ship.sta.color, (250 + int((ship.x - ship.sta.length * math.cos(ship.theta) / 2) / 10), 250 + int((ship.y - ship.sta.length * math.sin(ship.theta) / 2) / 10)), (250 + int((ship.x + ship.sta.length * math.cos(ship.theta) / 2) / 10), 250 + int((ship.y + ship.sta.length * math.sin(ship.theta) / 2) / 10)), 3)

def cannonFire(shipS, shipE):
    if shipS.inpR.cannonFire == True:
        shipS.cannonFire(shipE)

def torpedoFire(shipS, torlist):
    if shipS.inpR.torpedoFire == True:
        shipS.torpedoFire(torlist)
