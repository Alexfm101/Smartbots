import gym

ENVIROMENTS = (
    {
        'id':'Test-v0',
        'entry_point':'smartbots.enviroments.Test_Env:Test_Env'
    },
    {
        'id':'Driving-v0',
        'entry_point':'smartbots.enviroments.driving_0:Driving0'
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
