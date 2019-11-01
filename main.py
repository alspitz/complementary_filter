import argparse

import numpy as np

import matplotlib.pyplot as plt

from accel import Accel
from est import ComplementaryFilter
from gyro import Gyro

if __name__ == "__main__":
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--gravity", default=9.81, type=float, required=False, help="Gravity acceleration (m/s^2)")
  parser.add_argument("--accel-stddev-x", default=0.5, type=float, required=False, help="Accel white noise stddev x")
  parser.add_argument("--accel-stddev-z", default=0.5, type=float, required=False, help="Accel white noise stddev z")
  parser.add_argument("--gyro-stddev", default=0.01, type=float, required=False, help="Gyro white noise stddev")
  parser.add_argument("--gyro-biasdrift-stddev", default=0.3, type=float, required=False, help="Gyro bias drift strength")
  parser.add_argument("--filter-acc-weight", default=0.2, type=float, required=False, help="Weight to place on accelerometer measurements [0-1]")
  parser.add_argument("--time", default=5.0, type=float, required=False, help="Duration of time to simulate (s)")
  parser.add_argument("--dt", default=0.005, type=float, required=False, help="Duration of time between samples (s)")
  args = parser.parse_args()

  t_end = args.time
  dt = args.dt
  start_angle = 0.05

  accel = Accel((args.accel_stddev_x, args.accel_stddev_z), args.gravity)
  gyro = Gyro(args.gyro_stddev, args.gyro_biasdrift_stddev)
  filt = ComplementaryFilter(args.filter_acc_weight, args.gravity, start_angle)

  accel_data = []
  gyro_data = []
  angles = []

  true_angle = start_angle
  true_angvel = 0.0

  ts = np.arange(0, t_end, dt)
  true_angles = true_angle * np.ones(shape=ts.shape)

  for i, t in enumerate(ts):
    acc_obs = accel.get(true_angles[i])
    angvel_obs = gyro.get(true_angvel, dt)

    accel_data.append(acc_obs)
    gyro_data.append(angvel_obs)

    ang_est = filt.get(acc_obs, angvel_obs, dt)

    angles.append(ang_est)

  angles = np.array(angles)

  angle_error = angles - true_angles
  mean_abs_error = np.mean(np.abs(angle_error))
  print("Mean abs error is %f radians (%f degrees)" % (mean_abs_error, np.degrees(mean_abs_error)))

  plt.figure("Filter Results")
  plt.plot(ts, angles, label='Estimated')
  plt.plot(ts, true_angles, label='True')
  plt.xlabel('Time (s)')
  plt.ylabel('Angle (rad)')
  plt.title("Estimated vs. True Angle")
  plt.legend()

  plt.figure("Angle Error")
  plt.plot(ts, angle_error)
  plt.xlabel('Time (s)')
  plt.ylabel('Angle Error (rad)')
  plt.title("Angle Error")

  accel_data = np.array(accel_data)
  accel.plot(ts, accel_data)
  gyro_data = np.array(gyro_data)
  gyro.plot(ts, gyro_data)
  plt.show()
