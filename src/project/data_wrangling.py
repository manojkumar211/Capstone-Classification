import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import boxcox
from sklearn.preprocessing import LabelEncoder
from data_cleaning import df
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor


# Discretization method:-

df['Age_category']=pd.cut(df['Age'],bins=[0,12,19,30,60,90],labels=['kids','teen_age','young_age','midle_age','senior_citizen'])



# Feature Transformation Methods:-

df['Pregnancies_root']=df['Pregnancies']**(1/1.791)
df['Glucose_root']=df['Glucose']**(1/9.99)
df['BloodPressure_root']=df['BloodPressure']**(1/1.238)
df['SkinThickness_root']=df['SkinThickness']**(1/2.679)
df['Insulin_root']=df['Insulin']**(1/6.72)
df['BMI_root']=df['BMI']**(1/3.29)
df['DiabetesPedigreeFunction_root']=df['DiabetesPedigreeFunction']**(1/38)
df['Age_box'],param=boxcox(df['Age'])


# Feature Encoding:-

df['Age_category1']=df['Age_category'].map({'kids':0,'teen_age':1,'young_age':2,'midle_age':3,'senior_citizen':4})


# Feature Scasling:-

X=df.iloc[:,[10,11,12,13,14,15,16,17]]
y=df['Outcome']

X_sc=StandardScaler()
X_scale=X_sc.fit_transform(X)


# VIF method:-

vif=pd.DataFrame()
vif['VIF']=[variance_inflation_factor(X_scale,i) for i in range(X_scale.shape[1])]
vif['Features']=X.columns

print(vif)







