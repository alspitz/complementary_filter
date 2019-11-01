import numpy as np

import matplotlib.pyplot as plt

class Gyro:
  def __init__(self, stddev, biasdrift_stddev):
    self.stddev = stddev
    self.biasdrift_stddev = biasdrift_stddev
    self.reset()

  def reset(self):
    self.bias = 0
    self.biases = []

  def get(self, angvel, dt):
    self.bias += dt * np.random.normal(0, scale=self.biasdrift_stddev)
    self.biases.append(self.bias)
    return angvel + self.bias + np.random.normal(0, scale=self.stddev)

  def plot(self, ts, data):
    title = "Gyroscope Data"
    plt.figure(title)
    plt.plot(ts, data, label="Data")
    plt.plot(ts, self.biases, label="Bias")
    plt.ylabel("Gyro (rad/s)")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.title(title)
