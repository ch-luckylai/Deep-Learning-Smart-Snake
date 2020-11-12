#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  deeplearning.py
#  
#  Copyright 2020 luckylai <luckylai1126@foxmail.com>
#  

import numpy as np

class LearningWeb(object):
    def __init__(self,layersWidth=[]):
        self.layers = []
        self.weights = []
        for width in layersWidth:
            self.layers.append(np.array([0 for i in range(width)]))
        for layer in range(len(layersWidth)-1):
            self.weights.append(np.random.random((
                layersWidth[layer],layersWidth[layer+1]
            )))

        self.learningRate = 1

    def setLearningRate(self,rate):
        self.learningRate = rate

    def forward(self,inputLayer):
        layerCount = len(self.layers)
        if not layerCount:
            return 0
        self.layers[0] = inputLayer
        for layer in range(layerCount-1):
            self.layers[layer+1] = self.__sigmoid(self.layers[layer].dot(self.weights[layer]))
        return np.max(np.argwhere(self.layers[-1] == max(self.layers[-1])))

    def backward(self,outputExpect):
        #errors = []
        #deltas = []
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
                delta = error.dot(self.__sigmoidPrime(self.layers[opLayer]))
            self.weights[opLayer] += self.learningRate * self.layers[opLayer].dot(delta)

    def reward(self,rewardRate):
        layerCount = len(self.layers)
        if not layerCount:
            return 0
        lastOutput = self.layers[-1]
        maxIndex = np.argwhere(lastOutput == max(lastOutput))
        result = lastOutput.copy()
        result[maxIndex] = min(1,max(0,result[maxIndex] * (1 + rewardRate)))
        self.backward(result)

    def __sigmoid(self,array):
        return 1 / (1 + np.exp(-array))

    def __sigmoidPrime(self,array):
        return array * (1 - array)

