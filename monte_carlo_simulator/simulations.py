import numpy as np


def coin_flip_simulation(n_trials: int, p: float = 0.5) -> float:
    """
    Docstring for coin_flip_simulation
    
    :param n_trials: Number of Trials
    :type n_trials: int
    :param p: Convergence Value
    :type p: float
    :return: Average of Trials
    :rtype: float
    """
    flips = np.random.rand(n_trials) < p
    #Larger n will converge to p value
    return flips.mean()

def dice_expected_value_simulation(n_trials: int) -> float:
    """
    Docstring for dice_expected_value_simulation
    
    :param n_trials: Number of Trials
    :type n_trials: int
    :return: Estimated Expected Value
    :rtype: float
    """

    rolls = np.random.randint(1, 7, size = n_trials)
    return rolls.mean()

def at_least_one_six(n_trials: int, n_rolls: int) -> int:
    """
    Docstring for at_least_one_six
    
    :param n_trials: Description
    :type n_trials: int
    :param n_rolls: Description
    :type n_rolls: int
    :return: Description
    :rtype: int
    """
    
    successes = 0
    
    for _ in range(n_trials):
        rolls = np.random.randint(1, 7, size = n_rolls)
        
        if 6 in rolls:
            successes += 1

    return successes/n_trials