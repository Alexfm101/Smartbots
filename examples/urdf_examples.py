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
braccio = p.loadURDF('./smartbots/assets/Manipulators/braccio.urdf',startPos, startOrientation)


# obtener informacion de las articulaciones del robot
joints = p.getNumJoints(braccio) #me da el numero de articulaciones que hay ya sea de revolucion o traslacion
joints_info = p.getJointInfo(braccio,1) # me da info extra de las articulaciones



for _ in range(1000):
    p.stepSimulation()
    # p.setJointMotorControl2(braccio, 1, controlMode=p.POSITION_CONTROL,
    # targetPosition=40) #para controlar una sola articulacion
    time.sleep(1./240.)

cubePos, cubeOrn = p.getBasePositionAndOrientation(braccio)
print('position')
print('-----------------')
print(cubePos,cubeOrn)

print("joints")
print("----------------")
print(joints,joints_info)

# controlar al robot



p.disconnect()


# TODO: add collision to plane
