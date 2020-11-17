#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  snake.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

import random

class Snake(object):
	def __init__(self,blocks,length=3):
		self.gotScore = 0
		self.alive = 1
		self.length = length
		self.blocks = blocks
		self.snake = [(int(len(self.blocks)/2),int(len(self.blocks)/2))]
		self.direction = (1,0)
		self.spawnApple()
		
	def update(self,direction):
		self.gotScore = 0
		self.direction = direction
		x,y = self.snake[0]
		dx,dy = self.direction
		head = (x+dx,y+dy)
		self.snake.insert(0,head)
		if self.length < len(self.snake):
			deleteX,deleteY = self.snake.pop()
			self.blocks[deleteX][deleteY] = 'EMPTY'
		died = 0
		if max(*head) == len(self.blocks) or min(*head) < 0 or self.blocks[x+dx][y+dy] == 'BODY':
			died = 1
		else:
			if self.blocks[x+dx][y+dy] == "APPLE":
				self.length += 1
				self.spawnApple()
				self.gotScore = 1
			self.blocks[x][y] = 'BODY'
			self.blocks[x+dx][y+dy] = 'HEAD'
		if died:
			self.die()
		for blocks in self.blocks:
			if "APPLE" in blocks:
				return
		self.spawnApple()
				
	def spawnApple(self):
		x,y = random.randint(0,len(self.blocks)-1),random.randint(0,len(self.blocks[0])-1)
		while self.blocks[x][y] != "EMPTY":
			x,y = random.randint(0,len(self.blocks)-1),random.randint(0,len(self.blocks[0])-1)
		self.blocks[x][y] = 'APPLE'
		
	def die(self):
		self.alive = 0
		return 0

	def getData(self):
		length = len(self.blocks)
		inputData = []
		directions = (
			(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)
		)
		for direction in directions:
			result = self.__getDirectionData(direction)
			inputData.extend([
				result["apple"] ,
				result["body"] ,
				result["wall"] 
			])
		return inputData
	
	def __getDirectionData(self,direction=(1,0)):
		width = len(self.blocks)
		x,y=self.snake[0]
		counter = 0
		result = {
			"apple":0,
			"body":0,
			"wall":0
		}
		while 1:
			counter+= 1
			x+=direction[0]
			y+=direction[1]
			if max(x,y) == len(self.blocks) or min(x,y) < 0:
				result["wall"] = 1 / counter 
				break
			elif self.blocks[x][y] == "BODY" and not(result["body"]):
				result["body"] = 1 / counter
			elif self.blocks[x][y] == "APPLE":
				result["apple"] = 1 / counter
		return result

			



		
