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

import random



if __name__ == "__main__":
	DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))
	queueCount = 2000
	learningDatas = [LearningWeb([24,18,18,4]) for i in range(queueCount)]
	gen = 1
	_bestfitness = 0
	while 1:
		fitnesses = []
		bestFitness = 0
		replay = []
		for uid in range(queueCount):
			blocksHistroy = []
			lifeTime = 0
			stepLeft = 200
			score = 1
			blocks = [["EMPTY" for i in range(20)] for j in range(20)]
			snake = Snake(blocks)
			while 1:
				stepLeft -= 1
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
				lifeTime += 1
			if score < 10:
				fitness = lifeTime ** 2 * 2 ** score
			else:
				fitness = lifeTime ** 2 * 2 ** 10 * (score - 9)
			fitnesses.append(fitness)
			if fitness > bestFitness:
				bestFitness = fitness
				replay = blocksHistroy[:]
		best = fitnesses.index(max(fitnesses))
		newSnakes = [learningDatas[best]]
		for i in range(queueCount - 1):
			newSnakes.append(crossover(
				random.choice(learningDatas),random.choice(learningDatas)
			))
		if bestFitness > _bestfitness:
			_bestfitness = bestFitness
		print(f"Gen : {gen} , Best fitness : {fitnesses[best]}/{_bestfitness} {'[^]' if fitnesses[best] == _bestfitness else ''}")
		gen += 1
