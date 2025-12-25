import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
df=pd.read_csv("featured.csv")
#missing values handling
df.fillna(0,inplace=True)
# Create target variable
df["Next_close"]=df["ClosePrice"].shift(-1)
df["Movement"]=(df["Next_close"] > df["ClosePrice"]).astype(int)
df.dropna(inplace=True)
#features used
X=df[["ClosePrice","Volume","EMA","RSI_14","MACD"]]
y=df["Movement"]
#data spliting
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#scale features
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
#XGboost Model
xgb=XGBClassifier(n_estimators=20, learning_rate=0.3,max_depth=2, eval_metric="logloss", random_state=42)
xgb.fit(X_train, y_train)
print("XG boost accuracy",accuracy_score(y_test, xgb.predict(X_test)))
#Random Forest Model
rf=RandomForestClassifier(n_estimators=200,max_depth=5,random_state=42)
rf.fit(X_train, y_train)
print("Random forest accuracy:",accuracy_score(y_test, rf.predict(X_test)))
