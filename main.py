import argparse

import numpy as np

from accel import Accel
from est import ComplementaryFilter
from gyro import Gyro
from utils import get_args

def run_simulation(args):
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

  if not args.no_print:
    print("Mean abs error is %f radians (%f degrees)" % (mean_abs_error, np.degrees(mean_abs_error)))

  if not args.no_plot:
    import matplotlib.pyplot as plt

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

  return mean_abs_error

if __name__ == "__main__":
  run_simulation(get_args())
