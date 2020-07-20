# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:32:39 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()


mc.player.setTilePos(X,Y,Z)
'time'.sleep(5)

X = X + 100
mc.player.setPos(X,Y,Z)
'time'.sleep(5)

X = X + 100
mc.player.setPos(X,Y,Z)




X,Y,Z=mcgetTilePos(X,Y,Z).player.