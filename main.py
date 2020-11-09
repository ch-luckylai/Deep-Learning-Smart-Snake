#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

from src.view import Viewer as Viewer

viewer = Viewer()
viewer.createBlocks(10,10)
viewer.mainloop()
