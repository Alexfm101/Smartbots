import pybullet as p
import time
import pybullet_data
import os

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")
p.setGravity(0,0,-10)

startPos = [0,0,0.3]
startOrientation = p.getQuaternionFromEuler([0,0,0])
manipulator = p.loadURDF('./smartbots/assets/Manipulators/braccio.urdf',startPos, startOrientation)

while True:
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(manipulator)
print(cubePos,cubeOrn)
p.disconnect()
