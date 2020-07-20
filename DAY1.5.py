# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:05:57 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    
    X,Y,Z=mc.player.getTilePos()
    mc.postToChat("你現在在x:"+str(X)+"Y"+str(Y)+"(Z)"+str(Z))
