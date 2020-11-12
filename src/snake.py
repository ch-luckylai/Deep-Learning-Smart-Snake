#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  snake.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

import random

class Snake(object):
	def __init__(self,blocks,length=4):
		self.alive = 1
		self.defaultLength = length
		self.defaultBlocks = blocks[:]
		self.length = length
		self.blocks = blocks
		self.snake = [(10,10)]
		self.direction = (1,0)
		self.spawnApple()
		
	def update(self,direction):
		self.direction = direction
		x,y = self.snake[0]
		dx,dy = self.direction
		head = (x+dx,y+dy)
		self.snake.insert(0,head)
		if self.length < len(self.snake):
			deleteX,deleteY = self.snake.pop()
			self.blocks[deleteX][deleteY] = 'EMPTY'
		if max(*head) == len(self.blocks) or min(*head) < 0 or self.blocks[x+dx][y+dy] == 'BODY':
			self.die()
		else:
			if self.blocks[x+dx][y+dy] == "APPLE":
				self.length += 1
				self.spawnApple()
			self.blocks[x][y] = 'BODY'
			self.blocks[x+dx][y+dy] = 'HEAD'
			
	def spawnApple(self):
		x,y = random.randint(0,len(self.blocks)-1),random.randint(0,len(self.blocks[0])-1)
		while self.blocks[x][y] != "EMPTY":
			x,y = random.randint(len(self.blocks)-1),random.randint(len(self.blocks[0])-1)
		self.blocks[x][y] = 'APPLE'
	def die(self):
		self.alive = 0
		print("Oh, your snake was died.")
		return 0


		
