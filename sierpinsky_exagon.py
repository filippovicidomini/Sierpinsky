# esemio

# vorrei creare un esagono di sierpinsky
import matplotlib.pyplot as plt
import numpy as np
from random import uniform, choice
from tqdm import tqdm

# set up the figure


uno: tuple = (1, 0)
due: tuple = (round(np.cos(np.pi / 3), 2), round(np.sin(np.pi / 3), 2))
tre: tuple = (round(np.cos(2 * np.pi / 3), 2), round(np.sin(2 * np.pi / 3), 2))
quattro: tuple = (round(np.cos(3 * np.pi / 3), 2), round(np.sin(3 * np.pi / 3), 2))
cinque: tuple = (round(np.cos(4 * np.pi / 3), 2), round(np.sin(4 * np.pi / 3), 2))
sei: tuple = (round(np.cos(5 * np.pi / 3), 2), round(np.sin(5 * np.pi / 3), 2))

angoli: list = [uno, due, tre, quattro, cinque, sei]

plt.plot(uno[0], uno[1], 'ro')
plt.plot(due[0], due[1], 'ro')
plt.plot(tre[0], tre[1], 'ro')
plt.plot(quattro[0], quattro[1], 'ro')
plt.plot(cinque[0], cinque[1], 'ro')
plt.plot(sei[0], sei[1], 'ro')

start = choice(angoli)
angoli.remove(start)
prima_scelta = choice(angoli)
angoli.append(start)
x, y = (0, 0)


def sierpinski():
    for i in range(len(angoli)):
        x = punto[i][0] - punto[i + 1][0]
        y = punto[i][1] - punto[i + 1][1]
        plt.plot(x, y, 'ro')
        plt.plot(x, y, 'ro')
        angoli.append((x, y))


for i in tqdm(range(1000)):
    for dot in angoli:
        x = round(2 / 3 * (start[0] - prima_scelta[0]), 2)
        y = round(2 / 3 * (start[1] - prima_scelta[1]), 2)

        plt.plot(x, y, 'bo', markersize=1)
    angoli.append((x, y))
    start = choice(angoli)
    angoli.remove(start)
    prima_scelta = choice(angoli)
    angoli.append(start)

plt.show()
