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
        p.loadURDF("plane.urdf") #TODO:agregar piso
        self.indices = list(range(0,p.getNumJoints(self.id)))




    def step(self,action):
        # TODO:
            # crear las acciones
            # obtener la observation
            # dar la recompenza
            # indicar si se logro la tarea o no



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

        # generar la observacion del ambiente
        braccio_joints_positions, braccio_joints_velocities = bullet.jointStates(self.id, self.indices)

        # observacion del ambiente para el agente
        observation = {
            "braccio_joints_positions": braccio_joints_positions,
            "braccio_joints_velocities": braccio_joints_velocities
        }

        return observation

    def render(self, mode='human'):
        pass

    def close(self):
        p.disconnect()
