#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  deeplearning.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

from random import randint
import numpy as np
import random

class LearningWeb(object):
    def __init__(self,layersWidth=[]):
        self.layers = []
        self.weights = []
        for width in layersWidth:
            self.layers.append(np.array([0 for i in range(width)]))
        for layer in range(len(layersWidth)-1):
            self.weights.append(self.__randomLayer(
                layersWidth[layer],layersWidth[layer+1]
            ))
        self.layersWidth = layersWidth
        self.learningRate = 0.7
        self.mutationRate = 0.1

    def __randomLayer(self,width1,width2):
        return np.array([[random.uniform(-1,1) for i in range(width2)] for j in range(width1)])

    def __resetWeightPoint(self):
        weightCount = len(self.weights)
        a = random.randint(0,weightCount-1)
        weightX = len(self.weights[a])
        b = random.randint(0,weightX-1)
        weightY = len(self.weights[a][b])
        c = random.randint(0,weightY-1)
        result = random.gauss(0,1) / 5
        if result > 1:
            result = 1
        elif result < -1:
            result = -1
        self.weights[a][b][c] = result

    def mutate(self):
        for i in range(1):
            self.__resetWeightPoint()

    def setLearningRate(self,rate):
        self.learningRate = rate

    def forward(self,input):
        inputLayer = np.array(input)
        layerCount = len(self.layers)
        if not layerCount:
            return 0
        self.layers[0] = inputLayer
        for layer in range(layerCount-1):
            self.layers[layer+1] = self.__relu(self.layers[layer].dot(self.weights[layer]))
        return np.max(np.argwhere(self.layers[-1] == max(self.layers[-1])))

    def backward(self,outputExpect):
        delta = 0
        layerCount = len(self.layers)
        if not layerCount:
            return 0
        output = self.layers[-1]
        for layer in range(layerCount-1):
            opLayer = -(layer+1)
            if layer == 0:
                error = outputExpect - output
                delta = error * (self.__sigmoidPrime(output))
            else:
                error = delta.dot(self.weights[opLayer+1].T)
                delta = error * self.__sigmoidPrime(self.layers[opLayer])
            self.weights[opLayer] += self.learningRate * self.layers[opLayer] * (delta)

    def reward(self,rewardRate):
        layerCount = len(self.layers)
        if not layerCount:
            return 0
        lastOutput = self.layers[-1]
        maxIndex = np.argwhere(lastOutput == max(lastOutput))
        result = lastOutput.copy()
        result[maxIndex] = result[maxIndex] * (1 + rewardRate)
        for i in range(5):
            self.backward(result)

    def __relu(self,array):
        array[array<0] = 0
        return array

    def __sigmoid(self,array):
        return 1 / (1 + np.exp(-array))

    def __sigmoidPrime(self,array):
        return array * (1 - array)

def crossover(father,mother):
    if father.layersWidth != mother.layersWidth:
        return 0
    mutationRate = (father.mutationRate + mother.mutationRate) / 2
    layerCount = len(father.weights)
    children = LearningWeb(father.layersWidth)
    for layer in range(layerCount):
        weightX = len(children.weights[layer])
        for x in range(weightX):
            weightY = len(children.weights[layer][x])
            for y in range(weightY):
                children.weights[layer][x][y] = random.choice(
                    (father.weights[layer][x][y],mother.weights[layer][x][y])
                )
                if mutationRate> random.random():
                    np.add(children.weights[layer][x][y],random.gauss(0,1) / 5)
                    if children.weights[layer][x][y] > 1:
                        children.weights[layer][x][y] = 1
                    if children.weights[layer][x][y] < -1:
                        children.weights[layer][x][y] = -1
                    
    return children


if __name__ == "__main__":
    test1 = LearningWeb([2,3,2])
    test2 = LearningWeb([2,3,2])
    print(test1.weights)
    print(test2.weights)
    print(crossover(test1,test2).weights)