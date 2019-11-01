import numpy as np

class ComplementaryFilter:
  def __init__(self, acc_w, g, initial_angle):
    self.acc_w = acc_w
    self.g = g
    self.angle = initial_angle

  def get(self, acc, gyro, dt):
    ang_est_acc = np.arctan2(-acc[0], acc[1])
    ang_est_gyro = self.angle + gyro * dt

    self.angle = self.acc_w * ang_est_acc + (1 - self.acc_w) * ang_est_gyro
    return self.angle
