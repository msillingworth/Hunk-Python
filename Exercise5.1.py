import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web
import datetime.datetime

start = datetime(2000,1,1)
end = datetime(2014,4,14)
tkr = "aapl"

apple = web.DataReader(tkr, "google", start=start, end=end)

apple["Close"].plot(grid=True, figsize=(8,5))
plt.show()
