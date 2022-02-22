
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

    def Line(self, length, xOffset=0, yOffset=0, zOffset=0, block="white_concrete", dir=0):
        if dir == 0:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{length+xOffset} ~{yOffset-1} ~{zOffset} minecraft:{block}\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{length+xOffset} ~{yOffset} ~{zOffset} minecraft:redstone_wire\n")
        if dir == 1:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{length+zOffset} minecraft:{block}\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{length+zOffset} minecraft:redstone_wire\n")
        if dir == 2:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{-length+xOffset} ~{yOffset-1} ~{zOffset} minecraft:{block}\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{-length+xOffset} ~{yOffset} ~{zOffset} minecraft:redstone_wire\n")
        if dir == 3:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{-length+zOffset} minecraft:{block}\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{-length+zOffset} minecraft:redstone_wire\n")

    def Bus(self, length, width=8, xOffset=-1, yOffset=0, zOffset=0, gap=1, dir=0):
        for j in range(width):
            for i in range(int(length/18)):
                self.Line(14, xOffset=2+18*i+xOffset, yOffset=yOffset, zOffset=zOffset+j*(gap+1))
                self.instantRepeater(xOffset=16+18*i+xOffset, yOffset=1+yOffset, zOffset=zOffset+j*(gap+1))
                if self.debug:
                    print(f"Line {j}, stage {i}")
            self.Line(length%18-1, xOffset=2+18*int(length/18)+xOffset, yOffset=yOffset, zOffset=zOffset+j*(gap+1))



    def instantRepeater(self, xOffset=0, yOffset=0, zOffset=0, dir=0): 
        if dir==0:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=east]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+2} ~{yOffset-1} ~{zOffset} ~{xOffset+2} ~{yOffset-1} ~{zOffset} minecraft:sticky_piston[facing=west]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+1} ~{yOffset} ~{zOffset} ~{xOffset+1} ~{yOffset} ~{zOffset} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+3} ~{yOffset-1} ~{zOffset} ~{xOffset+3} ~{yOffset-1} ~{zOffset} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+3} ~{yOffset} ~{zOffset} ~{xOffset+3} ~{yOffset} ~{zOffset} minecraft:redstone_wire\n")
        elif dir == 1:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=south]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset+2} ~{xOffset} ~{yOffset-1} ~{zOffset+2} minecraft:sticky_piston[facing=north]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset+1} ~{xOffset} ~{yOffset} ~{zOffset+1} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset+3} ~{xOffset} ~{yOffset-1} ~{zOffset+3} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset+3} ~{xOffset} ~{yOffset} ~{zOffset+3} minecraft:redstone_wire\n")
        elif dir == 2:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=west]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-2} ~{yOffset-1} ~{zOffset} ~{xOffset-2} ~{yOffset-1} ~{zOffset} minecraft:sticky_piston[facing=east]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-1} ~{yOffset} ~{zOffset} ~{xOffset-1} ~{yOffset} ~{zOffset} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-3} ~{yOffset-1} ~{zOffset} ~{xOffset-3} ~{yOffset-1} ~{zOffset} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-3} ~{yOffset} ~{zOffset} ~{xOffset-3} ~{yOffset} ~{zOffset} minecraft:redstone_wire\n")
        elif dir == 3:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=north]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset-2} ~{xOffset} ~{yOffset-1} ~{zOffset-2} minecraft:sticky_piston[facing=south]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset-1} ~{xOffset} ~{yOffset} ~{zOffset-1} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset-3} ~{xOffset} ~{yOffset-1} ~{zOffset-3} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset-3} ~{xOffset} ~{yOffset} ~{zOffset-3} minecraft:redstone_wire\n")

    def tester(self):
        # self.Bus(length=64, width=4, gap=2)
        self.instantRepeater(zOffset=2, dir=3)
 
    def OpenLine(self, key="/"):
        self.keyboard.press(key)
        self.keyboard.release(key)
        time.sleep(1.0/self.framerate)

for i in range(3):
    print(f"{5-i}!")
    time.sleep(1)
print("Start!")
helper = RedstoneHelper(framerate=20, debug=True)
helper.tester()

