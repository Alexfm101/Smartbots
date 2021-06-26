# import pybullet as p
# import time
# import pybullet_data
# import os

# p.connect(p.GUI)
# p.setGravity(0,0,-10)
# p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
#
# angle = p.addUserDebugParameter('Steering', -0.5, 0.5, 0)
# throttle = p.addUserDebugParameter('Throttle', 0, 20, 0)
# car = p.loadURDF('./smartbots/robots/simplecar.urdf', [0, 0, 0.1])
# plane = p.loadURDF('plane.urdf')
#
# wheel_indices = [1, 3, 4, 5]
# hinge_indices = [0, 2]
#
#
# while True:
#     user_angle = p.readUserDebugParameter(angle)
#     user_throttle = p.readUserDebugParameter(throttle)
#     for joint_index in wheel_indices:
#         p.setJointMotorControl2(car, joint_index,
#                                 p.VELOCITY_CONTROL,
#                                 targetVelocity=user_throttle)
#     for joint_index in hinge_indices:
#         p.setJointMotorControl2(car, joint_index,
#                                 p.POSITION_CONTROL,
#                                 targetPosition=user_angle)
#     p.stepSimulation()


# physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
# p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
# p.setGravity(0,0,-10)
# planeId = p.loadURDF("plane.urdf")
# startPos = [0,0,1]
# startOrientation = p.getQuaternionFromEuler([0,0,0])
# boxId = p.loadURDF('./smartbots/robots/manipulator.urdf',startPos, startOrientation)
# #set the center of mass frame (loadURDF sets base link frame)
# # startPos/   Ornp.resetBasePositionAndOrientation(boxId,startPos,startOrientation)
# while True:
#     p.stepSimulation()
#     time.sleep(1./240.)
# cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
# print(cubePos,cubeOrn)
# p.disconnect()


'''
Runs driving-v0 OpenAI gym environment.
'''

import gym
import smartbots
import matplotlib.pyplot as plt


def reward_func(end, rew):
    return 10
    if end:
        return 100 if rew[0] > 0 else -100

    return rew[0] if rew[0] > 0 else 0

def main():
    env = gym.make('Driving-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())
    env.close()
if __name__ == '__main__':
    main()
