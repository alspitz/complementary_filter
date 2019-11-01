import argparse

def get_args():
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--gravity", default=9.81, type=float, required=False, help="Gravity acceleration (m/s^2)")
  parser.add_argument("--accel-stddev-x", default=0.5, type=float, required=False, help="Accel white noise stddev x")
  parser.add_argument("--accel-stddev-z", default=0.5, type=float, required=False, help="Accel white noise stddev z")
  parser.add_argument("--gyro-stddev", default=0.01, type=float, required=False, help="Gyro white noise stddev")
  parser.add_argument("--gyro-biasdrift-stddev", default=0.3, type=float, required=False, help="Gyro bias drift strength")
  parser.add_argument("--filter-acc-weight", default=0.2, type=float, required=False, help="Weight to place on accelerometer measurements [0-1]")
  parser.add_argument("--time", default=5.0, type=float, required=False, help="Duration of time to simulate (s)")
  parser.add_argument("--dt", default=0.005, type=float, required=False, help="Duration of time between samples (s)")
  parser.add_argument("--no-plot", action='store_true', required=False, help="Don't open plots of data")
  parser.add_argument("--no-print", action='store_true', required=False, help="Don't print mean abs. error on stdout")
  return parser.parse_args()

