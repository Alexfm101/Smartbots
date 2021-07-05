import gym

ENVIROMENTS = (
    {
        'id':'Driving-v0',
        'entry_point':'smartbots.enviroments.driving_0:Driving0'
    },
    {
        'id': 'RobotArm-v0',
        'entry_point':'smartbots.enviroments.RobotArm_Env:RobotArmEnv'
    }
)

def register_environments():
    for env in ENVIROMENTS:
        gym.register(**env)

    gym_ids = tuple(
        environment['id']
        for environment in ENVIROMENTS
    )

    return gym_ids

def make(enviroment,*args,**kwargs):
    env = gym.make(environment, *args, **kwargs)
    return env
