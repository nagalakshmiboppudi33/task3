import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("featured.csv")
df=df.set_index("TradeDate")
#pricetrends
plt.plot(df["OpenPrice"])
plt.title("price trend")
plt.xlabel("Trade date")
plt.ylabel("open price")
plt.show()
#volumeanalysis
plt.plot(df["Volume"],color="black")
plt.title("volume Trend")
plt.xlabel("trade date")
plt.xlabel("volume")
plt.show()
#volatility
df["Vol_7"] = df["OpenPrice"]-df["ClosePrice"]
plt.plot(df["Vol_7"],color="red", marker='o')
plt.title("volatility trend")
plt.figure(figsize=(8,4))
plt.show()
#candlestick
plt.plot(df["HighPrice"]-df["LowPrice"], marker='o')
plt.title("High-low range")
plt.xlabel("trade date")
plt.ylabel("range")
plt.figure(figsize=(8,4))
plt.show()
