import gym
import smartbots

def main():
    env = gym.make('Braccio-v0')

    for episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()

            action = env.actionSpace.sample()

            observation, reward, done, info = env.step(action)
            if done:
                print('Episode finished after {} timesteps'.format(t+1))
                break
    env.close()

if __name__ == '__main__':
    main()
