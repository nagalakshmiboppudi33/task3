import pandas as pd
import numpy as np
df = pd.read_csv("featured.csv")
#Closer prices and charges
price = df["ClosePrice"]
df["EMA(large)"] = price.ewm(span=5).mean()
df["EMA(small)"] = price.ewm(span=3).mean()
#trading signals
df["Signal"] = 0
df.loc[df["EMA(small)"] > df["EMA(large)"], "Signal"] = 1
df.loc[df["EMA(small)"] < df["EMA(large)"], "Signal"] = -1   
#strategy
df["return diff"] = price.diff()
df["strat_return"] = df["Signal"].shift(1) * df["return diff"]
#profit/loss
total = df["strat_return"].sum()
#trades count
trades = df["Signal"].diff().abs().sum() / 2
#win_ratio
wins = (df["strat_return"]>0).sum()
tot_trades = (df["strat_return"] != 0).sum()
winratio = wins / tot_trades if tot_trades != 0 else 0
#accuracy
accuracy = wins / tot_trades if tot_trades != 0 else 0
#drawdown calculation
cumul = df["strat_return"].cumsum()
drawdown = cumul - cumul.cummax()
max_drawdown = drawdown.min()
print("accuracy:",accuracy)
print("profit/loss:",total)
print("drawdown:",max_drawdown)
print("no of trades:",trades)
print("win ratio:",winratio)



