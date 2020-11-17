#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

from src.view import Viewer 
from src.snake import Snake
from src.deeplearning import LearningWeb, crossover
import threading

import copy
import time
import random
import sys

def viewThread(size,queue):
	while len(queue) == 0:
		pass
	viewer = Viewer(size,size)
	block = queue[0]
	viewer.createBlocks(block)
	while viewer.alive:
		while not len(queue):
			viewer.updateBlocks(block)
			viewer.mainloop()
			time.sleep(0.1)
		block = queue.pop(0)
		viewer.updateBlocks(block)
		viewer.mainloop()
		time.sleep(0.3)
	sys.exit()

def find(array,value):
	indexes = []
	arrayCopy = array[:]
	for i in range(arrayCopy.count(value)):
		index = arrayCopy.index(value)
		indexes.append(index)
		arrayCopy[index] = None
	return indexes


if __name__ == "__main__":
	DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))
	inpValue = input("输入训练数量（默认2000）：")
	try:
		queueCount = int(inpValue)
	except:
		queueCount = 2000
	else:
		if queueCount <= 0 :
			queueCount = 2000
	learningDatas = [LearningWeb([24,12,8,4]) for i in range(queueCount)]
	historyQueue = []
	gen = 1
	_bestfitness = 0
	size = 10
	threadView = threading.Thread(target=viewThread,args=(size,historyQueue))
	threadView.start()
	while 1:
		fitnesses = []
		bestFitness = 0
		replay = []
		t0 = time.time()
		for uid in range(queueCount):
			blocksHistroy = []
			lifeTime = 0
			stepLeft = 25
			score = 3
			blocks = [["EMPTY" for i in range(size)] for j in range(size)]
			snake = Snake(blocks)
			lastDirection = (0,0)
			while 1:
				stepLeft -= 1
				lifeTime += 1
				learningData = learningDatas[uid]
				result = DIRECTIONS[
					learningData.forward(snake.getData())
				]
				if ((not(result[0] + lastDirection[0]))and(not(result[1] + lastDirection[1]))):
					result = lastDirection
				snake.update(result)
				blocksHistroy.append(copy.deepcopy(blocks))
				if not snake.alive:
					break
				if not stepLeft:
					break 
				if snake.gotScore:
					score += 1
					stepLeft = 500 if stepLeft > 450 else stepLeft + 50
			if score < 10:
				fitness = lifeTime * 2 ** score
			else:
				fitness = lifeTime * 2 ** 10 * (score - 9)
			fitnesses.append(fitness)
			if fitness > bestFitness:
				bestFitness = fitness
				replay = blocksHistroy[:]
		historyQueue.extend(replay[:])
		t1 = time.time()
		best = fitnesses.index(max(fitnesses))
		if bestFitness > _bestfitness:
			_bestfitness = bestFitness
		print(f"代数 : {gen} ,最佳评分 : {fitnesses[best]}/{_bestfitness} {'[BEST]' if fitnesses[best] == _bestfitness else ''}")
		newSnakes = [learningDatas[index] for index in find(fitnesses,fitnesses[best]) * 2]
		while len(newSnakes) < queueCount:
			newSnakes.append(crossover(
				random.choice(learningDatas),
				random.choice(learningDatas)
			))
		t2 = time.time()
		gen += 1

sys.exit()