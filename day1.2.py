# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:59:57 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()


mc.player.setTilePos(100,100,100)

X = 254
Y = 69
Z = 220

mc.player.setTilePos(X,Y,Z)



