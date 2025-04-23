import numpy as np

from tasadofi.random_number import RndFloat


class Signal:
    def __init__(self, noise=0.1):
        self.noise = noise

    def generate_signal(self, length=100):
        # code to generate some signal
        # ...
        signal = np.linspace(0, length / 2 * np.pi, length)  # Example signal: a sine wave
        signal = np.sin(signal)  # Example signal: a sine wave
        signal += self.noise
        return signal


signal = Signal()
for _ in range(2):
    print(signal.generate_signal(length=5))
    # [ 0.1 1.02387953 -0.60710678 -0.28268343  1.1 ]
    # [ 0.1 1.02387953 -0.60710678 -0.28268343  1.1 ]

signal = Signal(noise=RndFloat('uniform', 0, 0.5))
for _ in range(2):
    print(signal.generate_signal(length=5))
    # [ 0.13548616  1.0593657  -0.57162062 -0.24719727  1.13548616]
    # [ 0.08913056  1.01301009 -0.61797623 -0.29355288  1.08913056]

print(signal.noise)
# sampler uniform(0, 0.5)
# last 10 generated values [0.13548616468953223, 0.08913055526374658]
