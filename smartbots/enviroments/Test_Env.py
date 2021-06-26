import gym
import numpy as np
import pybullet as p

class Test_Env(gym.Env):

    def __init__(self):
        self.client = p.connect(p.DIRECT)

    def reset(self):
        '''
        Initialization to start simulation. Loads all proper objects.
        '''

    def step(self, action):
        '''
        Applies an action and return environment information
        '''

    def render(self):
        '''
        Renders the environment.
        '''

    def close(self):
        '''
        Performs environment cleanup.
        '''

    def seed(self, seed=None):
        '''
        Takes an int seed to set randomly generated behavior.

        If None, generates a random seed. Returns seed value.
        '''
