import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the data:

df=pd.read_csv("C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/Arrhythmia.csv")


class data_des:

    try:
    
        df_head=df.head()
        df_shape=df.shape
        df_tail=df.tail()
        df_columns=df.columns
        df_des=df.describe()
        df_type=df.dtypes
        df_duplicate=df.duplicated().sum()
        df_null=df.isnull().sum()
        df_unique=df.nunique()

    except Exception as e:
        raise Exception(f'Error find in data descriptor :\n'+str(e))

    def __init__(self,df_head,df_shape,df_tail,df_columns,df_des,df_type,df_duplicate,df_null,df_unique):

        try:

            self.df_head=df_head
            self.df_shape=df_shape
            self.df_tail=df_tail
            self.df_columns=df_columns
            self.df_des=df_des
            self.df_type=df_type
            self.df_duplicate=df_duplicate
            self.df_null=df_null
            self.df_unique=df_unique

        except Exception as e:
            raise Exception(f'Error find in data init level :\n'+str(e))
        
    try:    

        def df_head_values(self):
            return self.df_head
        
        def df_shape_values(self):
            return self.df_shape
        
        def df_tail_values(self):
            return self.df_tail
        
        def df_columns_values(self):
            return self.df_columns
        
        def df_des_values(self):
            return self.df_des
        
        def df_type_values(self):
            return self.df_type
        
        def df_duplicate_values(self):
            return self.df_duplicate
        
        def df_null_values(self):
            return self.df_null
        
        def df_unique_values(self):
            return self.df_unique
        
    except Exception as e:
        raise Exception(f'Error find in data function level :\n'+str(e))
    



continuous_variables=['0_pPeak','0_tPeak','0_rPeak','0_sPeak','0_qPeak','0_qrs_morph0','0_qrs_morph1','0_qrs_morph2','0_qrs_morph3','0_qrs_morph4',
                      '1_pPeak','1_tPeak','1_rPeak','1_sPeak','1_qPeak','1_qrs_morph0','1_qrs_morph1','1_qrs_morph2','1_qrs_morph3','1_qrs_morph4']
discrete_categorical=['record','type']

discrete_count=['0_pre-RR','0_post-RR','0_qrs_interval','0_pq_interval','0_qt_interval','0_st_interval','1_pre-RR','1_post-RR','1_qrs_interval',
                '1_pq_interval','1_qt_interval','1_st_interval']

df[continuous_variables].plot()
plt.title("Countinuous Variables Plot")
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/countinuous_variables.png")

df[discrete_count].plot()
plt.title("Discrete Count Variables Plot")
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/discrete_count.png")
