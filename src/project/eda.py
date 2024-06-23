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



try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['record','type_new']].corr(),annot=True,cmap='CMRmap',ax=ax)
    plt.title('HeatMap plot for record Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/record/record_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))




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




# 0_pre-RR column:-

class pre_RR0_column:

    try:

        pre_RR0_des=df['0_pre-RR'].describe()
        pre_RR0_null=df['0_pre-RR'].isnull().sum()
        pre_RR0_skewness=df['0_pre-RR'].skew()
        pre_RR0_var=df['0_pre-RR'].var(ddof=0)
        pre_RR0_std=df['0_pre-RR'].std(ddof=0)
        pre_RR0_cov=df[['0_pre-RR','type_new']].cov()
        pre_RR0_corr=df[['0_pre-RR','type_new']].corr()

    except Exception as e:
        raise Exception(f'Error find in pre_RR1_column :\n'+str(e))
    

    def __init__(self,pre_RR0_des,pre_RR0_null,pre_RR0_skewness,pre_RR0_var,pre_RR0_std,pre_RR0_cov,pre_RR0_corr):

        try:

            self.pre_RR0_des=pre_RR0_des
            self.pre_RR0_null=pre_RR0_null
            self.pre_RR0_skewness=pre_RR0_skewness
            self.pre_RR0_var=pre_RR0_var
            self.pre_RR0_std=pre_RR0_std
            self.pre_RR0_cov=pre_RR0_cov
            self.pre_RR0_corr=pre_RR0_corr

        except Exception as e:
            raise Exception(f'Error find in pre_RR1_column at init level :\n' + str(e))

    try:

        def pre_RR0_des_column(self):
            return self.pre_RR0_des
        
        def pre_RR0_null_column(self):
            return self.pre_RR0_null
        
        def pre_RR0_skewness_column(self):
            return self.pre_RR0_skewness
        
        def pre_RR0_var_column(self):
            return self.pre_RR0_var
        
        def pre_RR0_std_column(self):
            return self.pre_RR0_std
        
        def pre_RR0_cov_column(self):
            return self.pre_RR0_cov
        
        def pre_RR0_corr_column(self):
            return self.pre_RR0_corr
        
    except Exception as e:
        raise Exception(f'Error find in pre_RR1_column at function level :\n' + str(e))
    
    
# 0_pre-RR column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['0_pre-RR'],ax=ax)
    plt.title('Histo plot for 0_pre-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pre-RR/0_pre-RR_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# 0_pre-RR column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['0_pre-RR'],ax=ax,color='r')
    plt.title('Distribution plot for 0_pre-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pre-RR/0_pre-RR_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# 0_pre-RR column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['0_pre-RR'],ax=ax)
    plt.title('Box plot for 0_pre-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pre-RR/0_pre-RR_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# 0_pre-RR column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['0_pre-RR'],ax=ax)
    plt.title('Scatter plot for 0_pre-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pre-RR/0_pre-RR_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))


# 0_pre-RR column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['0_pre-RR','type_new']].corr(),annot=True,cmap='gist_ncar',ax=ax)
    plt.title('HeatMap plot for 0_pre-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pre-RR/0_pre-RR_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))



# 0_post-RR column analysis:-

class post_RR0_column:

    try:

        post_RR0_des=df['0_post-RR'].describe()
        post_RR0_null=df['0_post-RR'].isnull().sum()
        post_RR0_skewness=df['0_post-RR'].skew()
        post_RR0_var=df['0_post-RR'].var(ddof=0)
        post_RR0_std=df['0_post-RR'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in post_RR1_column :\n'+str(e))
    

    def __init__(self,post_RR0_des,post_RR0_null,post_RR0_skewness,post_RR0_var,post_RR0_std):

        try:

            self.post_RR0_des=post_RR0_des
            self.post_RR0_null=post_RR0_null
            self.post_RR0_skewness=post_RR0_skewness
            self.post_RR0_var=post_RR0_var
            self.post_RR0_std=post_RR0_std

        except Exception as e:
            raise Exception(f'Error find in post_RR1_column at init level :\n' + str(e))
        

    try:

        def post_RR0_des_column(self):
            return self.post_RR0_des
        
        def post_RR0_null_column(self):
            return self.post_RR0_null
        
        def post_RR0_skewness_column(self):
            return self.post_RR0_skewness
        
        def post_RR0_var_column(self):
            return self.post_RR0_var
        
        def post_RR0_std_column(self):
            return self.post_RR0_std
        
    except Exception as e:
        raise Exception(f'Error find in post_RR1_column at function level :\n' + str(e))
    
# 0_post-RR column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['0_post-RR'],ax=ax)
    plt.title('Histo plot for 0_post-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_post-RR/0_post-RR_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# 0_post-RR column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['0_post-RR'],ax=ax,color='r')
    plt.title('Distribution plot for 0_post-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_post-RR/0_post-RR_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# 0_post-RR column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['0_post-RR'],ax=ax)
    plt.title('Box plot for 0_post-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_post-RR/0_post-RR_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# 0_post-RR column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['0_post-RR'],ax=ax)
    plt.title('Scatter plot for 0_post-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_post-RR/0_post-RR_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))

# 0_post-RR column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['0_post-RR','type_new']].corr(),annot=True,cmap='OrRd',ax=ax)
    plt.title('HeatMap plot for 0_post-RR Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_post-RR/0_post-RR_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))

    

# 0_pPeak column analysis:

class pPeak0_column:

    try:

        pPeak0_des=df['0_pPeak'].describe()
        pPeak0_null=df['0_pPeak'].isnull().sum()
        pPeak0_skewness=df['0_pPeak'].skew()
        pPeak0_var=df['0_pPeak'].var(ddof=0)
        pPeak0_std=df['0_pPeak'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in pPeak1_column :\n'+str(e))
    

    def __init__(self,pPeak0_des,pPeak0_null,pPeak0_skewness,pPeak0_var,pPeak0_std):

        try:

            self.pPeak0_des=pPeak0_des
            self.pPeak0_null=pPeak0_null
            self.pPeak0_skewness=pPeak0_skewness
            self.pPeak0_var=pPeak0_var
            self.pPeak0_std=pPeak0_std

        except Exception as e:
            raise Exception(f'Error find in pPeak1_column at init level :\n' + str(e))
        
    try:

        def pPeak0_des_column(self):
            return self.pPeak0_des
        
        def pPeak0_null_column(self):
            return self.pPeak0_null
        
        def pPeak0_skewness_column(self):
            return self.pPeak0_skewness
        
        def pPeak0_var_column(self):
            return self.pPeak0_var
        
        def pPeak0_std_column(self):
            return self.pPeak0_std
        
    except Exception as e:
        raise Exception(f'Error find in pPeak1_column at function level :\n' + str(e))
    
    
# 0_pPeak column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['0_pPeak'],ax=ax)
    plt.title('Histo plot for 0_pPeak Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pPeak/0_pPeak_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# 0_pPeak column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['0_pPeak'],ax=ax,color='r')
    plt.title('Distribution plot for 0_pPeak Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pPeak/0_pPeak_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# 0_pPeak column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['0_pPeak'],ax=ax)
    plt.title('Box plot for 0_pPeak Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pPeak/0_pPeak_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# 0_pPeak column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['0_pPeak'],ax=ax)
    plt.title('Scatter plot for 0_pPeak Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pPeak/0_pPeak_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))

# 0_pPeak column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['0_pPeak','type_new']].corr(),annot=True,cmap='cividis',ax=ax)
    plt.title('HeatMap plot for 0_pPeak Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/0_pPeak/0_pPeak_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))



