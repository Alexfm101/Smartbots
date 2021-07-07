import numpy as np
import pybullet as p

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
