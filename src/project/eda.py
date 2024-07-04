import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df


# Column wise Analysis:

class Pregnancies_column:
        
    try:

        Pregnancies_unique=df['Pregnancies'].unique()
        Pregnancies_des=df['Pregnancies'].describe()
        Pregnancies_null=df['Pregnancies'].isnull().sum()
        Pregnancies_mode=df['Pregnancies'].mode()[0]
        Pregnancies_skew=df['Pregnancies'].skew()
        Pregnancies_var=df['Pregnancies'].var(ddof=0)
        Pregnancies_std=df['Pregnancies'].std(ddof=0)
        Pregnancies_corr=df[['Pregnancies','Outcome']].corr()

    except Exception as e:
        raise Exception(f'Error find in Pregnancies_column :\n'+str(e))

  

    def __init__(self,Pregnancies_unique,Pregnancies_des,Pregnancies_null,Pregnancies_mode,Pregnancies_skew,Pregnancies_var,Pregnancies_std,Pregnancies_corr):

        try:
        
            self.Pregnancies_unique=Pregnancies_unique
            self.Pregnancies_des=Pregnancies_des
            self.Pregnancies_null=Pregnancies_null
            self.Pregnancies_mode=Pregnancies_mode
            self.Pregnancies_skew=Pregnancies_skew
            self.Pregnancies_var=Pregnancies_var
            self.Pregnancies_std=Pregnancies_std
            self.Pregnancies_corr=Pregnancies_corr
        
        except Exception as e:
            raise Exception(f'Error find in Pregnancies_column at init level :\n'+str(e))

    
    try:

        def Pregnancies_unique_column(self):
            return self.Pregnancies_unique
        
        def Pregnancies_des_column(self):
            return self.Pregnancies_des
        
        def Pregnancies_null_column(self):
            return self.Pregnancies_null
        
        def Pregnancies_mode_column(self):
            return self.Pregnancies_mode
        
        def Pregnancies_skew_column(self):
            return self.Pregnancies_skew
        
        def Pregnancies_var_column(self):
            return self.Pregnancies_var
        
        def Pregnancies_std_column(self):
            return self.Pregnancies_std
        
        def Pregnancies_corr_column(self):
            return self.Pregnancies_corr
    
    except Exception as e:
        raise Exception(f'Error find in Pregnancies_column at function level :\n'+str(e))
    
    
    

