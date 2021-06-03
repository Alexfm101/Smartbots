import pybullet as p
import time
import pybullet_data
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")

p.loadURDF('./Controllers/manipulator.urdf')

for i in range(100000000000000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()
