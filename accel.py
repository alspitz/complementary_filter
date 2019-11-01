import numpy as np

import matplotlib.pyplot as plt

class Accel:
  def __init__(self, stddevs, g):
    self.stddev = np.array(stddevs)
    self.g_vec = np.array((0, g))
    self.reset()

  def reset(self):
    self.true_accs = []

  def get(self, angle):
    rot = np.array((
      (np.cos(angle), -np.sin(angle)),
      (np.sin(angle), np.cos(angle))
    ))

    acc_true = rot.dot(self.g_vec)
    self.true_accs.append(acc_true)

    return acc_true + np.random.normal(0, scale=self.stddev, size=2)

  def plot(self, ts, data):
    title = "Accelerometer Data"

    true_accs = np.array(self.true_accs)

    plt.figure(title)
    plt.subplot(2, 1, 1)
    plt.plot(ts, data[:, 0], label="Data")
    plt.plot(ts, true_accs[:, 0], label="True")
    plt.ylabel("Accel X (m/s$^2$)")
    plt.title(title)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(ts, data[:, 1], label="Data")
    plt.plot(ts, true_accs[:, 1], label="True")
    plt.ylabel("Accel Z (m/s$^2$)")

    plt.xlabel("Time (s)")
