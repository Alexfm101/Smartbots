'''
This is the first try of robot arm enviroment :)
'''

import gym
import pybullet as p
import numpy as np
import smartbots.utils.bullet as bullet


class RobotArmEnv(gym.Env):
    """docstring for RobotArmEnv."""

    def __init__(self, arg, client=p.DIRECT, robot):
        super(RobotArmEnv, self).__init__()
        self.arg = arg
        self.client = p.connect(client)
        self.robot = robot

    # initialization to start simulation
    def reset(self):
        p.resetSimulation(self.client)
        p.setRealTimeSimulation(False)
        p.resetSimulation()
        bullet.connection_setup()
        bullet.load_urdf(self.robot)

        return self.get_observation()



    # applies an action and return environment information
    def step(self, action):
        pass

    # render the environment
    def render(self):
        pass

    # clean de performs environment
    def close(self):
        p.disconnect()

    def get_observation(self):
        # TODO: terminar de definir observation
        observation = {}
        return observation
