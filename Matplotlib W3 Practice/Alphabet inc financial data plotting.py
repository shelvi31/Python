import matplotlib.pyplot as plt
import numpy
import pandas as pd

print(plt.style.available)

# plt.figure(figsize=(10,10))
# df = pd.read_csv("fdata.csv")
# df.plot()
# plt.xlabel("OCT 2016")
# plt.ylabel("achievements")
# plt.show()

month = ["Jan","Feb","March","April"]
sales =[34,23,42,11]
plt.plot(month,sales,"b--o")
plt.tight_layout()
plt.grid()
plt.show()





