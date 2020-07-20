# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:30:55 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()



X,Y,Z=mc.player.getTilePos()


mc.setBlock(X+1,Y,Z,169)
mc.setBlock(X+2,Y,Z,169)
mc.setBlock(X+3,Y,Z,169)  
mc.setBlock(X+4,Y,Z,171)