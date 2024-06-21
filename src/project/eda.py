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

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['record'],ax=ax)
    plt.title('Histo plot for Record Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record/record_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))


# Record column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['record'],ax=ax,color='r')
    plt.title('Distribution plot for Record Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record/record_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# Record column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['record'],ax=ax)
    plt.title('Box plot for Record Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record/record_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))


# Record column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['record'],ax=ax)
    plt.title('Scatter plot for Record Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record/record_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))



# Type Column:-

class type_column:

    try:

        type_unique=df['type'].unique()
        type_count=df['type'].value_counts()
        type_mode=df['type'].mode()[0]
        type_null=df['type'].isnull().sum()

    except Exception as e:
        raise Exception(f'Error find in type_column :\n'+str(e))

    def __init__(self, type_unique, type_count, type_mode, type_null):

        try:

            self.type_unique = type_unique
            self.type_count = type_count
            self.type_mode = type_mode
            self.type_null = type_null

        except Exception as e:
            raise Exception(f'Error find in type_column at init level :\n' + str(e))
        
    try: 

        def type_unique_column(self):
            return self.type_unique
        
        def type_count_column(self):
            return self.type_count
        
        def type_mode_column(self):
            return self.type_mode
        
        def type_null_column(self):
            return self.type_nul
        
    except Exception as e:
        raise Exception(f'Error find in type_column at function level :\n' + str(e))
    

# Type column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    plt.bar(x='type',data=df,height=0.8)
    plt.title('Bar plot for type column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/type/type_bar.png')

except Exception as e:
    raise Exception(f'error find in bar plot :\n'+str(e))

try:

    fig,ax=plt.subplots(figsize=(10,5))
    plt.pie(x=df['type'].value_counts(),labels=df['type'].unique(),autopct='%0.2f%%',explode=[0,0,0,0.5,0.8])
    plt.title('Pie plot for type column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/type/type_pie.png')

except Exception as e:
    raise Exception(f'error find in pie plot :\n'+str(e))


try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.countplot(data=df,x=df['type'],hue='type',ax=ax)
    plt.title('Count plot for type column')
    plt.legend(df['type'].unique())
    plt.legend(df['type'].value_counts())
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/type/type_count.png')

except Exception as e:
    raise Exception(f'error find in count plot :\n'+str(e))

