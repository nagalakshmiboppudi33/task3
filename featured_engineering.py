import pandas as pd
df=pd.read_csv("cleaned_data.csv")
#EMA 
df["EMA"] = df["ClosePrice"].ewm(span=10).mean()
#RSI 
def compute_rsi(close, period=14):
    delta=close.diff()
    gain=delta.clip(lower=0)
    loss=delta.clip(upper=0)
    avg_gain=gain.rolling(period).mean()
    avg_loss=loss.rolling(period).mean()
    rs=avg_gain / avg_loss
    rsi=100-(100/(1 + rs))
    return rsi
df["RSI_14"]=compute_rsi(df["ClosePrice"])
#MACD 
short_ema=df["ClosePrice"].ewm(span=12).mean()
long_ema=df["ClosePrice"].ewm(span=26).mean()
df["MACD"] = short_ema - long_ema
#Volatility 
df["Volatility"] = df["ClosePrice"].rolling(window=7).std()
#ATR(Average True Range)
df["H-L"]=df["HighPrice"]-df["LowPrice"]
df["H-PC"]=abs(df["HighPrice"]-df["ClosePrice"].shift(1))
df["L-PC"]=abs(df["LowPrice"]-df["ClosePrice"].shift(1))
df["TR"]=df[["H-L","H-PC","L-PC"]].max(axis=1)
df["ATR"]=df["TR"].rolling(14).mean()
print(df.head(20))
df.to_csv("featured.csv")
print("File saved in cleaned_data.csv")