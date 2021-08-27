import gym
import smartbots

def main():
    env = gym.make('Braccio-v0')
    env.reset()
    for _ in range(1000):
        print(env.reset())
        # env.render()
        # env.step(env.action_space.sample())
    env.close()

if __name__ == '__main__':
    main()
