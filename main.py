
from distutils.log import debug
from multiprocessing import Condition
import time
from tkinter import N

from cv2 import add

class RedstoneHelper():
    def __init__(self, debug=False, framerate=10, kill=False):
        """Class that has all the functions of the helper.\n
        framerate-how quickly the commands are typed in 1s/framerate\n
        kill-kills all item entities on start"""
        from pynput.keyboard import Controller
        self.keyboard = Controller()
        self.debug = debug
        self.framerate = framerate
        if kill:
            self.OpenLine()
            self.keyboard.type("kill @e[type=minecraft:item]\n")

    def fillCond(self, x, y, z, endX, endY, endZ, block, nbt="", condition=""):
        self.OpenLine()
        self.keyboard.type(f"fill ~{x} ~{y} ~{z} ~{endX} ~{endY} ~{endZ} minecraft:{block}{nbt} {condition}\n")


    def block(self, x, y, z, block, nbt="", condition=""):
        self.OpenLine()
        self.keyboard.type(f"fill ~{x} ~{y} ~{z} ~{x} ~{y} ~{z} minecraft:{block}{nbt} {condition}\n")

    def instantRepeater(self, xOffset=0, yOffset=0, zOffset=0, dir=0): 
        """
        dir: 0 = +x;\n1 = +z;\n2 = -x;\n3 = -z;
        """
        if dir==0:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+1} ~{yOffset} ~{zOffset} ~{xOffset+1} ~{yOffset} ~{zOffset} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+3} ~{yOffset-1} ~{zOffset} ~{xOffset+3} ~{yOffset-1} ~{zOffset} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+3} ~{yOffset} ~{zOffset} ~{xOffset+3} ~{yOffset} ~{zOffset} minecraft:redstone_wire\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=east]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset+2} ~{yOffset-1} ~{zOffset} ~{xOffset+2} ~{yOffset-1} ~{zOffset} minecraft:sticky_piston[facing=west]\n")
        elif dir == 1:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset+1} ~{xOffset} ~{yOffset} ~{zOffset+1} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset+3} ~{xOffset} ~{yOffset-1} ~{zOffset+3} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset+3} ~{xOffset} ~{yOffset} ~{zOffset+3} minecraft:redstone_wire\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=south]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset+2} ~{xOffset} ~{yOffset-1} ~{zOffset+2} minecraft:sticky_piston[facing=north]\n")
        elif dir == 2:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-1} ~{yOffset} ~{zOffset} ~{xOffset-1} ~{yOffset} ~{zOffset} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-3} ~{yOffset-1} ~{zOffset} ~{xOffset-3} ~{yOffset-1} ~{zOffset} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-3} ~{yOffset} ~{zOffset} ~{xOffset-3} ~{yOffset} ~{zOffset} minecraft:redstone_wire\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=west]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset-2} ~{yOffset-1} ~{zOffset} ~{xOffset-2} ~{yOffset-1} ~{zOffset} minecraft:sticky_piston[facing=east]\n")
        elif dir == 3:
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset} ~{xOffset} ~{yOffset-1} ~{zOffset} minecraft:target\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset-1} ~{xOffset} ~{yOffset} ~{zOffset-1} minecraft:redstone_block\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset-3} ~{xOffset} ~{yOffset-1} ~{zOffset-3} minecraft:white_concrete\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset-3} ~{xOffset} ~{yOffset} ~{zOffset-3} minecraft:redstone_wire\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset} ~{zOffset} ~{xOffset} ~{yOffset} ~{zOffset} minecraft:sticky_piston[facing=north]\n")
            self.OpenLine()
            self.keyboard.type(f"fill ~{xOffset} ~{yOffset-1} ~{zOffset-2} ~{xOffset} ~{yOffset-1} ~{zOffset-2} minecraft:sticky_piston[facing=south]\n")

    def line(self, length, xOffset=0, yOffset=0, zOffset=0, block="white_concrete", dir=0):
        """dir: 0 = +x;\n1 = +z;\n2 = -x;\n3 = -z;"""
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
        """dir: 0 = +x;\n1 = +z;\n2 = -x;\n3 = -z;"""
        if dir == 0:
            for j in range(width):
                for i in range(int(length/18)):
                    if self.debug:
                        print(f"line {j}, stage {i}")
                    self.line(14, xOffset=2+18*i+xOffset, yOffset=yOffset, zOffset=zOffset+j*(gap+1))
                    self.instantRepeater(xOffset=16+18*i+xOffset, yOffset=1+yOffset, zOffset=zOffset+j*(gap+1))
                self.line(length%18-1, xOffset=2+18*int(length/18)+xOffset, yOffset=yOffset, zOffset=zOffset+j*(gap+1))
        else:
            pass

    def bin2LineDecoder(self, numbits=8, xOffset=0, yOffset=0, zOffset=0, dir=0):
        """dir: 0 = +x;\n1 = +z;\n2 = -x;\n3 = -z;"""
        import math
        if dir==0:
            for k in range(math.ceil(numbits/5)):
                if self.debug:
                    print(f"k: {k}")
                numOps = 5
                if (k+1)*5 >= numbits:
                    numOps = numbits%5
                    if self.debug:
                        print(f"NumOps: {numOps}")
                self.Bus(2*(2**numbits), width=numOps, xOffset=xOffset, yOffset=yOffset, zOffset=zOffset+k*17, gap=2, dir=0)
                for i in range(numOps):
                    self.line(2*(2**numbits), xOffset+2, yOffset+4, 1+zOffset+i*3+k*17, dir=0)
                for j in range(numOps): #fix NOT Mod6
                    for i in range(int(2*(2**numbits)/8)):
                        if 8*(i+1)%18<14:
                            if self.debug:
                                print(f"Adding block bit: {j}, pos: {i}")
                            self.block(8*(i+1)+xOffset, yOffset+0, zOffset+j*3+k*17, "white_concrete", condition="replace minecraft:redstone_wire")
                            self.block(8*(i+1)+xOffset, yOffset+1, zOffset+j*3+k*17, "redstone_wire", condition="replace minecraft:air")
                            self.block(8*(i+1)+xOffset, yOffset+1, zOffset+j*3+1+k*17, "target", condition="replace minecraft:air")
                            self.block(8*(i+1)+xOffset, yOffset+2, zOffset+j*3+1+k*17, "redstone_torch", condition="replace minecraft:air")
                for j in range(numOps):
                    for i in range(int(2**numbits)):
                        if self.debug and i%16 == 0:
                            print(f"Block Bit {j} pos {i}")
                        self.block(xOffset+2*i+2, yOffset+4, zOffset+j*3+k*17, "target")
                        self.block(xOffset+2*i+2, yOffset+5, zOffset+j*3+k*17, "redstone_torch")
                        self.block(xOffset+2*i+2, yOffset+6, zOffset+j*3+k*17, "white_concrete")
                        if i%(2**(5*k+j+1)) >= ((2**(5*k+j+1))/2):
                            self.block(xOffset+2*i+2, yOffset+7, zOffset+j*3+k*17, "redstone_torch")
                        else:
                            self.block(xOffset+2*i+2, yOffset+6, zOffset+j*3+1+k*17, "redstone_wall_torch", nbt="[facing=south]")
                            self.block(xOffset+2*i+2, yOffset+7, zOffset+j*3+1+k*17, "white_concrete")
                            self.block(xOffset+2*i+2, yOffset+7, zOffset+j*3+k*17, "redstone_wall_torch", nbt="[facing=north]")
                for i in range(2**numbits):
                    self.line(13, xOffset+2+i*2, yOffset+9, zOffset+17*k, dir=1)
                    self.instantRepeater(xOffset=xOffset+2+i*2, yOffset=yOffset+10, zOffset=13+17*k, dir=1)



    
    def tester(self):
        self.bin2LineDecoder(numbits=6, xOffset=1)

 
    def OpenLine(self, key="/"):
        self.keyboard.press(key)
        self.keyboard.release(key)
        time.sleep(1.0/self.framerate)

for i in range(3):
    print(f"{3-i}!")
    time.sleep(1)
print("Start!")
helper = RedstoneHelper(framerate=20, debug=True, kill=True)
helper.tester()

# for j in range(4):
#     for i in range(8):
#         print(f"i: {i}, j:{j}\n1:{i%(2**(j+1))} 2:{((2**(j+1))/2)}\n\n")
# 

