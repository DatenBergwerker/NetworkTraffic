import re
import pandas as pd

traffic = pd.read_csv(r"pathtocsv", header=None,
                      usecols=[0, 1, 2], names= ["date", "bytes_sent", "bytes_received"], index_col=0)

val_extr = re.compile(r"[A-Z_]*=([0-9]*)")
traffic.applymap = 