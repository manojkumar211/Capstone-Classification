import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df


# Column wise Analysis:

class record_column:
        
    try:

        record_unique=df['record'].unique()
        record_des=df['record'].describe()
        record_null=df['record'].isnull().sum()
        record_mode=df['record'].mode()[0]
        record_skew=df['record'].skew()
        record_var=df['record'].var(ddof=0)
        record_std=df['record'].std(ddof=0)
        record_corr=df[['record','type_new']].corr()

    except Exception as e:
        raise Exception(f'Error find in record_column :\n'+str(e))

  

    def __init__(self,record_unique,record_des,record_null,record_mode,record_skew,record_var,record_std,record_corr):

        try:
        
            self.record_unique=record_unique
            self.record_des=record_des
            self.record_null=record_null
            self.record_mode=record_mode
            self.record_skew=record_skew
            self.record_var=record_var
            self.record_std=record_std
            self.record_corr=record_corr
        
        except Exception as e:
            raise Exception(f'Error find in record_column at init level :\n'+str(e))

    
    try:

        def record_unique_column(self):
            return self.record_unique
        
        def record_des_column(self):
            return self.record_des
        
        def record_null_column(self):
            return self.record_null
        
        def record_mode_column(self):
            return self.record_mode
        
        def record_skew_column(self):
            return self.record_skew
        
        def record_var_column(self):
            return self.record_var
        
        def record_std_column(self):
            return self.record_std
        
        def record_corr_column(self):
            return self.record_corr
    
    except Exception as e:
        raise Exception(f'Error find in record_column at function level :\n'+str(e))
    
    
    

# Record column histo plot:

fig,ax=plt.subplots(figsize=(5,5))
sns.histplot(data=df['record'],ax=ax)
plt.title('Histo plot for Record Column')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record_histo.png')


# Record column distribution plot:

fig,ax=plt.subplots(figsize=(5,5))
sns.kdeplot(data=df['record'],ax=ax,color='r')
plt.title('Distribution plot for Record Column')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record_dist.png')

# Record column box plot:

fig,ax=plt.subplots(figsize=(5,5))
sns.boxplot(data=df['record'],ax=ax)
plt.title('Box plot for Record Column')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record_box.png')


# Record column scatter plot:

fig,ax=plt.subplots(figsize=(5,5))
sns.scatterplot(data=df['record'],ax=ax)
plt.title('Scatter plot for Record Column')
plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record_scatter.png')



   