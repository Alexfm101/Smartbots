'''
This is the first try of robot arm enviroment :)
'''

import gym
import pybullet as bullet
import numpy as np


class RobotArmEnv(gym.Env):
    """docstring for RobotArmEnv."""

    def __init__(self, arg):
        super(RobotArmEnv, self).__init__()
        self.arg = arg

    # initialization to start simulation
    def reset(self):
        pass

    # applies an action and return environment information
    def step(self, action):
        pass

    # render the environment
    def render(self):
        pass

    # clean de performs environment
    def close(self):
        pass
