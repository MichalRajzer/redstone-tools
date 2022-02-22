
from distutils.log import debug
import time

class RedstoneHelper():
    def __init__(self, debug=False, framerate=15):
        """Class that has all the functions of the helper.\n
        dirX-direction multiplier, 1 means positive X, -1 means negative.\n
        dirY-direction multiplier, 1 means positive Y, -1 means negative."""
        from pynput.keyboard import Controller
        self.keyboard = Controller()
        self.debug = debug
        self.framerate = framerate

    def xLine(self, length, xOffset=0, zOffset=0, yOffset=0, block="white_concrete", dir=0):
        if dir == 0:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset-1} ~{yOffset} ~{length+xOffset} ~{zOffset-1} ~{yOffset} minecraft:{block}\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset} ~{yOffset} ~{length+xOffset} ~{zOffset} ~{yOffset} minecraft:redstone_wire\n")
        if dir == 2:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset-1} ~{yOffset} ~{-length+xOffset} ~{zOffset-1} ~{yOffset} minecraft:{block}\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset} ~{yOffset} ~{-length+xOffset} ~{zOffset} ~{yOffset} minecraft:redstone_wire\n")

    def xBus(self, length, width=8, xOffset=-1, zOffset=0, yOffset=0, gap=1):
        for j in range(width):
            for i in range(int(length/18)):
                self.xLine(14, xOffset=2+18*i+xOffset, zOffset=zOffset, yOffset=yOffset+j*(gap+1))
                self.instantRepeater(xOffset=16+18*i+xOffset, zOffset=1+zOffset, yOffset=yOffset+j*(gap+1))
                if self.debug:
                    print(f"Line {j}, stage {i}")
            self.xLine(length%18-1, xOffset=2+18*int(length/18)+xOffset, zOffset=zOffset, yOffset=yOffset+j*(gap+1))



    def instantRepeater(self, xOffset=0, zOffset=0, yOffset=0, dir=0): 
        if dir==0:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset-1} ~{yOffset} ~{xOffset} ~{zOffset-1} ~{yOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset} ~{yOffset} ~{xOffset} ~{zOffset} ~{yOffset} minecraft:sticky_piston[facing=east]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+2} ~{zOffset-1} ~{yOffset} ~{xOffset+2} ~{zOffset-1} ~{yOffset} minecraft:sticky_piston[facing=west]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+1} ~{zOffset} ~{yOffset} ~{xOffset+1} ~{zOffset} ~{yOffset} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+3} ~{zOffset-1} ~{yOffset} ~{xOffset+3} ~{zOffset-1} ~{yOffset} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+3} ~{zOffset} ~{yOffset} ~{xOffset+3} ~{zOffset} ~{yOffset} minecraft:redstone_wire\n")
        elif dir == 1:
            pass
        elif dir == 2:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset-1} ~{yOffset} ~{xOffset} ~{zOffset-1} ~{yOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{zOffset} ~{yOffset} ~{xOffset} ~{zOffset} ~{yOffset} minecraft:sticky_piston[facing=west]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-2} ~{zOffset-1} ~{yOffset} ~{xOffset-2} ~{zOffset-1} ~{yOffset} minecraft:sticky_piston[facing=east]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-1} ~{zOffset} ~{yOffset} ~{xOffset-1} ~{zOffset} ~{yOffset} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-3} ~{zOffset-1} ~{yOffset} ~{xOffset-3} ~{zOffset-1} ~{yOffset} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-3} ~{zOffset} ~{yOffset} ~{xOffset-3} ~{zOffset} ~{yOffset} minecraft:redstone_wire\n")
        elif dir == 3:
            pass

    def tester(self):
        self.xBus(length=64, width=4, gap=2)
 
    def OpenLine(self, key="/"):
        self.keyboard.press(key)
        self.keyboard.release(key)
        time.sleep(1.0/self.framerate)

for i in range(5):
    print(f"{5-i}!")
    time.sleep(1)
print("Start!")
helper = RedstoneHelper(framerate=20, debug=True)
helper.tester()

