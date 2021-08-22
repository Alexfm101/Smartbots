import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pybullet as p
import smartbots.utils.bullet as bullet

# VARIABLES INICIALES
#------------------------------
RESET_JOINT_VALUES = [1.57, -0.6, 0, -1.57, 0, 0, 0.5]
RESET_JOINT_INDICES = [0, 1, 2, 3, 4, 5, 6]

# AMBIENTE DEL BRACCIO
# -----------------------------

class BraccioEnv(gym.Env):
    metadata = {'render.modes':['human']}

    def __init__(self):
        self.reset_joint_indices = RESET_JOINT_VALUES 
        self.reset_joint_values = RESET_JOINT_INDICES
        self.id = 1
    
    def step(self,action):
        # TODO: 
            # crear las acciones
            # obtener la observation
            # dar la recompenza
            # indicar si se logro la tarea o no



        return observation, reward, done, info

    def reset(self):
        # resetear simulacion
        p.setRealTimeSimulation(False)
        p.resetSimulation()

        # dar las configuraciones iniciales del ambiente
        bullet.setup_init()

        # resetear las articulaciones del robot a su estado inicial
        bullet.reset_robot(
            self.id,
            self.reset_joint_indices,
            self.reset_joint_values
        )
        # TODO:crear robot_states
        # observacion del ambiente para el agente
        observation = {
            "braccio_states": robot_states
        }
        return observation
    
    def render(self, mode='human'):
    
    def close(self):
        p.disconnect()
    
