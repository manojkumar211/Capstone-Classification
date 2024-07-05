import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from eda import df




df['Glucose'].replace(0,df['Glucose'].median(),inplace=True)
df['BloodPressure'].replace(0,df['BloodPressure'].median(),inplace=True)
df['SkinThickness'].replace(0,df['SkinThickness'].median(),inplace=True)
df['BMI'].replace(0,df['BMI'].median(),inplace=True)


class Glucose_IQR:

    try:

        Glucose_q1=df['Glucose'].quantile(q=0.25)
        Glucose_q2=df['Glucose'].quantile(q=0.50)
        Glucose_q3=df['Glucose'].quantile(q=0.75)

        Glucose_iqr=Glucose_q3-Glucose_q1

        Glucose_lower_limit=Glucose_q1-(1.5*Glucose_iqr)
        Glucose_upper_limit=Glucose_q3+(1.5*Glucose_iqr)

    except Exception as e:
        raise Exception(f'Error find in Glucose_IQR :\n'+str(e))

    def __init__(self,Glucose_q1,Glucose_q2,Glucose_q3,Glucose_iqr,Glucose_lower_limit,Glucose_upper_limit):

        try:

            self.Glucose_q1=Glucose_q1
            self.Glucose_q2=Glucose_q2
            self.Glucose_q3=Glucose_q3
            self.Glucose_iqr=Glucose_iqr
            self.Glucose_lower_limit=Glucose_lower_limit
            self.Glucose_upper_limit=Glucose_upper_limit

        except Exception as e:
            raise Exception(f'Error find in Glucose_IQR init level :\n'+str(e))
        
    try:

        def Glucose_column_q1(self):
            return self.Glucose_q1
        
        def Glucose_column_q2(self):
            return self.Glucose_q2
        
        def Glucose_column_q3(self):
            return self.Glucose_q3
        
        def Glucose_column_iqr(self):
            return self.Glucose_iqr
        
        def Glucose_column_lower_limit(self):
            return self.Glucose_lower_limit
        
        def Glucose_column_upper_limit(self):
            return self.Glucose_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in Glucose_IQR column level :\n'+str(e))
    

df[(df['Glucose']>Glucose_IQR.Glucose_upper_limit) | (df['Glucose']<Glucose_IQR.Glucose_lower_limit)]

df['Glucose']=df['Glucose'].clip(lower=Glucose_IQR.Glucose_lower_limit, upper=Glucose_IQR.Glucose_upper_limit)


