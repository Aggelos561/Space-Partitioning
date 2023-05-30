import numpy as np

def gen_random_points(size):
    rng = np.random.default_rng()
    return [tuple(p) for p in rng.uniform(0, 100, (size, 2)).astype(np.float64)]