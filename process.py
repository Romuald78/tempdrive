### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade
from utils import *



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

        

    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        params = {
            "filePath" : "images/codingFactory/cf_background.png",
            "size" : (self.SCREEN_WIDTH, self.SCREEN_HEIGHT),
            "filterColor": (255,255,255,128),
            "position" : (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)
        }
        self.background = createFixedSprite(params)
        params = {
            "filePath" : "images/codingFactory/cf.png",
            "filterColor": (255,255,255,160),
            "position" : (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)
        }
        self.logo  = createFixedSprite(params)
        self.speedX = random()*5 + 5
        self.speedY = random()*5 + 5


    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self,deltaTime):
        self.logo.center_x += self.speedX * deltaTime * 60
        self.logo.center_y += self.speedY * deltaTime * 60
        if(self.logo.center_x < 0 or self.logo.center_x >= self.SCREEN_WIDTH):
            self.speedX = -self.speedX
        if(self.logo.center_y < 0 or self.logo.center_y >= self.SCREEN_HEIGHT):
            self.speedY = -self.speedY


    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        self.background.draw()
        self.logo.draw()

        message  = "Are you ready to code ?"
        paramTxt = {"x": 3*self.SCREEN_WIDTH//4,
                    "y": 60,
                    "alignH": "center",
                    "alignV": "center",
                    "message": message,
                    "size": 50,
                    "color": (255, 255, 255, 128),
                    }
        drawText(paramTxt)


    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self,key,isPressed):
        print(f"key={key} - isPressed={isPressed}")
        

    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum,buttonName,isPressed):
        print(f"GamePad={gamepadNum} - ButtonNum={buttonName} - isPressed={isPressed}")
        

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
        if abs(self.logo.center_x - x) < self.logo.width//2.2:
            if abs(self.logo.center_y - y) < self.logo.height // 2.2:
                if isPressed:
                    if abs(self.speedX) < 1 and abs(self.speedY) < 1:
                        self.speedX *= 20
                        self.speedY *= 20
                    else:
                        self.speedX /= 20
                        self.speedY /= 20
