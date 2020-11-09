#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  view.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

import sys

import pygame
from pygame.sprite import Sprite,Group

EMPTY_BLOCK_PATH = "static/empty.png"
BODY_BLOCK_PATH = "static/body.png"
APPLE_BLOCK_PATH = "static/apple.png"
HEAD_BLOCK_PATH = "static/head.png"


pygame.init()



def doNothing():
	return 
	
class Block(Sprite):
	def __init__(self,style,screen,x='-',y='-'):
		super(Block,self).__init__()
		self.screen = screen
		self.style = style
		self.image = pygame.image.load(BODY_BLOCK_PATH)
		self.rect = self.image.get_rect()
		
		self.rect.x = x if x != '-' else self.rect.width
		self.rect.y = y if y != '-' else self.rect.height
	
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		

class Viewer(object):
	def __init__(self,width=320,height=240):
		self.screen = pygame.display.set_mode()
		self.size =(width,height)
	def mainloop(self,status=1):
		pygame.display.set_mode(self.size)
		while status:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				else:
					self.mainfun()
			self.blocks.draw(self.screen)
			pygame.display.flip()
	def mainfun(self,function=doNothing):
		function()			
		
	def createBlocks(self,x,y):
		self.blocks = Group()
		for x0 in range(x):
			for y0 in range(y):
				block = Block("empty",self.screen,x0*64,y0*64)
				self.blocks.add(block)
				