# Glucose column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Glucose'],ax=ax)
    plt.title('Box plot for Glucose Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Glucose/Glucose_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))




class BloodPressure_IQR:

    try:

        BloodPressure_q1=df['BloodPressure'].quantile(q=0.25)
        BloodPressure_q2=df['BloodPressure'].quantile(q=0.50)
        BloodPressure_q3=df['BloodPressure'].quantile(q=0.75)

        BloodPressure_iqr=BloodPressure_q3-BloodPressure_q1

        BloodPressure_lower_level=BloodPressure_q1-(1.5*BloodPressure_iqr)
        BloodPressure_upper_level=BloodPressure_q3+(1.5*BloodPressure_iqr)

    except Exception as e:
        raise Exception(f'Error find in BloodPressure_IQR :\n'+str(e))

    def __init__(self,BloodPressure_q1,BloodPressure_q2,BloodPressure_q3,BloodPressure_iqr,BloodPressure_lower_level,BloodPressure_upper_level):

        try:

            self.BloodPressure_q1=BloodPressure_q1
            self.BloodPressure_q2=BloodPressure_q2
            self.BloodPressure_q3=BloodPressure_q3
            self.BloodPressure_iqr=BloodPressure_iqr
            self.BloodPressure_lower_level=BloodPressure_lower_level
            self.BloodPressure_upper_level=BloodPressure_upper_level

        except Exception as e:
            raise Exception(f'Error find in BloodPressure_IQR init level :\n'+str(e))
        
    try:

        def BloodPressure_column_q1(self):
            return self.BloodPressure_q1
        
        def BloodPressure_column_q2(self):
            return self.BloodPressure_q2
        
        def BloodPressure_column_q3(self):
            return self.BloodPressure_q3
        
        def BloodPressure_column_iqr(self):
            return self.BloodPressure_iqr
        
        def BloodPressure_column_lower_level(self):
            return self.BloodPressure_lower_level
        
        def BloodPressure_column_upper_level(self):
            return self.BloodPressure_upper_level
        
    except Exception as e:
        raise Exception(f'Error find in BloodPressure_IQR column level :\n'+str(e))
    

df[(df['BloodPressure']>BloodPressure_IQR.BloodPressure_upper_level) | (df['BloodPressure']<BloodPressure_IQR.BloodPressure_lower_level)]

df['BloodPressure']=df['BloodPressure'].clip(lower=BloodPressure_IQR.BloodPressure_lower_level, upper=BloodPressure_IQR.BloodPressure_upper_level)

# BloodPressure column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['BloodPressure'],ax=ax)
    plt.title('Box plot for BloodPressure Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BloodPressure/BloodPressure_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))





class SkinThickness_IQR:

    try:

        SkinThickness_q1=df['SkinThickness'].quantile(0.25)
        SkinThickness_q2=df['SkinThickness'].quantile(0.50)
        SkinThickness_q3=df['SkinThickness'].quantile(0.75)

        SkinThickness_iqr=SkinThickness_q3-SkinThickness_q1

        SkinThickness_lower_limit=SkinThickness_q1-(1.5*SkinThickness_iqr)
        SkinThickness_upper_limit=SkinThickness_q3+(1.5*SkinThickness_iqr)

    except Exception as e:
        raise Exception(f'Error find in SkinThickness_IQR :\n'+str(e))
    

    def __init__(self,SkinThickness_q1,SkinThickness_q2,SkinThickness_q3,SkinThickness_iqr,SkinThickness_lower_limit,SkinThickness_upper_limit):

        try:

            self.SkinThickness_q1 = SkinThickness_q1
            self.SkinThickness_q2 = SkinThickness_q2
            self.SkinThickness_q3 = SkinThickness_q3
            self.SkinThickness_iqr = SkinThickness_iqr
            self.SkinThickness_lower_limit = SkinThickness_lower_limit
            self.SkinThickness_upper_limit= SkinThickness_upper_limit

        except Exception as e:
            raise Exception(f'Error find in SkinThickness_IQR init level :\n'+str(e))
        
    try:

        def SkinThickness_column_q1(self):
            return self.SkinThickness_q1
        
        def SkinThickness_column_q2(self):
            return self.SkinThickness_q2
        
        def SkinThickness_column_q3(self):
            return self.SkinThickness_q3
        
        def SkinThickness_column_iqr(self):
            return self.SkinThickness_iqr
        
        def SkinThickness_column_lower_limit(self):
            return self.SkinThickness_lower_limit
        
        def SkinThickness_column_upper_limit(self):
            return self.SkinThickness_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in SkinThickness_IQR column level :\n'+str(e))
    

    
df[(df['SkinThickness']>SkinThickness_IQR.SkinThickness_upper_limit) | (df['SkinThickness']<SkinThickness_IQR.SkinThickness_lower_limit)]

df['SkinThickness']=df['SkinThickness'].clip(lower=SkinThickness_IQR.SkinThickness_lower_limit,upper=SkinThickness_IQR.SkinThickness_upper_limit)


# SkinThickness column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['SkinThickness'],ax=ax)
    plt.title('Box plot for SkinThickness Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/SkinThickness/SkinThickness_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))





class BMI_IQR:

    try:

        BMI_q1=df['BMI'].quantile(q=0.25)
        BMI_q2=df['BMI'].quantile(q=0.50)
        BMI_q3=df['BMI'].quantile(q=0.75)

        BMI_iqr=BMI_q3-BMI_q1

        BMI_lower_limit=BMI_q1-(1.5*BMI_iqr)
        BMI_upper_limit=BMI_q3+(1.5*BMI_iqr)

    except Exception as e:
        raise Exception(f'Error find in BMI_IQR :\n'+str(e))
    

    def __init__(self,BMI_q1,BMI_q2,BMI_q3,BMI_iqr,BMI_lower_limit,BMI_upper_limit):

        try:

            self.BMI_q1=BMI_q1
            self.BMI_q2=BMI_q2
            self.BMI_q3=BMI_q3
            self.BMI_iqr=BMI_iqr
            self.BMI_lower_limit=BMI_lower_limit
            self.BMI_upper_limit=BMI_upper_limit

        except Exception as e:
            raise Exception(f'Error find in BMI_IQR init level :\n'+str(e))
        
    try:

    
        def BMI_column_q1(self):
            return self.BMI_q1
        
        def BMI_column_q2(self):
            return self.BMI_q2
        
        def BMI_column_q3(self):
            return self.BMI_q3
        
        def BMI_column_iqr(self):
            return self.BMI_iqr
        
        def BMI_column_lower_limit(self):
            return self.BMI_lower_limit
        
        def BMI_column_upper_limit(self):
            return self.BMI_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in BMI_IQR column level :\n'+str(e))
    

df[(df['BMI']>BMI_IQR.BMI_upper_limit) | (df['BMI']<BMI_IQR.BMI_lower_limit)]

df['BMI']=df['BMI'].clip(lower=BMI_IQR.BMI_lower_limit,upper=BMI_IQR.BMI_upper_limit)


# BMI column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['BMI'],ax=ax)
    plt.title('Box plot for BMI Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/BMI/BMI_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

        

class Pregnancies_IQR:

    try:

        Pregnancies_q1=df['Pregnancies'].quantile(q=0.25)
        Pregnancies_q2=df['Pregnancies'].quantile(q=0.50)
        Pregnancies_q3=df['Pregnancies'].quantile(q=0.75)

        Pregnancies_iqr=Pregnancies_q3-Pregnancies_q1

        Pregnancies_lower_limit=Pregnancies_q1-(1.5*Pregnancies_iqr)
        Pregnancies_upper_limit=Pregnancies_q3+(1.5*Pregnancies_iqr)

    except Exception as e:
        raise Exception(f'Error find in Pregnancies_IQR :\n'+str(e))
    

    def __init__(self,Pregnancies_q1,Pregnancies_q2,Pregnancies_q3,Pregnancies_iqr,Pregnancies_lower_limit,Pregnancies_upper_limit):

        try:

            self.Pregnancies_q1=Pregnancies_q1
            self.Pregnancies_q2=Pregnancies_q2
            self.Pregnancies_q3=Pregnancies_q3
            self.Pregnancies_iqr=Pregnancies_iqr
            self.Pregnancies_lower_limit=Pregnancies_lower_limit
            self.Pregnancies_upper_limit=Pregnancies_upper_limit

        except Exception as e:
            raise Exception(f'Error find in Pregnancies_IQR init level :\n'+str(e))
        
    try:

        def Pregnancies_column_q1(self):
            return self.Pregnancies_q1
        
        def Pregnancies_column_q2(self):
            return self.Pregnancies_q2
        
        def Pregnancies_column_q3(self):
            return self.Pregnancies_q3
        
        def Pregnancies_column_iqr(self):
            return self.Pregnancies_iqr
        
        def Pregnancies_column_lower_limit(self):
            return self.Pregnancies_lower_limit
        
        def Pregnancies_column_upper_limit(self):
            return self.Pregnancies_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in Pregnancies_IQR column level :\n'+str(e))
    
    
df[(df['Pregnancies']>Pregnancies_IQR.Pregnancies_upper_limit) | (df['Pregnancies']<Pregnancies_IQR.Pregnancies_lower_limit)]

df['Pregnancies']=df['Pregnancies'].clip(lower=Pregnancies_IQR.Pregnancies_lower_limit,upper=Pregnancies_IQR.Pregnancies_upper_limit)

# Pregnancies column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Pregnancies'],ax=ax)
    plt.title('Box plot for Pregnancies Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Pregnancies/Pregnancies_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))




class Insulin_IQR:

    try:

        Insulin_q1=df['Insulin'].quantile(q=0.25)
        Insulin_q2=df['Insulin'].quantile(q=0.50)
        Insulin_q3=df['Insulin'].quantile(q=0.75)
        
        Insulin_iqr=Insulin_q3-Insulin_q1

        Insulin_lower_limit=Insulin_q1-(1.5*Insulin_iqr)
        Insulin_upper_limit=Insulin_q3+(1.5*Insulin_iqr)

    except Exception as e:
        raise Exception(f'Error find in Insulin_IQR :\n'+str(e))

    def __init__(self,Insulin_q1,Insulin_q2,Insulin_q3,Insulin_iqr,Insulin_lower_limit,Insulin_upper_limit):

        try:

            self.Insulin_q1=Insulin_q1
            self.Insulin_q2=Insulin_q2
            self.Insulin_q3=Insulin_q3
            self.Insulin_iqr=Insulin_iqr
            self.Insulin_lower_limit=Insulin_lower_limit
            self.Insulin_upper_limit=Insulin_upper_limit

        except Exception as e:
            raise Exception(f'Error find in Insulin_IQR init level :\n'+str(e))
        
    try:

    
        def Insulin_column_q1(self):
            return self.Insulin_q1
        
        def Insulin_column_q2(self):
            return self.Insulin_q2
        
        def Insulin_column_q3(self):
            return self.Insulin_q3
        
        def Insulin_column_iqr(self):
            return self.Insulin_iqr
        
        def Insulin_column_lower_limit(self):
            return self.Insulin_lower_limit
        
        def Insulin_column_upper_limit(self):
            return self.Insulin_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in Insulin_IQR column level :\n'+str(e))
    

df[(df['Insulin']>Insulin_IQR.Insulin_upper_limit) | (df['Insulin']<Insulin_IQR.Insulin_lower_limit)]

df['Insulin']=df['Insulin'].clip(lower=Insulin_IQR.Insulin_lower_limit,upper=Insulin_IQR.Insulin_upper_limit)


# Insulin column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Insulin'],ax=ax)
    plt.title('Box plot for Insulin Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Insulin/Insulin_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))




class DiabetesPedigreeFunction_IQR:

    try:

        DiabetesPedigreeFunction_q1=df['DiabetesPedigreeFunction'].quantile(q=0.25)
        DiabetesPedigreeFunction_q2=df['DiabetesPedigreeFunction'].quantile(q=0.50)
        DiabetesPedigreeFunction_q3=df['DiabetesPedigreeFunction'].quantile(q=0.75)

        DiabetesPedigreeFunction_iqr=DiabetesPedigreeFunction_q3-DiabetesPedigreeFunction_q1

        DiabetesPedigreeFunction_lower_limit=DiabetesPedigreeFunction_q1-(1.5*DiabetesPedigreeFunction_iqr)
        DiabetesPedigreeFunction_upper_limit=DiabetesPedigreeFunction_q3+(1.5*DiabetesPedigreeFunction_iqr)

    except Exception as e:
        raise Exception(f'Error find in DiabetesPedigreeFunction_IQR :\n'+str(e))
    

    def __init__(self,DiabetesPedigreeFunction_q1,DiabetesPedigreeFunction_q2,DiabetesPedigreeFunction_q3,DiabetesPedigreeFunction_iqr,DiabetesPedigreeFunction_lower_limit,DiabetesPedigreeFunction_upper_limit):

        try:

            self.DiabetesPedigreeFunction_q1=DiabetesPedigreeFunction_q1
            self.DiabetesPedigreeFunction_q2=DiabetesPedigreeFunction_q2
            self.DiabetesPedigreeFunction_q3=DiabetesPedigreeFunction_q3
            self.DiabetesPedigreeFunction_iqr=DiabetesPedigreeFunction_iqr
            self.DiabetesPedigreeFunction_lower_limit=DiabetesPedigreeFunction_lower_limit
            self.DiabetesPedigreeFunction_upper_limit=DiabetesPedigreeFunction_upper_limit

        except Exception as e:
            raise Exception(f'Error find in DiabetesPedigreeFunction_IQR init level :\n'+str(e))
        
    try:

        def DiabetesPedigreeFunction_column_q1(self):
            return self.DiabetesPedigreeFunction_q1
        
        def DiabetesPedigreeFunction_column_q2(self):
            return self.DiabetesPedigreeFunction_q2
        
        def DiabetesPedigreeFunction_column_q3(self):
            return self.DiabetesPedigreeFunction_q3
        
        def DiabetesPedigreeFunction_column_iqr(self):
            return self.DiabetesPedigreeFunction_iqr
        
        def DiabetesPedigreeFunction_column_lower_limit(self):
            return self.DiabetesPedigreeFunction_lower_limit
        
        def DiabetesPedigreeFunction_column_upper_limit(self):
            return self.DiabetesPedigreeFunction_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in DiabetesPedigreeFunction_IQR column level :\n'+str(e))
    

df[(df['DiabetesPedigreeFunction']>DiabetesPedigreeFunction_IQR.DiabetesPedigreeFunction_upper_limit) | (df['DiabetesPedigreeFunction']<DiabetesPedigreeFunction_IQR.DiabetesPedigreeFunction_lower_limit)]

df['DiabetesPedigreeFunction']=df['DiabetesPedigreeFunction'].clip(lower=DiabetesPedigreeFunction_IQR.DiabetesPedigreeFunction_lower_limit,upper=DiabetesPedigreeFunction_IQR.DiabetesPedigreeFunction_upper_limit)

# DiabetesPedigreeFunction column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['DiabetesPedigreeFunction'],ax=ax)
    plt.title('Box plot for DiabetesPedigreeFunction Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/DiabetesPedigreeFunction/DiabetesPedigreeFunction_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))




class Age_IQR:

    try:

        Age_q1=df['Age'].quantile(q=0.25)
        Age_q2=df['Age'].quantile(q=0.50)
        Age_q3=df['Age'].quantile(q=0.75)
        
        Age_iqr=Age_q3-Age_q1

        Age_lower_limit=Age_q1-(1.5*Age_iqr)
        Age_upper_limit=Age_q3+(1.5*Age_iqr)

    except Exception as e:
        raise Exception(f'Error find in Age_IQR :\n'+str(e))
    

    def __init__(self,Age_q1,Age_q2,Age_q3,Age_iqr,Age_lower_limit,Age_upper_limit):

        try:

            self.Age_q1=Age_q1
            self.Age_q2=Age_q2
            self.Age_q3=Age_q3
            self.Age_iqr=Age_iqr
            self.Age_lower_limit=Age_lower_limit
            self.Age_upper_limit=Age_upper_limit

        except Exception as e:
            raise Exception(f'Error find in Age_IQR init level :\n'+str(e))
        
    try:

        def Age_column_q1(self):
            return self.Age_q1
        
        def Age_column_q2(self):
            return self.Age_q2
        
        def Age_column_q3(self):
            return self.Age_q3
        
        def Age_column_iqr(self):
            return self.Age_iqr
        
        def Age_column_lower_limit(self):
            return self.Age_lower_limit
        
        def Age_column_upper_limit(self):
            return self.Age_upper_limit
        
    except Exception as e:
        raise Exception(f'Error find in Age_IQR column level :\n'+str(e))
    

df[(df['Age']>Age_IQR.Age_upper_limit) | (df['Age']<Age_IQR.Age_lower_limit)]

df['Age']=df['Age'].clip(lower=Age_IQR.Age_lower_limit,upper=Age_IQR.Age_upper_limit)

# Age column box plot after Outliers:

try:

    fig,ax=plt.subplots(figsize=(5,5))
    sns.boxplot(data=df['Age'],ax=ax)
    plt.title('Box plot for Age Column after Outliers')
    plt.savefig('C:/AI&ML Engineer/Projects/Apple/diabetes Prediction/plots/Age/Age_box_outliers.png')

except Exception as e:
    raise Exception(f'error find in box plot :\n'+str(e))

