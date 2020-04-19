import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_boston
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import  PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

data = load_boston()
df = pd.DataFrame( data.data, columns= data.feature_names)
# print(df.head())
df['target'] = data.target

# print(df.corr()['target'])

feature = ['RM', 'LSTAT']

X = df[feature]
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=50, random_state=42)

model = Pipeline([
    ('scale', StandardScaler()),
    ('quadratic', PolynomialFeatures(degree=2)),
    ('predictor', LinearRegression())
])

model.fit(X_train, y_train)

# print('Training evaluation', model.score(X_train, y_train))
# print('Testing evaluation', model.score(X_test, y_test))
