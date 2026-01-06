import numpy as np
import matplotlib.pyplot as plt
from simulations import coin_flip_simulation


trials = np.logspace(1,5, num =20, dtype = int)
results = [coin_flip_simulation(n) for n in trials]

#Plot in a seperate window
plt.plot(trials, results, marker = 'o')
plt.axhline(0.5, linestyle = '--')
plt.xscale('log')
plt.xlabel('Number of Trials')
plt.ylabel("Estimated Probability of Heads")
plt.title("Monte Carlo COnvergence - Coin Flip")
plt.show()