# Pregnancies column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['Pregnancies'],ax=ax)
    plt.title('Histo plot for Pregnancies Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Pregnancies/Pregnancies_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))


# Pregnancies column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['Pregnancies'],ax=ax,color='r')
    plt.title('Distribution plot for Pregnancies Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Pregnancies/Pregnancies_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# Pregnancies column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Pregnancies'],ax=ax)
    plt.title('Box plot for Pregnancies Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Pregnancies/Pregnancies_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))


# Pregnancies column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['Pregnancies'],ax=ax)
    plt.title('Scatter plot for Pregnancies Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Pregnancies/Pregnancies_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))



try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['Pregnancies','Outcome']].corr(),annot=True,cmap='CMRmap',ax=ax)
    plt.title('HeatMap plot for Pregnancies Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Pregnancies/Pregnancies_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))




# Glucose Column:-

class Glucose_column:

    try:

        Glucose_unique=df['Glucose'].unique()
        Glucose_count=df['Glucose'].value_counts()
        Glucose_mode=df['Glucose'].mode()[0]
        Glucose_null=df['Glucose'].isnull().sum()

    except Exception as e:
        raise Exception(f'Error find in Glucose_column :\n'+str(e))

    def __init__(self, Glucose_unique, Glucose_count, Glucose_mode, Glucose_null):

        try:

            self.Glucose_unique = Glucose_unique
            self.Glucose_count = Glucose_count
            self.Glucose_mode = Glucose_mode
            self.Glucose_null = Glucose_null

        except Exception as e:
            raise Exception(f'Error find in Glucose_column at init level :\n' + str(e))
        
    try: 

        def Glucose_unique_column(self):
            return self.Glucose_unique
        
        def Glucose_count_column(self):
            return self.Glucose_count
        
        def Glucose_mode_column(self):
            return self.Glucose_mode
        
        def Glucose_null_column(self):
            return self.Glucose_nul
        
    except Exception as e:
        raise Exception(f'Error find in Glucose_column at function level :\n' + str(e))
    

# Glucose column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    plt.bar(x='Glucose',data=df,height=0.8)
    plt.title('Bar plot for Glucose column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Glucose/Glucose_bar.png')

except Exception as e:
    raise Exception(f'error find in bar plot :\n'+str(e))



try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['Glucose','Outcome']].corr(),annot=True,cmap='PuRd',ax=ax)
    plt.title('HeatMap plot for Glucose Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Glucose/Glucose_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))



try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['Glucose'],ax=ax)
    plt.title('Histo plot for Glucose Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Glucose/Glucose_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))


# Pregnancies column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['Glucose'],ax=ax,color='r')
    plt.title('Distribution plot for Glucose Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Glucose/Glucose_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# Pregnancies column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Glucose'],ax=ax)
    plt.title('Box plot for Glucose Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Glucose/Glucose_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))





# BloodPressure column:-

class BloodPressure_column:

    try:

        BloodPressure_des=df['BloodPressure'].describe()
        BloodPressure_null=df['BloodPressure'].isnull().sum()
        BloodPressure_skewness=df['BloodPressure'].skew()
        BloodPressure_var=df['BloodPressure'].var(ddof=0)
        BloodPressure_std=df['BloodPressure'].std(ddof=0)
        BloodPressure_cov=df[['BloodPressure','Outcome']].cov()
        BloodPressure_corr=df[['BloodPressure','Outcome']].corr()

    except Exception as e:
        raise Exception(f'Error find in BloodPressure_column :\n'+str(e))
    

    def __init__(self,BloodPressure_des,BloodPressure_null,BloodPressure_skewness,BloodPressure_var,BloodPressure_std,BloodPressure_cov,BloodPressure_corr):

        try:

            self.BloodPressure_des=BloodPressure_des
            self.BloodPressure_null=BloodPressure_null
            self.BloodPressure_skewness=BloodPressure_skewness
            self.BloodPressure_var=BloodPressure_var
            self.BloodPressure_std=BloodPressure_std
            self.BloodPressure_cov=BloodPressure_cov
            self.BloodPressure_corr=BloodPressure_corr

        except Exception as e:
            raise Exception(f'Error find in BloodPressure_column at init level :\n' + str(e))

    try:

        def BloodPressure_des_column(self):
            return self.BloodPressure_des
        
        def BloodPressure_null_column(self):
            return self.BloodPressure_null
        
        def BloodPressure_skewness_column(self):
            return self.BloodPressure_skewness
        
        def BloodPressure_var_column(self):
            return self.BloodPressure_var
        
        def BloodPressure_std_column(self):
            return self.BloodPressure_std
        
        def BloodPressure_cov_column(self):
            return self.BloodPressure_cov
        
        def BloodPressure_corr_column(self):
            return self.BloodPressure_corr
        
    except Exception as e:
        raise Exception(f'Error find in BloodPressure_column at function level :\n' + str(e))
    
    
# BloodPressure column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['BloodPressure'],ax=ax)
    plt.title('Histo plot for BloodPressure Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BloodPressure/BloodPressure_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# BloodPressure column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['BloodPressure'],ax=ax,color='r')
    plt.title('Distribution plot for BloodPressure Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BloodPressure/BloodPressure_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# BloodPressure column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['BloodPressure'],ax=ax)
    plt.title('Box plot for BloodPressure Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BloodPressure/BloodPressure_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# BloodPressure column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['BloodPressure'],ax=ax)
    plt.title('Scatter plot for BloodPressure Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BloodPressure/BloodPressure_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))


# BloodPressure column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['BloodPressure','Outcome']].corr(),annot=True,cmap='gist_ncar',ax=ax)
    plt.title('HeatMap plot for BloodPressure Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BloodPressure/BloodPressure_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))



# SkinThickness column analysis:-

class SkinThickness_column:

    try:

        SkinThickness_des=df['SkinThickness'].describe()
        SkinThickness_null=df['SkinThickness'].isnull().sum()
        SkinThickness_skewness=df['SkinThickness'].skew()
        SkinThickness_var=df['SkinThickness'].var(ddof=0)
        SkinThickness_std=df['SkinThickness'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in SkinThickness_column :\n'+str(e))
    

    def __init__(self,SkinThickness_des,SkinThickness_null,SkinThickness_skewness,SkinThickness_var,SkinThickness_std):

        try:

            self.SkinThickness_des=SkinThickness_des
            self.SkinThickness_null=SkinThickness_null
            self.SkinThickness_skewness=SkinThickness_skewness
            self.SkinThickness_var=SkinThickness_var
            self.SkinThickness_std=SkinThickness_std

        except Exception as e:
            raise Exception(f'Error find in SkinThickness_column at init level :\n' + str(e))
        

    try:

        def SkinThickness_des_column(self):
            return self.SkinThickness_des
        
        def SkinThickness_null_column(self):
            return self.SkinThickness_null
        
        def SkinThickness_skewness_column(self):
            return self.SkinThickness_skewness
        
        def SkinThickness_var_column(self):
            return self.SkinThickness_var
        
        def SkinThickness_std_column(self):
            return self.SkinThickness_std
        
    except Exception as e:
        raise Exception(f'Error find in SkinThickness_column at function level :\n' + str(e))
    
# SkinThickness column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['SkinThickness'],ax=ax)
    plt.title('Histo plot for SkinThickness Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SkinThickness/SkinThickness_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# SkinThickness column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['SkinThickness'],ax=ax,color='r')
    plt.title('Distribution plot for SkinThickness Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SkinThickness/SkinThickness_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# SkinThickness column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['SkinThickness'],ax=ax)
    plt.title('Box plot for SkinThickness Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SkinThickness/SkinThickness_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# SkinThickness column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['SkinThickness'],ax=ax)
    plt.title('Scatter plot for SkinThickness Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SkinThickness/SkinThickness_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))

# SkinThickness column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['SkinThickness','Outcome']].corr(),annot=True,cmap='OrRd',ax=ax)
    plt.title('HeatMap plot for SkinThickness Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SkinThickness/SkinThickness_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))

    

# Insulin column analysis:

class Insulin_column:

    try:

        Insulin_des=df['Insulin'].describe()
        Insulin_null=df['Insulin'].isnull().sum()
        Insulin_skewness=df['Insulin'].skew()
        Insulin_var=df['Insulin'].var(ddof=0)
        Insulin_std=df['Insulin'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in Insulin_column :\n'+str(e))
    

    def __init__(self,Insulin_des,Insulin_null,Insulin_skewness,Insulin_var,Insulin_std):

        try:

            self.Insulin_des=Insulin_des
            self.Insulin_null=Insulin_null
            self.Insulin_skewness=Insulin_skewness
            self.Insulin_var=Insulin_var
            self.Insulin_std=Insulin_std

        except Exception as e:
            raise Exception(f'Error find in Insulin_column at init level :\n' + str(e))
        
    try:

        def Insulin_des_column(self):
            return self.Insulin_des
        
        def Insulin_null_column(self):
            return self.Insulin_null
        
        def Insulin_skewness_column(self):
            return self.Insulin_skewness
        
        def Insulin_var_column(self):
            return self.Insulin_var
        
        def Insulin_std_column(self):
            return self.Insulin_std
        
    except Exception as e:
        raise Exception(f'Error find in Insulin_column at function level :\n' + str(e))
    
    
# Insulin column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['Insulin'],ax=ax)
    plt.title('Histo plot for Insulin Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Insulin/Insulin_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# Insulin column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['Insulin'],ax=ax,color='r')
    plt.title('Distribution plot for Insulin Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Insulin/Insulin_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# Insulin column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Insulin'],ax=ax)
    plt.title('Box plot for Insulin Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Insulin/Insulin_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# Insulin column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['Insulin'],ax=ax)
    plt.title('Scatter plot for Insulin Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Insulin/Insulin_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))

# Insulin column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['Insulin','Outcome']].corr(),annot=True,cmap='cividis',ax=ax)
    plt.title('HeatMap plot for Insulin Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Insulin/Insulin_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))



# BMI column analysis:

class BMI_column:

    try:

        BMI_des=df['BMI'].describe()
        BMI_null=df['BMI'].isnull().sum()
        BMI_skewness=df['BMI'].skew()
        BMI_var=df['BMI'].var(ddof=0)
        BMI_std=df['BMI'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in BMI_column :\n'+str(e))


    def __init__(self,BMI_des,BMI_null,BMI_skewness,BMI_var,BMI_std):

        try:

            self.BMI_des = BMI_des
            self.BMI_null = BMI_null
            self.BMI_skewness = BMI_skewness
            self.BMI_var = BMI_var
            self.BMI_std = BMI_std

        except Exception as e:
            raise Exception(f'Error find in BMI_column at init level :\n' + str(e))
        
    try:

        def BMI_des_column(self):
            return self.BMI_des
        
        def BMI_null_column(self):
            return self.BMI_null
        
        def BMI_skewness_column(self):
            return self.BMI_skewness
        
        def BMI_var_column(self):
            return self.BMI_var
        
        def BMI_std_column(self):
            return self.BMI_std
        
    except Exception as e:
        raise Exception(f'Error find in BMI_column at function level :\n' + str(e))
    
    
# BMI column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['BMI'],ax=ax)
    plt.title('Histo plot for BMI Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BMI/BMI_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# BMI column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['BMI'],ax=ax,color='r')
    plt.title('Distribution plot for BMI Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BMI/BMI_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# BMI column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['BMI'],ax=ax)
    plt.title('Box plot for BMI Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BMI/BMI_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# BMI column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['BMI'],ax=ax)
    plt.title('Scatter plot for BMI Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BMI/BMI_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))

# BMI column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['BMI','Outcome']].corr(),annot=True,cmap='Greens',ax=ax)
    plt.title('HeatMap plot for BMI Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BMI/BMI_heatmap.png')

except Exception as e:
    raise Exception(f'error find in heatmap plot :\n'+str(e))


# DiabetesPedigreeFunction column analysis:

class DiabetesPedigreeFunction_column:

    try:

        DiabetesPedigreeFunction_des=df['DiabetesPedigreeFunction'].describe()
        DiabetesPedigreeFunction_null=df['DiabetesPedigreeFunction'].isnull().sum()
        DiabetesPedigreeFunction_skewness=df['DiabetesPedigreeFunction'].skew()
        DiabetesPedigreeFunction_var=df['DiabetesPedigreeFunction'].var(ddof=0)
        DiabetesPedigreeFunction_std=df['DiabetesPedigreeFunction'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in DiabetesPedigreeFunction_column :\n'+str(e))

    def __init_(self,DiabetesPedigreeFunction_des,DiabetesPedigreeFunction_null,DiabetesPedigreeFunction_skewness,DiabetesPedigreeFunction_var,DiabetesPedigreeFunction_std):

        try:

            self.DiabetesPedigreeFunction_des = DiabetesPedigreeFunction_des
            self.DiabetesPedigreeFunction_null = DiabetesPedigreeFunction_null
            self.DiabetesPedigreeFunction_skewness = DiabetesPedigreeFunction_skewness
            self.DiabetesPedigreeFunction_var = DiabetesPedigreeFunction_var
            self.DiabetesPedigreeFunction_std = DiabetesPedigreeFunction_std

        except Exception as e:
            raise Exception(f'Error find in DiabetesPedigreeFunction_column at init level :\n' + str(e))
        
    try:


        def DiabetesPedigreeFunction_des_column(self):
            return self.DiabetesPedigreeFunction_des
        
        def DiabetesPedigreeFunction_null_column(self):
            return self.DiabetesPedigreeFunction_null
        
        def DiabetesPedigreeFunction_skewness_column(self):
            return self.DiabetesPedigreeFunction_skewness
        
        def DiabetesPedigreeFunction_var_column(self):
            return self.DiabetesPedigreeFunction_var
        
        def DiabetesPedigreeFunction_std_column(self):
            return self.DiabetesPedigreeFunction_std
        
    except Exception as e:
        raise Exception(f'Error find in DiabetesPedigreeFunction_column at function level :\n' + str(e))
    
# DiabetesPedigreeFunction column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['DiabetesPedigreeFunction'],ax=ax)
    plt.title('Histo plot for DiabetesPedigreeFunction Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/DiabetesPedigreeFunction/DiabetesPedigreeFunction_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot :\n'+str(e))

# DiabetesPedigreeFunction column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['DiabetesPedigreeFunction'],ax=ax,color='r')
    plt.title('Distribution plot for DiabetesPedigreeFunction Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/DiabetesPedigreeFunction/DiabetesPedigreeFunction_dist.png')

except Exception as e:
    raise Exception(f'error find in distribution plot :\n'+str(e))

# DiabetesPedigreeFunction column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['DiabetesPedigreeFunction'],ax=ax)
    plt.title('Box plot for DiabetesPedigreeFunction Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/DiabetesPedigreeFunction/DiabetesPedigreeFunction_box.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

# DiabetesPedigreeFunction column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['DiabetesPedigreeFunction'],ax=ax)
    plt.title('Scatter plot for DiabetesPedigreeFunction Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/DiabetesPedigreeFunction/DiabetesPedigreeFunction_scatter.png')

except Exception as e:
    raise Exception(f'error find in scatter plot :\n'+str(e))

# DiabetesPedigreeFunction column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['DiabetesPedigreeFunction','Outcome']].corr(),annot=True,cmap='winter',ax=ax)
    plt.title('HeatMap plot for DiabetesPedigreeFunction Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/DiabetesPedigreeFunction/DiabetesPedigreeFunction_heatmap.png')

except Exception as e:
    raise Exception('error find in Heatmap plot :\n'+str(e))


# Age column analysis:

class Age_column:

    try:

        Age_des=df['Age'].describe()
        Age_null=df['Age'].isnull().sum()
        Age_skewness=df['Age'].skew()
        Age_var=df['Age'].var(ddof=0)
        Age_std=df['Age'].std(ddof=0)

    except Exception as e:
        raise Exception(f'Error find in Age_column :\n'+str(e))
    

    def __init__(self,Age_des,Age_null,Age_skewness,Age_var,Age_std):

        try:

            self.Age_des = Age_des
            self.Age_null = Age_null
            self.Age_skewness = Age_skewness
            self.Age_var = Age_var
            self.Age_std = Age_std

        except Exception as e:
            raise Exception(f'Error find in Age_column at init level :\n' + str(e))
        
    try:

        def Age_des_column(self):
            return self.Age_des
        
        def Age_null_column(self):
            return self.Age_null
        
        def Age_skewness_column(self):
            return self.Age_skewness
        
        def Age_var_column(self):
            return self.Age_var
        
        def Age_std_column(self):
            return self.Age_std
        
    except Exception as e:
        raise Exception(f'Error find in Age_column at function level :\n' + str(e))
    

# Age column histo plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.histplot(data=df['Age'],ax=ax)
    plt.title('Histo plot for Age Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Age/Age_histo.png')

except Exception as e:
    raise Exception(f'error find in histo plot for Age :\n'+str(e))

# Age column distribution plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.kdeplot(data=df['Age'],ax=ax,color='r')
    plt.title('Distribution plot for Age Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Age/Age_dist.png')

except Exception as e:
    raise Exception(f'error in distribution plot for Age :\n'+str(e))

# Age column box plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Age'],ax=ax)
    plt.title('Box plot for Age Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Age/Age_box.png')

except Exception as e:
    raise Exception(f'error find in Box plot for Age :\n'+str(e))

# Age column scatter plot:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.scatterplot(data=df['Age'],ax=ax)
    plt.title('Scatter plot for Age Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Age/Age_scatter.png')

except Exception as e:
    raise Exception(f'error find in Scatter plot for Age :\n'+str(e))

# Age column heatmap plot:

try:

    fig,ax=plt.subplots(figsize=(8,5))
    sns.heatmap(df[['Age','Outcome']].corr(),annot=True,cmap='winter',ax=ax)
    plt.title('HeatMap plot for Age Column')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Age/Age_heatmap.png')

except Exception as e:
    raise Exception(f'error find in Heatmap plot for Age :\n'+str(e))



# Outcome column analysis:


class Outcome_column:

    Outcome_unique=df['Outcome'].unique()
    Outcome_values=df['Outcome'].value_counts()
    Outcome_nunique=df['Outcome'].nunique()
    Outcome_null=df['Outcome'].isnull().sum()


    def __init__(self,Outcome_unique,Outcome_values,Outcome_nunique,Outcome_null):

        self.Outcome_unique = Outcome_unique
        self.Outcome_values = Outcome_values
        self.Outcome_nunique = Outcome_nunique
        self.Outcome_null = Outcome_null


    def Outcome_unique_column(self):
        return self.Outcome_unique
    
    def Outcome_values_column(self):
        return self.Outcome_values
    
    def Outcome_nunique_column(self):
        return self.Outcome_nunique
    
    def Outcome_null_column(self):
        return self.Outcome_null
    

# Outcome column pie plot:

try:

    fig,ax=plt.subplots(figsize=(10,5))
    plt.pie(x=df['Outcome'].value_counts(),labels=sorted(df['Outcome'].unique()),autopct='%0.2f%%',explode=[0,0.1])
    plt.title('Pie plot for Outcome column')
    plt.legend()
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Outcome/Outcome_pie.png')

except Exception as e:
    raise Exception(f'error find in pie plot :\n'+str(e))

# Outcome column count plot:


try:

    fig,ax=plt.subplots(figsize=(10,5))
    sns.countplot(data=df,x=df['Outcome'],hue='Outcome',ax=ax)
    plt.title('Count plot for Outcome column')
    plt.legend(df['Outcome'].unique())
    plt.legend(df['Outcome'].value_counts())
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Outcome/Outcome_count.png')

except Exception as e:
    raise Exception(f'error find in count plot :\n'+str(e))