import gym
import smartbots

def main():
    env = gym.make('Braccio-v0')
    env.reset()
    action = 0
    for _ in range(1000):
        print(env.reset())
        # env.render()
        observation, reward, done, _ = env.step(0)
        if action == 0:
            action = 1
        else:
            action = 0
            
        print(observation)
        print(reward)
    env.close()

if __name__ == '__main__':
    main()
