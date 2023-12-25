"""build a random theory: how many times do you need to do something randomly to get the same result x number of times"""

import random
import matplotlib.pyplot as plt
import numpy as np


class Something():
    def __init__(self, numb_low, num_high, target):
        self.numb_low = numb_low
        self.numb_high = num_high
        self.target = target
        self.num = None
        self.i = 0
        x = np.array([self.i])
        y = np.array([self.num_of_tries])
        for i in range(self.num):
            self.randomizer(1, 1000, 5)
            x += self.randomizer
        plt.scatter(x, y)
        plt.show()

    def randomizer(self, num):
        self.num_of_tries = 0
        while True:
            random1 = random.randint(self.numb_low, self.num_high)
            self.num_of_tries += 1
            if random1 == self.target:
                print("hi")
            # return self.num_of_tries
            else:
                continue




