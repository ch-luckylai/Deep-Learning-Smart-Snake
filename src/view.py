#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  view.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

import sys
import os

import pygame
from pygame.sprite import Sprite,Group

EMPTY_BLOCK_PATH = "static/empty.png"
BODY_BLOCK_PATH = "static/body.png"
APPLE_BLOCK_PATH = "static/apple.png"
HEAD_BLOCK_PATH = "static/head.png"
# I USED 64PX IMAGES AT FIRST BUT THEY ARE TOO BIIIIIIIIG! 
EMPTY_BLOCK_32PX_PATH = "static/empty32px.png" 
BODY_BLOCK_32PX_PATH = "static/body32px.png"
APPLE_BLOCK_32PX_PATH = "static/apple32px.png"
HEAD_BLOCK_32PX_PATH = "static/head32px.png"
BG_COLOR = (230,230,230)

IMAGES = {
	"EMPTY" :	pygame.image.load(EMPTY_BLOCK_32PX_PATH),
	"BODY"  :	pygame.image.load(BODY_BLOCK_32PX_PATH),
	"APPLE"	:	pygame.image.load(APPLE_BLOCK_32PX_PATH),
	"HEAD"  :	pygame.image.load(HEAD_BLOCK_32PX_PATH)
}

class Block(Sprite):
	def __init__(self,screen,styles,x='-',y='-'):
		super(Block,self).__init__()
		self.screen = screen
		self.styles = styles
		self.style = styles[x][y]
		self.image = IMAGES[self.style]
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x*32 if x != '-' else self.rect.width 
		self.rect.y = y*32 if y != '-' else self.rect.height
		
		#	I love JavaScript BETTER because I can use it like
		#	self.rect.x = (x != "-")? x*32 : self.rect.width
		
	def update(self,block):
		self.style = block[self.x][self.y]
		self.image = IMAGES[self.style]

class Viewer(object):
	def __init__(self,width,height):
		pygame.init()
		self.alive = 1
		self.width = width
		self.height = height
		self.size =(width * 32 + 160,height * 32)
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("BP-Deep-Learning Smart Snake")
		
	def mainloop(self):
		self.screen.fill(BG_COLOR)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.alive = 0
				sys.exit()
		self.blocks.draw(self.screen)
		pygame.display.flip()		
		
	def createBlocks(self,blocks):
		x = self.width
		y = self.height
		self.blocks = Group()
		style = blocks
		for x0 in range(x):
			for y0 in range(y):
				block = Block(self.screen,style,x0,y0)
				self.blocks.add(block)
		return style
		
	def updateBlocks(self,block):
		self.blocks.update(block)
				

# ALMOST FINISHED EVERYTHING 
# SEP.10 2020
# LUCKY
