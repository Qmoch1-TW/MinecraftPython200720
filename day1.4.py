# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:40:28 2020

@author: user
"""
mc=Minecraft.create()from mcpi.minecraft import Minecraft

import time
t=0
while True :
        t = t + 1

        mc.postToChat("這是牛逼第"+str(t)+"次")
        time.sleep(2)
        
        