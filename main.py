#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

from src.view import Viewer 
from src.snake import Snake

import time
import random

if __name__ == "__main__":
	viewer = Viewer()
	blocks = viewer.createBlocks(20,20)
	snake = Snake(blocks)
	while snake.alive:
		snake.update(random.choice(((1,0),(-1,0),(0,1),(0,-1)))) # RANDOM FOR TESTING
		viewer.mainloop()
		viewer.updateBlocks()
		
		time.sleep(0.3)
		
	# FOR TESTING ONLY
