# AI For self driving car

# libraries

import numpy as np
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

class Network(nn.Module):
    def __init__(self, input_size, ):
        super(Network,self).__init__()
        self.input_size = input_size
        self.nb_action = nb_action 
        self.fc1 = nn.Linear(input_size, 30)
        self.fc2 = nn.Linear(30, nb_action)
        
    def forward(self, state):
        X = F.relu(self.fc1(state))
        q_values = self.fc2(X)
        return q_values
    
# Implementing Experience Replay

class ReplayMemory(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        
    def push(self, event):
        self.memory.append(event)
        if len(self.memory) > self.capacity:
            del self.memory[0]
            
            
            
            
        