import numpy as np
import pybullet as p


def connectSimulation(gui=False):
    if gui:
        p.connect(p.GUI)#version grafica
    else:
        p.connect(p.DIRECT)#version sin graficos

def connection_setup(timestep=1./240, solver_iterations=150, gravity=10):
    """
        This function defines how you connect with pybullet config.
        parameters:
            timestep(default:1/240)
            solver_iterations(default:150)
            gravity(default:10)
    """

    p.setPhysicsEngineParameter(numSolverIterations=solver_iterations)
    p.setTimeStep(timestep)
    p.setGravity(0,0,gravity)
    p.setRealTimeSimulation(False)
    p.stepSimulation()

def load_urdf(urdf=''):
    """
        This function load the urdf
    """
    p.loadURDF(urdf)

def setup_init(timestep=1./240, iterations=150, gravity=-9.5):
    """
        This function give an initial  setup to the reset
    """
    p.setPhysicsEngineParameter(numSolverIterations=iterations)
    p.setTimeStep(timestep)
    p.setGravity(0, 0, gravity)
    p.setRealTimeSimulation(False)
    p.stepSimulation()

def reset_robot(id, reset_joint_indices, reset_joint_values):
    """
        This function reset all the states of the joints of the robot
    """
    assert len(reset_joint_indices) == len(reset_joint_values)
    for i, value in zip(reset_joint_indices, reset_joint_values):
        p.resetJointState(id, i, value)


# control stuff
# ----------------------------

def jointStates(id,jointIndices):
    """
        This function get me all the position and velocities of the joints
    """
    jointStates = p.getJointStates(id,jointIndices)
    jointPositions, jointVelocities = [],[]
    for state in jointStates:
        jointPositions.append(state[0])
        jointVelocities.append(state[1])

    return jointPositions,jointVelocities
