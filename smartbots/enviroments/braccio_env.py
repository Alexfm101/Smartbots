import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pybullet as p
import pybullet_data
import smartbots.utils.bullet as bullet

# VARIABLES INICIALES
#------------------------------
RESET_JOINT_VALUES = [1.57, 0.6, 0., 1.57, 0., 0., 0.5,0.]
RESET_JOINT_INDICES = [0, 1, 2, 3, 4, 5, 6,7]

# AMBIENTE DEL BRACCIO
# -----------------------------

class BraccioEnv(gym.Env):
    metadata = {'render.modes':['human']}

    def __init__(self,gui=True):

        self.reset_joint_indices = RESET_JOINT_INDICES
        self.reset_joint_values = RESET_JOINT_VALUES
        self.gui = gui

        bullet.connectSimulation(gui=self.gui)

        self.id =  p.loadURDF('./smartbots/assets/Manipulators/braccio.urdf',
                        basePosition=[0,0,0],
                        baseOrientation=p.getQuaternionFromEuler([0,0,0])
                        )
        # p.loadURDF("plane.urdf") #TODO:agregar piso
        self.indices = list(range(0,p.getNumJoints(self.id)))

        # espacion de acciones posibles
        self.actionSpace = spaces.Discrete(3)

    def step(self,action):

        # crear las acciones
        if action == 0:
            p.setJointMotorControl2(self.id, self.reset_joint_indices[6],controlMode=p.POSITION_CONTROL)
        elif action == 1:
            p.setJointMotorControl2(self.id,self.reset_joint_indices[6],controlMode=p.POSITION_CONTROL)
        elif action ==2:
            p.setJointMotorControl2(self.id,self.reset_joint_indices[6],controlMode=p.POSITION_CONTROL)

        # obtener la observation
        observation = self.getObservation()
        # dar la recompenza
        reward = self.getReward()
        # indicar si se logro la tarea o no
        done = False
        # info
        info = self.getInfo()

        return observation, reward, done, info

    def reset(self):

        # dar las configuraciones iniciales del ambiente
        bullet.setup_init()

        # resetear las articulaciones del robot a su estado inicial
        bullet.reset_robot(
            self.id,
            self.reset_joint_indices,
            self.reset_joint_values
        )

        # obtener observacion
        observation = self.getObservation()

        return observation

    def render(self, mode='human'):
        pass

    def close(self):
        p.disconnect()


    # enviroments methods
    # ------------------


    def getObservation(self):
        # me devuelve la posicion y velocidad de las articulaciones
        positions, velocities = bullet.jointStates(self.id, self.indices)

        observation = {
            "joints_position": positions,
            "joints_velocities": velocities
        }
        return observation

    def getReward(self):
        reward = -1.
        return reward

    def getInfo(self):
        info  = {}
        return info
