import random
import matplotlib.pyplot as plt

def random_walk(number_of_steps: int) -> [int, ...]:
    x, y = 0, 0
    steps = [(x, y)]
    for _ in range(number_of_steps):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        x += dx
        y += dy
        steps.append((x, y))
    return steps

if __name__ == '__main__':
    for _ in range(50): # different paths
        steps = random_walk(2000)
        steps = list(zip(*steps))
        plt.scatter(*steps)
        plt.plot(*steps)
    plt.show()
