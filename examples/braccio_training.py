import gym
import smartbots

def main():
    env = gym.make('Braccio-v0')
    env.reset()
    for _ in range(1000):
        # env.render()
        action = env.actionSpace.sample()
        observation, reward, done, _ = env.step(action)
        if action == 0:
            action = 1
        else:
            action = 0

        print(action)
    env.close()

if __name__ == '__main__':
    main()
