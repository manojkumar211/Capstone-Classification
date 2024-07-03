import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the data:

df=pd.read_csv("C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/diabetes.csv")


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
    



continuous_variables=['BMI','DiabetesPedigreeFunction']
discrete_categorical=['Outcome']

discrete_count=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','Age']


try:

    df[continuous_variables].plot()
    plt.title("Countinuous Variables Plot")
    plt.savefig("C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/countinuous_variables.png")

except Exception as e:
    raise Exception(f'error find in continuous variable plot :\n'+str(e))


try:

    df[discrete_count].plot()
    plt.title("Discrete Count Variables Plot")
    plt.savefig("C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/discrete_count.png")

except Exception as e:
    raise Exception(f'error find in discrete count variable plot :\n'+str(e))


try:

    fig,ax=plt.subplots(figsize=(10,5))
    sns.heatmap(df[continuous_variables].corr(),annot=True,cmap='Set2',ax=ax)
    plt.title('Heatmap for all continuous variables')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/countinuous_variables_heatmap.png')

except Exception as e:
    raise Exception(f'error find in continuous variable heatmap :\n'+str(e))


