import re
import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv(r"C:\Users\Lenovo\Dropbox\Projects\traffic.csv", header=None,
                      usecols=[0, 1, 2], names=["date", "bytes_sent", "bytes_received"])
#, index_col=0)

traffic["date"] = traffic["date"].apply(pd.to_datetime)
traffic.set_index("date", inplace=True)
val_extr = re.compile(r"[A-Z_]*=([0-9]*)")
traffic = traffic.applymap(lambda x: val_extr.search(x).groups(1)[0])
traffic = traffic.applymap(pd.to_numeric)
traffic = traffic.diff()
traffic = traffic.applymap(lambda x: x / 1024**2)
traffic_10 = traffic.resample("10min").sum()

traffic_10.plot(x=traffic_10.index, y="bytes_received")
plt.show()