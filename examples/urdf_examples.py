import pybullet as p
import time
import pybullet_data
import os
import math
import numpy as np

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")
p.setGravity(0,0,-10)
radians = 2*math.pi/360
startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])
braccio = p.loadURDF('./smartbots/assets/Manipulators/braccio.urdf',startPos, startOrientation)

# obtener informacion de las articulaciones del robot
joints = p.getNumJoints(braccio) #me da el numero de articulaciones que hay ya sea de revolucion o traslacion
joints_info = p.getJointInfo(braccio,1) # me da info extra de las articulaciones

# obtener articulaciones movibles
def get_movable_joints(id):
    joints = p.getNumJoints(id)
    movable_joints = []
    for i in range(joints):
        if p.getJointInfo(id,i)[2] != p.JOINT_FIXED:
            movable_joints.append(i)

    return movable_joints

def get_joint_states(id, joint_indices):
    all_joint_states = p.getJointStates(id, joint_indices)
    joint_positions, joint_velocities = [], []
    for state in all_joint_states:
        joint_positions.append(state[0])
        joint_velocities.append(state[1])

    return np.asarray(joint_positions), np.asarray(joint_velocities)

print(get_joint_states(braccio,list(range(0,p.getNumJoints(braccio)))))
# resetear las posiciones iniciales de las articulaciones del braccio
p.resetJointState(braccio,1,90*radians)
p.resetJointState(braccio,2,90*radians)
p.resetJointState(braccio,3,90*radians)
p.resetJointState(braccio,4,120*radians)
p.resetJointState(braccio,7,90*radians)

movable_joints = get_movable_joints(braccio)

for _ in range(1000):
    p.stepSimulation()
    # p.setJointMotorControl2(braccio, 1, controlMode=p.POSITION_CONTROL,
    # targetPosition=40) #para controlar una sola articulacion
    p.setJointMotorControl2(braccio, 2, controlMode=p.POSITION_CONTROL,targetPosition=120,maxVelocity=2.)
    # print(p.getJointState(braccio,2))

    time.sleep(1./240.)

cubePos, cubeOrn = p.getBasePositionAndOrientation(braccio)

print(p.getBasePositionAndOrientation(braccio))



p.disconnect()


# TODO: add collision to plane
