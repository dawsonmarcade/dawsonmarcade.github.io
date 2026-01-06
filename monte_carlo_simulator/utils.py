import numpy as np

def bootstrap_ci(data, n_bootstrap = 1000, alpha = 0.5):
    """
    Docstring for bootstrap_ci
    
    :param data: Description
    :param n_bootstrap: Description
    :param alpha: Description
    """
    
    boot_means = [
        np.means(np.random.choice(data, size=len(data), replace = True))
        for _ in range(n_bootstrap)

    ]
    lower = np.percentile(boot_means, 100 * alpha / 2)
    upper = np.percentile(boot_means, 100* (1 - (alpha / 2)))
    return lower, upper