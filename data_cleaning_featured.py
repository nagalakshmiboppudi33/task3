import pandas as pd
import numpy as np
df=pd.read_csv("NSE_BSE_data.csv")
#Convert date column
df["TradeDate"] = pd.to_datetime(df["TradeDate"])
df=df.set_index("TradeDate")
#Data cleaning 
for col in ["OpenPrice","HighPrice","LowPrice","ClosePrice","Volume"]:
    df[col] = pd.to_numeric(df[col])
print("Missing values before cleaning:")
print(df.isna().sum())
#Merging two datasets
merge=pd.read_csv("extra_dataset.csv")
merge["TradeDate"]=pd.to_datetime(merge["TradeDate"])
merge=merge.set_index("TradeDate")
merged=df.join(merge,lsuffix="_NSE",rsuffix="_BSE")
print(merged)
#Handling missing values
price_cols=["OpenPrice","HighPrice","LowPrice","ClosePrice"]
df[price_cols]=df[price_cols].ffill()       
df["Volume"]=df["Volume"].fillna(df["Volume"].mean())
print(df.isna().sum())
print(df)
df.to_csv("cleaned_data.csv" )
