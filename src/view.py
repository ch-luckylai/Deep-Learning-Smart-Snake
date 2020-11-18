#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  view.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

import sys

import pygame
import pygame.font
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

class Board(object):
	def __init__(self,screen,info={
		"gen":"0",
		"fitness":"0"
	}):
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.info = info
		self.textColor = (0,0,0)
		self.genFont = pygame.font.SysFont(None,24)
		self.genInfoFont = pygame.font.SysFont(None,20)
		self.fitnessFont = pygame.font.SysFont(None,24)
		self.fitnessInfoFont = pygame.font.SysFont(None,20)
		self.bgColor = (230,230,230)
		self.prep()

	def setInfo(self,info):
		self.info = info
		genInfoString = str(self.info.get("gen") or 0)
		fitnessInfoString = str(self.info.get("fitness") or 0)
		self.genInfoImage = self.genInfoFont.render(genInfoString,True,self.textColor)
		self.fitnessInfoImage = self.genInfoFont.render(fitnessInfoString,True,self.textColor)

	def prep(self):
		genInfoString = str(self.info.get("gen") or 0)
		fitnessInfoString = str(self.info.get("fitness") or 0)
		self.genImage = self.genFont.render("Gen",True,self.textColor)
		self.genInfoImage = self.genInfoFont.render(genInfoString,True,self.textColor)
		self.fitnessImage = self.genFont.render("Fitness",True,self.textColor)
		self.fitnessInfoImage = self.genInfoFont.render(fitnessInfoString,True,self.textColor)

		self.genRect = self.genImage.get_rect()
		self.genRect.right = self.screenRect.right - 20
		self.genRect.top = 20

		self.genInfoRect = self.genInfoImage.get_rect()
		self.genInfoRect.right = self.screenRect.right - 40
		self.genInfoRect.top = 40

		self.fitnessRect = self.fitnessImage.get_rect()
		self.fitnessRect.right = self.screenRect.right - 20
		self.fitnessRect.top = 60

		self.fitnessInfoRect = self.fitnessInfoImage.get_rect()
		self.fitnessInfoRect.right = self.screenRect.right - 40
		self.fitnessInfoRect.top = 80

	def show(self):
		self.screen.blit(self.genImage,self.genRect)
		self.screen.blit(self.genInfoImage,self.genInfoRect)
		self.screen.blit(self.fitnessImage,self.fitnessRect)
		self.screen.blit(self.fitnessInfoImage,self.fitnessInfoRect)

class Viewer(object):
	def __init__(self,width,height):
		pygame.init()
		self.alive = 1
		self.width = width
		self.height = height
		self.size =(width * 32 + 160,height * 32)
		self.screen = pygame.display.set_mode(self.size)
		self.board = Board(self.screen)
		pygame.display.set_caption("Deep-Learning Smart Snake")
		
	def mainloop(self):
		self.screen.fill(BG_COLOR)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.alive = 0
				sys.exit()
		self.blocks.draw(self.screen)
		self.board.show()
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
		

	def setInfo(self,info):
		self.info = info
		self.board.setInfo(info)
		
				

# ALMOST FINISHED EVERYTHING 
# SEP.10 2020
# LUCKY
