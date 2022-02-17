### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade
from utils import *
from random import randint



class Process:

    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================
    SCREEN_WIDTH  = int(1920*0.75)
    SCREEN_HEIGHT = int(1080*0.75)

    

    ### ====================================================================================================
    ### CONSTRUCTOR
    ### ====================================================================================================
    def __init__(self):
        pass

    # Create item and add to list
    def createItem(self):
        idx = randint(0,5)
        posX = randint(0,self.SCREEN_WIDTH)
        params = {
            "filePath": "images/items/candies.png",
            "position": (posX, self.SCREEN_HEIGHT+100),
            "spriteBox": (3,2, 128,128),
            "startIndex": idx,
            "endIndex"  : idx,
            "frameDuration":1/20,
        }
        itm = createAnimatedSprite(params)
        self.itemList.append(itm)


    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        # Create background (fixed)
        params = {
            "filePath" : "images/backgrounds/country.png",
            "size" : (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
            "filterColor": (255,255,255,255),
            "position" : (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)
        }
        self.background = createFixedSprite(params)
        # Create Player (fixed)
        params = {
            "filePath": "images/characters/troll_fix.png",
            "filterColor": (255, 128, 128, 255),
            "position": (self.SCREEN_WIDTH // 2, 260)
        }
        self.troll = createFixedSprite(params)
        # Movement variables
        self.moveL = False
        self.moveR = False
        # Create player running Right (animation)
        params = {
            "filePath": "images/characters/troll.png",
            "filterColor": (255, 128, 128, 255),
            "position": (self.SCREEN_WIDTH // 2, 260),
            "spriteBox": (5,1, 400,250),
            "startIndex": 1,
            "endIndex"  : 4,
            "frameDuration":1/20,
        }
        self.trollR = createAnimatedSprite(params)
        # Create player running Left (animation)
        params = {
            "filePath": "images/characters/troll.png",
            "filterColor": (255, 128, 128, 255),
            "position": (self.SCREEN_WIDTH // 2, 260),
            "spriteBox": (5, 1, 400, 250),
            "startIndex": 1,
            "endIndex": 4,
            "frameDuration": 1 / 20,
            "flipH":True
        }
        self.trollL = createAnimatedSprite(params)
        # Create item list (see createItem function)
        self.itemList = []
        # Create timer (item generation)
        self.timer = 0


    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self,deltaTime):
        # update sprite animations
        self.trollR.update_animation(deltaTime)
        self.trollL.update_animation(deltaTime)
        # Increase timer for item generation
        self.timer += deltaTime
        # if teimer over 1 second...
        if self.timer > 1:
            self.timer -= 1
            # ... then create item
            self.createItem()

        # For each item, move down
        for itm in self.itemList:
            itm.center_y -= 10
            # if item too low, destroy (remove from list)
            if itm.center_y < -100:
                self.itemList.remove(itm)
                # LIFE --

        # Collisions (for each item)
        for itm  in self.itemList:
            # check distance with the player (here rectangle hitbox between centers)
            if abs(itm.center_x - self.troll.center_x) < 150:
                if abs(itm.center_y - self.troll.center_y) < 100:
                    # Remove from list (destroy item : we got it)
                    self.itemList.remove(itm)
                    # SCORE ++
        # If we are moving to the left, move player
        if self.moveL:
            self.troll.center_x -= 20
        # If we are moving to the right, move player
        if self.moveR:
            self.troll.center_x += 20

        # Block player on the screen edges
        if self.troll.center_x < 100:
            self.troll.center_x = 100
        if self.troll.center_x > self.SCREEN_WIDTH-100:
            self.troll.center_x = self.SCREEN_WIDTH-100

        # Set the animated trolls to the player position (all sprites at the same X/Y)
        self.trollL.center_x = self.troll.center_x
        self.trollR.center_x = self.troll.center_x


    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        # Draw back first
        self.background.draw()
        # Draw troll (fixed one if not moving, else left, else right)
        if self.moveL == self.moveR:
            self.troll.draw()
        elif self.moveL:
            self.trollL.draw()
        else:
            self.trollR.draw()
        # display each items
        for itm in self.itemList:
            itm.draw()

    ### ====================================================================================================
    ### KEYBOARD EVENTS
    def onButtonEvent(self, gamepadNum,buttonName,isPressed):
        print(f"GamePad={gamepadNum} - ButtonNum={buttonName} - isPressed={isPressed}")

    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self,key,isPressed):
        print(f"key={key} - isPressed={isPressed}")
        if key == arcade.key.LEFT:
            self.moveL = isPressed
        if key == arcade.key.RIGHT:
            self.moveR = isPressed
        if key == arcade.key.SPACE and isPressed:
            self.createItem()

    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum,axisName,analogValue):
        print(f"GamePad={gamepadNum} - AxisName={axisName} - Value={analogValue}")
        

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self,x,y,dx,dy):
        print(f"MOUSE MOTION : x={x}/y={y} dx={dx}/dy={dy}")


    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self,x,y,buttonNum,isPressed):
        #print(f"MOUSE BUTTON : x={x}/y={y} buttonNum={buttonNum} isPressed={isPressed}")
        pass