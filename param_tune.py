import numpy as np

import matplotlib.pyplot as plt

from main import run_simulation
from utils import get_args

if __name__ == "__main__":
  args = get_args()

  args.no_plot = True
  args.no_print = True

  errs = []
  acc_ws = np.linspace(0, 1.0, 101)
  for acc_w in acc_ws:
    args.filter_acc_weight = acc_w
    errs.append(run_simulation(args))

  title = "Error vs. Accelerometer Weight"
  plt.figure(title)
  plt.title(title)
  plt.plot(acc_ws, errs)
  plt.xlabel("Accel. Weight")
  plt.ylabel("Mean Abs. Err. (rad)")
  plt.show()
