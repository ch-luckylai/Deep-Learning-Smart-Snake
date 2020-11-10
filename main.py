#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

from src.view import Viewer as Viewer

if __name__ == "__main__":

	viewer = Viewer()
	blocks = viewer.createBlocks(20,20)
	blocks[10][10] = "HEAD"
	blocks[10][9] = "BODY"
	blocks[9][9] = "BODY"
	blocks[9][10] = "BODY"
	while 1:
		viewer.mainloop()
		viewer.updateBlocks()
		
	# FOR TEST ONLY
