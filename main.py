#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

#from src.view import Viewer 
from src.snake import Snake
from src.deeplearning import LearningWeb, crossover

import time
import random

def find(array,value):
	indexes = []
	arrayCopy = array[:]
	for i in range(arrayCopy.count(value)):
		index = arrayCopy.index(value)
		indexes.append(index)
		arrayCopy[index] = None
	return indexes


if __name__ == "__main__":
	print("Start")
	DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))
	inpValue = input("Snakes Count (2000): ")
	try:
		queueCount = int(inpValue)
	except:
		queueCount = 2000
	else:
		if queueCount <= 0 :
			queueCount = 2000
	learningDatas = [LearningWeb([24,18,18,4]) for i in range(queueCount)]
	gen = 1
	_bestfitness = 0
	while 1:
		fitnesses = []
		bestFitness = 0
		replay = []
		t0 = time.time()
		for uid in range(queueCount):
			blocksHistroy = []
			lifeTime = 0
			stepLeft = 200
			score = 3
			blocks = [["EMPTY" for i in range(30)] for j in range(30)]
			snake = Snake(blocks)
			while 1:
				stepLeft -= 1
				lifeTime += 1
				learningData = learningDatas[uid]
				snake.update(DIRECTIONS[
					learningData.forward(snake.getData())
				])
				#blocksHistroy.append(blocks[:])
				if not snake.alive:
					break
				else:
					pass
				if not stepLeft:
					break 
				if snake.gotScore:
					score += 1
					stepLeft = 500 if stepLeft > 400 else stepLeft + 100
			if score < 10:
				fitness = lifeTime ** 2 * 2 ** score
			else:
				fitness = lifeTime ** 2 * 2 ** 10 * (score - 9)
			fitnesses.append(fitness)
			if fitness > bestFitness:
				bestFitness = fitness
				replay = blocksHistroy[:]
		t1 = time.time()
		best = fitnesses.index(max(fitnesses))
		if bestFitness > _bestfitness:
			_bestfitness = bestFitness
		print(f"Forward Time : {t1-t0}s")
		print(f"Gen : {gen} , Best fitness : {fitnesses[best]}/{_bestfitness} {'[BEST]' if fitnesses[best] == _bestfitness else ''}")
		newSnakes = [learningDatas[index] for index in find(fitnesses,fitnesses[best]) * 5]
		print(f"NexAge Count : {len(newSnakes)} + {int(queueCount / 20)}")
		for i in range(int(queueCount / 20)):
			newSnakes.append(
				random.choice(learningDatas)
			)
		while len(newSnakes) < queueCount:
			newSnakes.append(crossover(
				random.choice(learningDatas),
				random.choice(learningDatas)
			))
		t2 = time.time()
		print(f"Crossover Time : {t2-t1}s")
		gen += 1
